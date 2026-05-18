"""Fetch and parse the toread JSON Feed into `Paper` objects.

`Paper` is also the shape consumed by `drive_client` (ported from
research-radio): that code needs `.id`, `.title`, `.authors` (list[str]) and
`.date_published`.
"""
from __future__ import annotations

import os
from dataclasses import dataclass, field
from typing import Optional

import requests


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

    @property
    def bibtex_key(self) -> str:
        """`Boyd2026-pm` from `bibtex:Boyd2026-pm` — used as the note filename."""
        return self.id.split(":", 1)[-1]


def _item_to_paper(item: dict) -> Paper:
    academic = item.get("_academic", {}) or {}
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
    return [_item_to_paper(it) for it in data.get("items", [])]
