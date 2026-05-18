"""Fetch research-radio podcast episodes -> {paper id: audio URL}.

research-radio's episodes.json is keyed by the same `bibtex:` id the toread
feed uses, so this is a direct join — no normalisation needed.
"""
from __future__ import annotations

import requests

from .feed_client import github_raw_headers


def fetch_episode_audio(url: str, timeout: int = 30) -> dict[str, str]:
    """Return a mapping of paper id ("bibtex:...") -> podcast audio URL.

    `url` is a GitHub Contents API URL — see `feed_client.github_raw_headers`
    for why the API is used instead of raw.githubusercontent.com."""
    resp = requests.get(url, headers=github_raw_headers(), timeout=timeout)
    resp.raise_for_status()
    data = resp.json()
    episodes = data if isinstance(data, list) else data.get("episodes", [])
    out: dict[str, str] = {}
    for ep in episodes:
        ep_id = ep.get("id")
        audio = ep.get("audio_url") or ep.get("audioUrl")
        if ep_id and audio:
            out[ep_id] = audio
    return out
