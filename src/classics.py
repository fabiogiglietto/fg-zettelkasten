"""Suggest the works the vault's own papers cite most but the vault does not hold.

The archive fills from the `toread` feed, so it is strong on what was published
after it launched and blind to the literature those papers stand on. This module
finds that literature: it keeps each note's OpenAlex reference list in
`data/citations.json`, counts how many notes cite each outside work, and reports
the most-cited ones as *candidates*.

It deliberately stops at a report. A candidate has no bibtex key, and `toread`
owns that namespace — so a chosen work is added upstream (Paperpile) and arrives
through the feed like any other paper. Nothing here writes a note or calls an LLM.

The ranking is a candidate generator, not a selector: OpenAlex has reference
lists for about three quarters of the notes that carry a DOI (and none for the
rest), skewed towards journal articles in well-indexed fields, so heavily cited
work from thinner-indexed areas is under-counted. The per-topic view exists to make that skew visible.
"""
from __future__ import annotations

import json
import re
from collections import Counter
from datetime import datetime, timedelta, timezone
from difflib import SequenceMatcher
from pathlib import Path
from typing import Any, Optional

from . import state as state_mod
from . import supersede

_BOOK_TYPES = {"book", "monograph"}
_NON_ALNUM_RE = re.compile(r"[^a-z0-9]+")
# Lower-case name particles that belong to the surname ("van Dijck", "Del Vicario").
_PARTICLES = {"van", "von", "de", "del", "della", "di", "da", "den", "der", "la", "le"}


def normalize_doi(doi: Optional[str]) -> str:
    return re.sub(r"^https?://(?:dx\.)?doi\.org/", "", (doi or "").strip(), flags=re.I).lower()


# --- the citations cache ---------------------------------------------------


def load_citations(path: str) -> dict[str, Any]:
    """`{"works": {bibtex_key: {doi, openalex_id, referenced_works, fetched}}}`."""
    file = Path(path)
    if not file.exists():
        return {"works": {}}
    data = json.loads(file.read_text(encoding="utf-8"))
    data.setdefault("works", {})
    return data


def save_citations(data: dict[str, Any], path: str) -> None:
    file = Path(path)
    file.parent.mkdir(parents=True, exist_ok=True)
    file.write_text(
        json.dumps(data, indent=1, sort_keys=True, ensure_ascii=False) + "\n",
        encoding="utf-8",
    )


def stale_keys(
    records: dict[str, supersede.Record],
    cache: dict[str, Any],
    now: datetime,
    recheck_after_days: int = 30,
) -> list[str]:
    """Notes whose reference list should be (re)fetched.

    A published reference list does not change, so a note with references is
    fetched once. One that came back empty — unknown to OpenAlex, or indexed
    without references — is asked about again after `recheck_after_days`, since
    OpenAlex fills both gaps over time. A changed DOI (an in-place upgrade to the
    published version) always refetches.
    """
    cutoff = (now - timedelta(days=recheck_after_days)).isoformat()
    out = []
    for key, record in records.items():
        doi = normalize_doi(record.doi)
        if not doi or record.inactive:
            continue
        cached = cache["works"].get(key)
        if (
            cached is None
            or cached.get("doi") != doi
            or (not cached.get("referenced_works") and cached.get("fetched", "") < cutoff)
        ):
            out.append(key)
    return sorted(out)


def update_cache(
    cache: dict[str, Any],
    records: dict[str, supersede.Record],
    keys: list[str],
    fetched: dict[str, dict[str, Any]],
    now: datetime,
) -> None:
    """Record the lookup result for `keys`; a DOI OpenAlex lacks is kept as empty."""
    for key in keys:
        doi = normalize_doi(records[key].doi)
        hit = fetched.get(doi) or {}
        cache["works"][key] = {
            "doi": doi,
            "openalex_id": hit.get("openalex_id"),
            "referenced_works": sorted(set(hit.get("referenced_works") or [])),
            "fetched": now.isoformat(),
        }


# --- ranking ---------------------------------------------------------------


