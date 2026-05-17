"""Load/save data/state.json — per-paper processing state.

Schema (see the implementation plan):

    {
      "papers": {
        "bibtex:Boyd2026-pm": {
          "note_path": "Papers/Boyd2026-pm.md",
          "topics": ["information-disorder"],
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
