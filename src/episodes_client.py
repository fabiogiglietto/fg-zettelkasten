"""Fetch research-radio podcast episodes -> {paper id: episode record}.

research-radio's episodes.json is keyed by the same `bibtex:` id the toread
feed uses, so this is a direct join — no normalisation needed.
"""
from __future__ import annotations

from .feed_client import get_with_retries, github_raw_headers


def fetch_episodes(url: str, timeout: int = 30) -> dict[str, dict]:
    """Return a mapping of paper id ("bibtex:...") -> an episode record.

    Each record is a dict with `audio_url` (the standalone MP3), the optional
    per-episode `spotify_url` / `apple_url` platform links (None until
    research-radio publishes them), and the `own` flag. Only episodes that
    carry an `audio_url` are included.

    Episodes flagged `audio_mismatch` by research-radio carry the wrong paper's
    audio (a wrong-PDF generation bug) and are withheld from its public feed;
    they are skipped here too, so the wrong audio is never linked from a note.

    `url` is a GitHub Contents API URL — see `feed_client.github_raw_headers`
    for why the API is used instead of raw.githubusercontent.com."""
    resp = get_with_retries(url, headers=github_raw_headers(), timeout=timeout)
    data = resp.json()
    episodes = data if isinstance(data, list) else data.get("episodes", [])
    out: dict[str, dict] = {}
    for ep in episodes:
        if ep.get("audio_mismatch"):
            continue
        ep_id = ep.get("id")
        audio = ep.get("audio_url") or ep.get("audioUrl")
        if ep_id and audio:
            out[ep_id] = {
                "audio_url": audio,
                "spotify_url": ep.get("spotify_url"),
                "apple_url": ep.get("apple_url"),
                "own": bool(ep.get("own", False)),
            }
    return out
