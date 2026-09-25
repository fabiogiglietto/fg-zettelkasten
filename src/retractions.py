"""Ask Crossref whether a paper in the vault has been retracted or flagged.

Crossref records editorial notices on the *original* work as `updated-by`: each
entry names the notice's DOI, its `type` and its date. Since Crossref absorbed
the Retraction Watch database (2023) those entries include retractions the
publisher never deposited itself — Smith2025-kc's came from that source. One
batched `filter=doi:a,doi:b,...` query returns them for many works at once, so
a full scan of the vault is a handful of requests and needs no key, only a
polite-pool `mailto`.

Crossref only covers Crossref DOIs: arXiv / SocArXiv DataCite DOIs return
nothing, which is the honest answer — a withdrawn preprint is not tracked here.
"""
from __future__ import annotations

from typing import Any, Optional

import requests

API = "https://api.crossref.org/works"
# Crossref caps the filter length informally; 40 DOIs keep the URL well short.
_CHUNK = 40

# `updated-by` types that take a paper out of the live vault...
RETRACT_TYPES = {"retraction", "withdrawal", "removal"}
# ...and those that only flag it: the note says so, the paper stays in use.
FLAG_TYPES = {
    "expression_of_concern", "partial_retraction",
    "correction", "erratum", "corrigendum", "addendum",
}
# Human labels for the note callout and reports.
LABELS = {
    "retraction": "Retraction",
    "withdrawal": "Withdrawal",
    "removal": "Removal",
    "expression_of_concern": "Expression of concern",
    "partial_retraction": "Partial retraction",
    "correction": "Correction",
    "erratum": "Erratum",
    "corrigendum": "Corrigendum",
    "addendum": "Addendum",
}


def _date_of(update: dict) -> str:
    """`updated.date-parts` -> `YYYY-MM-DD` (month/day padded to 01 if absent)."""
    parts = ((update.get("updated") or {}).get("date-parts") or [[]])[0]
    if not parts:
        return ""
    y, m, d = (list(parts) + [1, 1])[:3]
    return f"{int(y):04d}-{int(m):02d}-{int(d):02d}"


def parse_updates(updated_by: Optional[list[dict]]) -> list[dict[str, str]]:
    """Normalize a work's `updated-by` list to the notices this module acts on.

    Returns `[{"type", "doi", "date", "source"}]`, sorted by date, keeping only
    the retraction and flag types — `new_version` and friends are not notices.
    The same notice is often listed twice (publisher + Retraction Watch, or a
    re-deposit with a new date); it is kept once, at its earliest date.
    """
    seen: dict[tuple[str, str], dict[str, str]] = {}
    for u in updated_by or []:
        kind = str(u.get("type") or "").lower()
        if kind not in RETRACT_TYPES and kind not in FLAG_TYPES:
            continue
        notice = {
            "type": kind,
            "doi": str(u.get("DOI") or "").lower(),
            "date": _date_of(u),
            "source": str(u.get("source") or ""),
        }
        key = (kind, notice["doi"])
        if key not in seen or (notice["date"] and notice["date"] < seen[key]["date"]):
            seen[key] = notice
    return sorted(seen.values(), key=lambda n: (n["date"], n["doi"]))


def retraction_of(notices: list[dict[str, str]]) -> Optional[dict[str, str]]:
    """The earliest notice that retracts the work, or None."""
    return next((n for n in notices if n["type"] in RETRACT_TYPES), None)


def flags_of(notices: list[dict[str, str]]) -> list[dict[str, str]]:
    """The notices that flag, but do not retract, the work."""
    return [n for n in notices if n["type"] in FLAG_TYPES]


def fetch_updates(
    dois: list[str], mailto: Optional[str] = None
) -> dict[str, list[dict[str, str]]]:
    """`{doi: notices}` for every DOI Crossref holds a notice for.

    DOIs are compared lowercased. A failed batch is logged and skipped, so a
    transient outage costs one run's coverage of those DOIs, never a crash.
    """
    from urllib.parse import urlencode

    from .feed_client import get_with_retries

    wanted = sorted({d.lower() for d in dois if d})
    out: dict[str, list[dict[str, str]]] = {}
    for i in range(0, len(wanted), _CHUNK):
        chunk = wanted[i:i + _CHUNK]
        params: dict[str, Any] = {
            "filter": ",".join(f"doi:{d}" for d in chunk),
            "rows": len(chunk),
            "select": "DOI,updated-by",
        }
        if mailto:
            params["mailto"] = mailto
        try:
            response = get_with_retries(
                f"{API}?{urlencode(params)}",
                headers={"User-Agent": f"fg-zettelkasten (mailto:{mailto or 'unset'})"},
                timeout=60,
            )
            items = (response.json().get("message") or {}).get("items") or []
        except (requests.RequestException, ValueError) as exc:
            print(f"  crossref: batch failed ({exc})")
            continue
        for item in items:
            notices = parse_updates(item.get("updated-by"))
            if notices:
                out[str(item.get("DOI") or "").lower()] = notices
    return out
