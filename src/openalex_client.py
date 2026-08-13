"""Ask OpenAlex whether a preprint already in the vault has since been published.

The passive path in `supersede` only fires when someone re-adds a paper in its
published form. Plenty of working papers are published without anyone noticing,
so this closes the gap by asking an index directly.

OpenAlex over Crossref: one response carries the DOI, the year, the venue and a
`type` that distinguishes `preprint` from `article`, and the polite pool needs
only a `mailto` — no key, no quota negotiation. What it does *not* reliably give
is an explicit preprint -> published link: a work's `locations` normally lists
only the deposit you asked about (verified against real SocArXiv records), and
`related_works` is topical similarity, not versions. So matching is done by
title search plus the same author/title agreement the rest of the pipeline uses,
and every hit is adjudicated before anything is written.
"""
from __future__ import annotations

import re
from typing import Any, Optional

import requests

API = "https://api.openalex.org/works"
_SELECT = "id,doi,title,type,publication_year,primary_location,authorships"
# Filter values are comma-separated, so punctuation in a title has to go.
_TITLE_CLEAN_RE = re.compile(r"[^A-Za-z0-9 ]+")


def _clean_title(title: str, max_words: int = 18) -> str:
    words = _TITLE_CLEAN_RE.sub(" ", title or "").split()
    return " ".join(words[:max_words])


def _doi_of(work: dict) -> str:
    return re.sub(r"^https?://(?:dx\.)?doi\.org/", "", work.get("doi") or "", flags=re.I)


def _venue_of(work: dict) -> str:
    source = (work.get("primary_location") or {}).get("source") or {}
    return source.get("display_name") or ""


# A hit only counts as *publication* if it landed somewhere that publishes.
# OpenAlex's `source.type` draws that line cleanly where a DOI prefix cannot:
# checked against real hits, NBER working papers, Figshare deposits and
# conference-video platforms all come back as `repository` while the genuine
# journal versions come back as `journal`. Without this the scan would "upgrade"
# a SocArXiv preprint to a Figshare copy of itself.
_PUBLISHING_SOURCE_TYPES = {"journal", "conference", "book series"}
# Work types that represent a version of record. `report` covers working-paper
# series (NBER), `other`/`dataset` are not papers at all.
_PUBLISHED_WORK_TYPES = {"article", "book-chapter", "review", "book"}


def _is_published_venue(work: dict) -> bool:
    source = (work.get("primary_location") or {}).get("source") or {}
    return (
        (source.get("type") or "") in _PUBLISHING_SOURCE_TYPES
        and (work.get("type") or "") in _PUBLISHED_WORK_TYPES
        and bool(source.get("display_name"))
    )


def _authors_of(work: dict) -> list[str]:
    out = []
    for authorship in work.get("authorships") or []:
        name = (authorship.get("author") or {}).get("display_name")
        if name:
            out.append(name)
    return out


def as_record(work: dict):
    """An OpenAlex work as a `supersede.Record`, so it scores like any other."""
    from .supersede import Record

    return Record(
        key=f"openalex:{_doi_of(work) or work.get('id', '')}",
        title=work.get("title") or "",
        authors=_authors_of(work),
        doi=_doi_of(work) or None,
        journal=_venue_of(work) or None,
        year=str(work.get("publication_year") or ""),
    )


def search_by_title(
    title: str,
    mailto: Optional[str] = None,
    per_page: int = 5,
    timeout: int = 20,
) -> list[dict]:
    """Works whose title matches `title`. Returns [] on any transport failure.

    A lookup service must never break the vault build, so every error path here
    is a quiet empty result rather than an exception.
    """
    cleaned = _clean_title(title)
    if len(cleaned) < 12:
        return []
    params: dict[str, Any] = {
        "filter": f"title.search:{cleaned}",
        "per-page": per_page,
        "select": _SELECT,
    }
    if mailto:
        params["mailto"] = mailto
    try:
        response = requests.get(
            API, params=params, timeout=timeout,
            headers={"User-Agent": f"fg-zettelkasten (mailto:{mailto or 'unset'})"},
        )
    except requests.RequestException as exc:  # noqa: BLE001 - logged, non-fatal
        print(f"  openalex: request failed ({exc})")
        return []
    if response.status_code != 200:
        print(f"  openalex: HTTP {response.status_code} for {cleaned[:48]!r}")
        return []
    try:
        return response.json().get("results") or []
    except ValueError:
        return []


def find_published_version(
    record,
    mailto: Optional[str] = None,
    min_title_sim: float = 0.85,
) -> Optional[dict]:
    """The published counterpart of a preprint `record`, or None.

    Requires the hit to be genuinely more published than what we hold (the same
    `pub_rank` comparison the passive path uses), to carry a real venue, and to
    agree with the record on title and authorship. Returns the raw work dict so
    the caller can adjudicate it before writing anything.
    """
    from . import supersede

    best: Optional[tuple[float, dict]] = None
    for work in search_by_title(record.title, mailto=mailto):
        if not _is_published_venue(work):
            continue
        candidate = as_record(work)
        if candidate.rank <= record.rank:
            continue
        score = supersede.title_sim(record.title, candidate.title)
        if score < min_title_sim:
            continue
        if not supersede.authors_compatible(record.tokens, candidate.tokens):
            continue
        if best is None or score > best[0]:
            best = (score, work)
    return best[1] if best else None


def describe(work: dict) -> dict[str, str]:
    """The fields an in-place upgrade needs from a work."""
    return {
        "doi": _doi_of(work),
        "title": work.get("title") or "",
        "venue": _venue_of(work),
        "year": str(work.get("publication_year") or ""),
    }
