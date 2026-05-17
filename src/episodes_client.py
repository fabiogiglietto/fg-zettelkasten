"""Fetch research-radio podcast episodes -> {paper id: audio URL}.

research-radio's episodes.json is keyed by the same `bibtex:` id the toread
feed uses, so this is a direct join — no normalisation needed.
"""
from __future__ import annotations

import requests


def fetch_episode_audio(url: str, timeout: int = 30) -> dict[str, str]:
    """Return a mapping of paper id ("bibtex:...") -> podcast audio URL."""
    resp = requests.get(url, timeout=timeout)
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
