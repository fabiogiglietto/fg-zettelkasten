"""Fetch and parse the toread JSON Feed into `Paper` objects.

`Paper` is also the shape consumed by `drive_client` (ported from
research-radio): that code needs `.id`, `.title`, `.authors` (list[str]) and
`.date_published`.
"""
from __future__ import annotations

import html
import os
import re
from dataclasses import dataclass, field
from typing import Optional

import requests

from .feed_contract import validate_toread_feed

# The toread feed carries the journal name only inside the rendered
# `content_html` ("Published in: <name>"); the own-publications feed carries it
# in `_academic.venue`. This pulls it out of the toread HTML.
_PUBLISHED_IN_RE = re.compile(
    r"<strong>Published in:</strong>\s*(.*?)</li>", re.IGNORECASE
)


@dataclass
class Paper:
    """One paper from the toread feed. Join key across the pipeline is `id`."""

    id: str                                    # "bibtex:AuthorYear-xx"
    title: str
    authors: list[str] = field(default_factory=list)
    abstract: Optional[str] = None
    date_published: Optional[str] = None
    discovery_date: Optional[str] = None
    url: Optional[str] = None
    doi: Optional[str] = None
    tags: list[str] = field(default_factory=list)
    academic: dict = field(default_factory=dict)   # the feed's `_academic` block
    journal: Optional[str] = None                  # venue / journal name
    volume: Optional[str] = None
    pages: Optional[str] = None
    is_own: bool = False                           # True for own-publications papers
    submitted_by: Optional[str] = None             # team-mate who suggested it via Slack
    submitted_by_id: Optional[str] = None          # their opaque Slack user-id, for @-mentioning
    slack_permalink: Optional[str] = None          # link to the originating Slack message

    @property
    def is_team_submission(self) -> bool:
        """True for a paper that entered via a team-mate's Slack suggestion
        (the feed carries a `_slack_suggestion` block identifying the suggester
        by display name and/or opaque user-id). Either is enough — a submission
        whose display name failed to resolve still carries the user-id. Always
        False on the fg chain, whose feed strips suggester identity."""
        return bool(self.submitted_by or self.submitted_by_id)

    @property
    def bibtex_key(self) -> str:
        """`Boyd2026-pm` from `bibtex:Boyd2026-pm` — used as the note filename."""
        return self.id.split(":", 1)[-1]


def _extract_journal(item: dict, academic: dict) -> Optional[str]:
    """Journal/venue name: `_academic.venue` (own-pub feed) or the toread feed's
    `content_html` "Published in:" line. Returns None when neither carries it."""
    venue = academic.get("venue")
    if not venue:
        match = _PUBLISHED_IN_RE.search(item.get("content_html") or "")
        venue = match.group(1).strip() if match else None
    if not venue:
        return None
    # The feed double-escapes (`&amp;amp;`), so unescape twice to recover `&`.
    return html.unescape(html.unescape(venue)).strip() or None


def _item_to_paper(item: dict) -> Paper:
    academic = item.get("_academic", {}) or {}
    # The team (mine) chain adds `submitted_by` / `submitted_by_id` to the
    # `_slack_suggestion` block for team submissions; fg feeds omit them.
    slack = item.get("_slack_suggestion", {}) or {}
    return Paper(
        id=item["id"],
        title=item.get("title", ""),
        authors=[a.get("name", "") for a in item.get("authors", [])],
        abstract=item.get("content_text"),
        date_published=item.get("date_published"),
        discovery_date=item.get("_discovery_date"),
        url=item.get("url") or item.get("external_url"),
        doi=academic.get("doi"),
        tags=item.get("tags", []),
        academic=academic,
        journal=_extract_journal(item, academic),
        volume=academic.get("volume"),
        pages=academic.get("pages"),
        submitted_by=slack.get("submitted_by") or None,
        submitted_by_id=slack.get("submitted_by_id") or None,
        slack_permalink=slack.get("permalink") or None,
    )


def github_raw_headers() -> dict:
    """Headers for a GitHub Contents API request: ask for the raw file body,
    and authenticate when GITHUB_TOKEN is set (lifts the rate limit to 5000/h).

    The Contents API is served fresh, unlike raw.githubusercontent.com which
    is CDN-cached ~5 min — and `fetch_feed` runs seconds after toread commits
    the feed, so a cached read would miss brand-new papers.
    """
    headers = {"Accept": "application/vnd.github.raw+json"}
    token = os.getenv("GITHUB_TOKEN")
    if token:
        headers["Authorization"] = f"Bearer {token}"
    return headers


def fetch_feed(url: str, timeout: int = 30) -> list[Paper]:
    """Fetch the published JSON Feed and return its items as `Paper` objects.

    `url` is a GitHub Contents API URL (see `config.yml`)."""
    resp = requests.get(url, headers=github_raw_headers(), timeout=timeout)
    resp.raise_for_status()
    data = resp.json()
    # Contract gate: abort before any vault/state mutation on drift.
    validate_toread_feed(data)
    return [_item_to_paper(it) for it in data.get("items", [])]


def fetch_own_publications(url: str, timeout: int = 30) -> list[Paper]:
    """Fetch the own-publications JSON Feed -> `Paper` objects (is_own=True).

    Same JSON Feed 1.1 shape as the toread feed (so `_item_to_paper` is reused),
    published by fabiogiglietto.github.io. `url` is a raw.githubusercontent.com
    URL — the ~5-min CDN cache is harmless here, own papers change rarely.
    """
    resp = requests.get(url, timeout=timeout)
    resp.raise_for_status()
    data = resp.json()
    papers = []
    for item in data.get("items", []):
        paper = _item_to_paper(item)
        paper.is_own = True
        papers.append(paper)
    return papers


def is_note_eligible(paper: Paper, min_year: int, min_citations: int) -> bool:
    """Whether an own paper earns a vault note. Two gates, both required:

      1. a full-text PDF is available (`open_access_pdf_url`) — without it
         there is nothing substantial to summarise, so the paper is skipped;
      2. the paper is recent OR well-cited.

    Both checks are re-evaluated every run, so a paper joins automatically once
    its green-OA PDF is deposited or its citation count crosses the threshold.
    """
    academic = paper.academic or {}
    if not academic.get("open_access_pdf_url"):
        return False
    year = academic.get("year")
    citations = academic.get("citation_count") or 0
    if isinstance(year, int) and year >= min_year:
        return True
    return citations >= min_citations