def rank(
    cache: dict[str, Any],
    sources: set[str],
    topics_by_key: dict[str, list[str]],
) -> list[dict[str, Any]]:
    """Outside works by how many `sources` notes cite them, most-cited first.

    A work that is itself a vault note (matched on OpenAlex id) is not a
    candidate. Each note counts once per work however often it cites it.
    """
    held = {
        entry["openalex_id"]
        for key, entry in cache["works"].items()
        if key in sources and entry.get("openalex_id")
    }
    cited_by: dict[str, list[str]] = {}
    for key in sorted(sources):
        refs = (cache["works"].get(key) or {}).get("referenced_works") or []
        for work_id in sorted(set(refs)):
            if work_id not in held:
                cited_by.setdefault(work_id, []).append(key)
    ranked = [
        {
            "openalex_ids": [work_id],
            "cited_by": keys,
            "count": len(keys),
            "topics": _topic_counts(keys, topics_by_key),
        }
        for work_id, keys in cited_by.items()
    ]
    ranked.sort(key=lambda c: (-c["count"], c["openalex_ids"][0]))
    return ranked


def _topic_counts(keys: list[str], topics_by_key: dict[str, list[str]]) -> dict[str, int]:
    counts = Counter(t for key in keys for t in topics_by_key.get(key, []))
    return dict(sorted(counts.items(), key=lambda kv: (-kv[1], kv[0])))


def _is_held(title: str, held_titles: list[str], threshold: float) -> bool:
    """Whether `title` matches a (pre-normalized) vault title.

    Same measure as `supersede.title_sim`, but with difflib's cheap upper bounds
    first: this runs for every candidate against every note.
    """
    norm = state_mod.normalize_title(title)
    if not norm:
        return False
    for held in held_titles:
        if norm == held:
            return True
        matcher = SequenceMatcher(None, norm, held)
        if (matcher.real_quick_ratio() >= threshold
                and matcher.quick_ratio() >= threshold
                and matcher.ratio() >= threshold):
            return True
    return False


def _surname(name: str) -> str:
    """`José van Dijck` -> `van Dijck`; `Nir Grinberg` -> `Grinberg`."""
    parts = name.split()
    if not parts:
        return ""
    start = len(parts) - 1
    while start > 1 and parts[start - 1].lower() in _PARTICLES:
        start -= 1
    return " ".join(parts[start:])


def _edition_key(meta: dict[str, Any]) -> tuple[str, str]:
    """Same title + same first-author surname = the same work in another edition."""
    title = _NON_ALNUM_RE.sub("", (meta.get("title") or "").lower())
    authors = meta.get("authors") or [""]
    surname = _NON_ALNUM_RE.sub("", _surname(authors[0]).lower())
    return title, surname


def build_report(
    ranked: list[dict[str, Any]],
    works: dict[str, dict[str, Any]],
    records: dict[str, supersede.Record],
    topics_by_key: dict[str, list[str]],
    exclude_types: Optional[set[str]] = None,
    exclude_dois: Optional[set[str]] = None,
    in_vault_title_sim: float = 0.9,
) -> list[dict[str, Any]]:
    """Annotate ranked works with metadata, merge editions, drop what is held.

    `works` is `{openalex short id: describe_candidate(...)}`; a ranked work with
    no metadata is dropped (it cannot be shown or acted on). Editions of one work
    — OpenAlex indexes a book's reprints separately — are merged and their citing
    notes unioned, which is why this re-sorts.
    """
    exclude_types = exclude_types or set()
    exclude_dois = {normalize_doi(d) for d in (exclude_dois or set())}
    held_dois = {normalize_doi(r.doi) for r in records.values() if r.doi}
    held_titles = [
        t for t in (state_mod.normalize_title(r.title) for r in records.values()) if t
    ]

    merged: dict[tuple[str, str], dict[str, Any]] = {}
    for cand in ranked:
        meta = works.get(cand["openalex_ids"][0])
        if not meta or not meta.get("title"):
            continue
        doi = normalize_doi(meta.get("doi"))
        if meta.get("type") in exclude_types or (doi and doi in exclude_dois):
            continue
        if doi and doi in held_dois:
            continue
        if _is_held(meta["title"], held_titles, in_vault_title_sim):
            continue
        edition = _edition_key(meta)
        if edition in merged:
            kept = merged[edition]
            kept["openalex_ids"] += cand["openalex_ids"]
            kept["cited_by"] = sorted(set(kept["cited_by"]) | set(cand["cited_by"]))
            continue
        merged[edition] = {**cand, **meta, "is_book": meta.get("type") in _BOOK_TYPES}

    report = list(merged.values())
    for cand in report:
        cand["count"] = len(cand["cited_by"])
        cand["topics"] = _topic_counts(cand["cited_by"], topics_by_key)
    report.sort(key=lambda c: (-c["count"], -(c.get("global_citations") or 0), c["title"]))
    return report


