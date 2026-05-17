"""Per-paper comprehension: full PDF text -> structured summary (Claude/Opus).

The structured summary is the *shared artifact* written to data/summaries/ — it
is what a future research-radio refactor will consume as a scaffold. The raw
PDF text is transient (cached in data/.cache/, gitignored) and never committed:
Paperpile publisher PDFs are not redistributable.
"""
from __future__ import annotations

import json
from pathlib import Path
from typing import Optional


def summarize_paper(paper, pdf_text: Optional[str], claude, model: str) -> dict:
    """Produce a structured summary dict for one paper.

    `pdf_text` is None when no PDF was found -> abstract-only summary.
    Returns a dict with at least: key_claims, methods, findings,
    contributions, framing, pdf_source ("drive" | "abstract_only").
    See the implementation plan, section "Note generation".
    """
    # TODO: build the summary prompt from pdf_text (or paper.abstract);
    #       call claude.complete_json(model=model, ...).
    raise NotImplementedError("summarizer.summarize_paper")


def load_summary(summaries_dir: str, bibtex_key: str) -> Optional[dict]:
    p = Path(summaries_dir) / f"{bibtex_key}.json"
    return json.loads(p.read_text()) if p.exists() else None


def save_summary(summary: dict, summaries_dir: str, bibtex_key: str) -> None:
    d = Path(summaries_dir)
    d.mkdir(parents=True, exist_ok=True)
    (d / f"{bibtex_key}.json").write_text(
        json.dumps(summary, indent=2, ensure_ascii=False)
    )
