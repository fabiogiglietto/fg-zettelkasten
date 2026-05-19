"""Post a curated digest of a newly-added paper to Slack.

The `update` pipeline already summarises each new paper into a structured,
Claude-authored `summary` dict (see `summarizer.py`). This module wraps that
data in a Slack Block Kit message and posts it to an incoming webhook —
replacing the bare-link Paperpile bot in the team's #toread channel.

The webhook URL is a secret, read from the SLACK_WEBHOOK_URL env var by the
caller; it is never stored in config.yml.
"""
from __future__ import annotations

from typing import Optional

import requests

from .note_builder import _year_of

# Slack Block Kit limits.
_HEADER_MAX = 150       # plain_text header block
_SECTION_MAX = 3000     # mrkdwn section block text
_TEXT_MAX = 200         # top-level notification fallback text
_MAX_BULLETS = 20       # sanity bound only; _SECTION_MAX is the real backstop


def _truncate(text: str, limit: int) -> str:
    """Trim `text` to `limit` characters, appending an ellipsis when cut."""
    text = (text or "").strip()
    return text if len(text) <= limit else text[: limit - 1].rstrip() + "…"


def _esc(text: str) -> str:
    """Escape the three characters Slack mrkdwn treats specially."""
    return str(text).replace("&", "&amp;").replace("<", "&lt;").replace(">", "&gt;")


def _bullets(items: list, limit: int) -> str:
    """Render a list as escaped `• ` mrkdwn lines, capped at `limit` entries."""
    lines = [f"• {_esc(_truncate(str(it), 280))}" for it in items[:limit] if it]
    if len(items) > limit:
        lines.append(f"_…and {len(items) - limit} more_")
    return "\n".join(lines)


def _authors(authors: list) -> str:
    """Author byline, collapsing long lists to `A, B, C +N more`."""
    if not authors:
        return "Unknown authors"
    if len(authors) <= 3:
        return ", ".join(authors)
    return f"{', '.join(authors[:3])} +{len(authors) - 3} more"


def build_blocks(
    paper,
    summary: dict,
    topics: list[str],
    podcast_url: Optional[str],
    note_url: Optional[str] = None,
) -> list[dict]:
    """Assemble the Block Kit digest for one paper. Deterministic — no LLM."""
    blocks: list[dict] = [
        {
            "type": "header",
            "text": {
                "type": "plain_text",
                "text": _truncate(paper.title, _HEADER_MAX),
                "emoji": True,
            },
        }
    ]

    # Byline: authors · year · topics.
    meta = [_esc(_authors(paper.authors))]
    year = _year_of(paper)
    if year:
        meta.append(_esc(year))
    if topics:
        meta.append(" ".join(f"`{_esc(t)}`" for t in topics))
    blocks.append(
        {
            "type": "context",
            "elements": [{"type": "mrkdwn", "text": "  ·  ".join(meta)}],
        }
    )

    abstract = summary.get("abstract")
    if abstract:
        blocks.append(
            {
                "type": "section",
                "text": {
                    "type": "mrkdwn",
                    "text": _truncate(_esc(abstract), _SECTION_MAX),
                },
            }
        )

    for label, key in (("Key contributions", "contributions"), ("Findings", "findings")):
        items = summary.get(key) or []
        if items:
            body = f"*{label}*\n{_bullets(items, _MAX_BULLETS)}"
            blocks.append(
                {
                    "type": "section",
                    "text": {"type": "mrkdwn", "text": _truncate(body, _SECTION_MAX)},
                }
            )

    # Source links: paper + podcast episode. Rendered as plain mrkdwn links,
    # not Block Kit `button` elements: a URL button still emits a block_actions
    # interaction payload, and an incoming webhook has no Interactivity Request
    # URL to answer it — Slack then warns the user the app isn't configured for
    # interactive responses. Plain links carry no interaction and never warn.
    links = []
    if paper.url:
        links.append(f"📄 <{paper.url}|*Read paper*>")
    if note_url:
        links.append(f"📖 <{note_url}|*Full note*>")
    if podcast_url:
        links.append(f"🎧 <{podcast_url}|*Listen to the episode*>")
    if links:
        blocks.append(
            {
                "type": "section",
                "text": {"type": "mrkdwn", "text": "   ·   ".join(links)},
            }
        )

    blocks.append(
        {
            "type": "context",
            "elements": [{"type": "mrkdwn", "text": "Added to toread"}],
        }
    )
    return blocks


def post_paper(
    webhook_url: str,
    paper,
    summary: dict,
    topics: list[str],
    podcast_url: Optional[str],
    note_url: Optional[str] = None,
) -> bool:
    """Post one paper's digest to the Slack incoming webhook.

    Returns True on a 2xx response. Never raises: a Slack failure must not
    break the vault build, so transport errors are logged and reported as
    False, leaving the paper's `slack_posted` state flag unset for a retry.
    """
    payload = {
        # Top-level `text` is the notification / accessibility fallback Slack
        # shows when blocks can't render (push notifications, screen readers).
        "text": _truncate(paper.title, _TEXT_MAX),
        "blocks": build_blocks(paper, summary, topics, podcast_url, note_url),
    }
    try:
        resp = requests.post(webhook_url, json=payload, timeout=15)
    except requests.RequestException as exc:  # noqa: BLE001 - logged, non-fatal
        print(f"  slack: post failed for {paper.bibtex_key} ({exc})")
        return False
    if resp.status_code // 100 == 2:
        return True
    print(
        f"  slack: webhook returned {resp.status_code} for "
        f"{paper.bibtex_key}: {resp.text[:200]}"
    )
    return False