def by_topic(report: list[dict[str, Any]], per_topic: int = 5) -> dict[str, list[dict[str, Any]]]:
    """Per topic, the candidates most cited *by that topic's notes*.

    The overall ranking favours whichever topics have the best-indexed reference
    lists; this is the view that lets a thinly indexed topic still surface its
    own foundations.
    """
    topics = sorted({t for cand in report for t in cand["topics"]})
    out: dict[str, list[dict[str, Any]]] = {}
    for topic in topics:
        rows = [c for c in report if c["topics"].get(topic, 0) >= 2]
        rows.sort(key=lambda c: (-c["topics"][topic], -c["count"], c["title"]))
        if rows:
            out[topic] = rows[:per_topic]
    return out


# --- rendering -------------------------------------------------------------


def cite(cand: dict[str, Any]) -> str:
    """`Surname et al. (2019)` — enough to recognise the work in a list."""
    surnames = [_surname(a) for a in cand.get("authors") or [] if a]
    if not surnames:
        who = "Unknown"
    elif len(surnames) <= 3:
        who = ", ".join(surnames[:-1]) + (" & " if len(surnames) > 1 else "") + surnames[-1]
    else:
        who = f"{surnames[0]} et al."
    return f"{who} ({cand.get('year') or 'n.d.'})"


def render_markdown(
    report: list[dict[str, Any]],
    topic_view: dict[str, list[dict[str, Any]]],
    stats: dict[str, int],
    generated: str,
) -> str:
    lines = [
        "# Classics candidates",
        "",
        f"Generated {generated}. {stats['with_refs']} of {stats['sources']} notes with a DOI "
        f"have a reference list in OpenAlex ({stats['in_openalex']} are indexed at all), "
        f"citing {stats['distinct_works']} distinct outside works.",
        "",
        "Works are ranked by the number of vault notes citing them. 📕 marks a book — "
        "expect no full text. Add a chosen work through Paperpile so `toread` mints its key.",
        "",
        "## Most cited overall",
        "",
        "| Notes citing | Work | Venue | OA | Strongest topics |",
        "|---:|---|---|---|---|",
    ]
    for cand in report:
        lines.append(_row(cand, cand["count"]))
    lines += ["", "## By topic", ""]
    for topic, rows in topic_view.items():
        lines += [f"### {topic}", "", "| Notes citing (this topic) | Work | Venue | OA | Strongest topics |",
                  "|---:|---|---|---|---|"]
        lines += [_row(c, c["topics"][topic]) for c in rows]
        lines.append("")
    return "\n".join(lines).rstrip() + "\n"


def _row(cand: dict[str, Any], count: int) -> str:
    title = cand["title"].replace("|", "\\|")
    link = f"[{title}](https://doi.org/{cand['doi']})" if cand.get("doi") else title
    topics = ", ".join(f"{t} ({n})" for t, n in list(cand["topics"].items())[:2])
    book = "📕 " if cand.get("is_book") else ""
    return (f"| {count} | {book}{cite(cand)}. {link} | {cand.get('venue') or ''} "
            f"| {cand.get('oa_status') or ''} | {topics} |")


def now_utc() -> datetime:
    return datetime.now(timezone.utc)
