"""Load/save data/state.json — per-paper processing state.

Schema (see the implementation plan):

    {
      "papers": {
        "bibtex:Boyd2026-pm": {
          "note_path": "Papers/Boyd2026-pm.md",
          "topics": ["information-disorder"],
          "doi": "10.xxxx/...",        # for duplicate detection (dedup_index)
          "title": "...",              # for duplicate detection (dedup_index)
          "kind": "own" | "team",      # optional: source marker
          "submitted_by": "...",       # optional: team-submission attribution
          "pdf_source": "drive" | "abstract_only",
          "content_hash": "<sha256>",
          "podcast_linked": true,
          "last_processed": "2026-05-17T..."
        }
      },
      "last_full_cluster": "2026-05-17T...",
      "papers_since_cluster": 0
    }
"""
from __future__ import annotations

import hashlib
import json
import re
import unicodedata
from pathlib import Path
from typing import Any


def load_state(path: str) -> dict[str, Any]:
    p = Path(path)
    if not p.exists():
        return {"papers": {}, "last_full_cluster": None, "papers_since_cluster": 0}
    return json.loads(p.read_text())


def save_state(state: dict[str, Any], path: str) -> None:
    p = Path(path)
    p.parent.mkdir(parents=True, exist_ok=True)
    p.write_text(json.dumps(state, indent=2, ensure_ascii=False))


def content_hash(source_text: str | None, podcast_linked: bool) -> str:
    """Hash over the paper's source text + podcast flag.

    Lets `update` detect when a note must be regenerated (e.g. a podcast
    episode became available) rather than only handling brand-new ids.
    """
    h = hashlib.sha256()
    h.update((source_text or "").encode("utf-8"))
    h.update(b"\x00podcast" if podcast_linked else b"\x00")
    return h.hexdigest()


# --- Duplicate detection ---------------------------------------------------
# In a multi-user archive two different bibtex ids can refer to the same paper
# (e.g. a team-mate's Slack submission of a paper Fabio already curates). These
# normalizers + index let `update` skip a new id whose DOI or title already has
# a note. The same normalization is mirrored upstream in team-toread's
# slack_ingest so the in-Slack "already in the archive" reply and this
# downstream safety net agree on what counts as a duplicate.

_DOI_PREFIX_RE = re.compile(r"^(?:https?://)?(?:dx\.)?doi\.org/", re.IGNORECASE)
_TITLE_STRIP_RE = re.compile(r"[^a-z0-9\s]")
_WS_RE = re.compile(r"\s+")


def normalize_doi(doi: str | None) -> str | None:
    """Lowercased bare DOI (`10.xxxx/…`), or None. Strips a doi.org prefix."""
    if not doi:
        return None
    d = _DOI_PREFIX_RE.sub("", doi.strip()).lower().rstrip(".")
    return d or None


def normalize_title(title: str | None) -> str | None:
    """Title reduced to lowercase, accent-folded, punctuation-stripped,
    whitespace-collapsed — a coarse key for matching the same paper across
    sources. Returns None for an empty/too-short title (no reliable signal)."""
    if not title:
        return None
    folded = unicodedata.normalize("NFKD", title)
    folded = folded.encode("ascii", "ignore").decode("ascii").lower()
    folded = _WS_RE.sub(" ", _TITLE_STRIP_RE.sub(" ", folded)).strip()
    return folded if len(folded) >= 8 else None


def dedup_index(state: dict[str, Any]) -> dict[str, str]:
    """Map `doi:<norm>` / `title:<norm>` -> bibtex id for existing notes.

    Built from the per-paper entries already in `state`; each entry stores its
    own `doi`/`title` (added when the note is created) so the index does not
    need the live feed. Used to detect a new paper that duplicates one already
    in the vault.

    Entries created before the `doi`/`title` fields existed (e.g. the seeded
    corpus a team fork starts from) contribute nothing here — pair this with
    `dedup_index_from_notes` to also cover them.
    """
    index: dict[str, str] = {}
    for pid, entry in state.get("papers", {}).items():
        nd = normalize_doi(entry.get("doi"))
        if nd:
            index.setdefault(f"doi:{nd}", pid)
        nt = normalize_title(entry.get("title"))
        if nt:
            index.setdefault(f"title:{nt}", pid)
    return index


_FRONTMATTER_RE = re.compile(r"\A---\n(.*?)\n---\n", re.DOTALL)


def dedup_index_from_notes(papers_dir: str | Path) -> dict[str, str]:
    """Dedup index built from vault note frontmatter (`doi`/`title` -> id).

    Every Papers/<key>.md carries `doi`, `title` and `bibtex_key` in its
    frontmatter (see note_builder), so this covers the *seeded* corpus a team
    fork starts from — whose `state.json` entries predate the per-entry
    `doi`/`title` fields. Merge it under `dedup_index(state)` so a team-mate's
    Slack submission of an already-archived paper is caught at launch, not only
    for papers added after the fork. Self-healing: no state migration needed.
    """
    import yaml  # local import: PyYAML is already a dependency (site_export)

    index: dict[str, str] = {}
    p = Path(papers_dir)
    if not p.is_dir():
        return index
    for note in sorted(p.glob("*.md")):
        try:
            m = _FRONTMATTER_RE.match(note.read_text(encoding="utf-8"))
            fm = yaml.safe_load(m.group(1)) if m else None
        except Exception:
            continue
        if not isinstance(fm, dict):
            continue
        key = str(fm.get("bibtex_key") or note.stem)
        pid = key if key.startswith("bibtex:") else f"bibtex:{key}"
        nd = normalize_doi(str(fm.get("doi") or "") or None)
        if nd:
            index.setdefault(f"doi:{nd}", pid)
        nt = normalize_title(fm.get("title"))
        if nt:
            index.setdefault(f"title:{nt}", pid)
    return index


def find_duplicate(index: dict[str, str], doi: str | None,
                   title: str | None) -> str | None:
    """Return the existing bibtex id that `doi`/`title` duplicates, or None.
    DOI match wins over title match."""
    nd = normalize_doi(doi)
    if nd and f"doi:{nd}" in index:
        return index[f"doi:{nd}"]
    nt = normalize_title(title)
    if nt and f"title:{nt}" in index:
        return index[f"title:{nt}"]
    return None
