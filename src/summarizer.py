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


_SUMMARY_SYSTEM = """\
You are a research analyst writing a structured summary of an academic paper \
for a Zettelkasten knowledge base. The summary is a shared artifact: it must \
stand on its own as a faithful, transformative digest of the paper — never a \
verbatim copy.

Read the source carefully and return ONLY a JSON object, no prose or markdown \
fences, with these fields:
  "abstract"      : a 2-4 sentence plain-language overview of the paper.
  "key_claims"    : array of the paper's central claims or theses.
  "methods"       : array describing the methods, data, or approach used.
  "findings"      : array of the main empirical or analytical findings.
  "contributions" : array of what the paper contributes to its field.
  "framing"       : 1-3 sentences on the paper's theoretical or disciplinary
                    framing — the conversation it positions itself within.

Be specific and concrete: name methods, datasets, and figures where the source \
gives them. When working from an abstract only, summarise what is stated and \
do not invent detail."""


def summarize_paper(paper, pdf_text: Optional[str], claude, model: str) -> dict:
    """Produce a structured summary dict for one paper.

    `pdf_text` is None when no PDF was found -> abstract-only summary.
    Returns a dict with at least: key_claims, methods, findings,
    contributions, framing, pdf_source ("drive" | "abstract_only").
    See the implementation plan, section "Note generation".
    """
    pdf_source = "drive" if pdf_text else "abstract_only"

    header = [
        f"Title: {paper.title}",
        f"Authors: {', '.join(paper.authors) or 'unknown'}",
        f"Published: {paper.date_published or 'unknown'}",
    ]
    if pdf_text:
        body = f"Full extracted PDF text follows:\n\n{pdf_text}"
    else:
        body = (
            "No PDF was available — summarise from the abstract only:\n\n"
            f"{paper.abstract or '(no abstract provided)'}"
        )
    prompt = "\n".join(header) + "\n\n" + body

    summary = claude.complete_json(
        model=model,
        system=_SUMMARY_SYSTEM,
        prompt=prompt,
        max_tokens=4096,
    )
    summary["pdf_source"] = pdf_source
    return summary


def load_summary(summaries_dir: str, bibtex_key: str) -> Optional[dict]:
    p = Path(summaries_dir) / f"{bibtex_key}.json"
    return json.loads(p.read_text()) if p.exists() else None


def save_summary(summary: dict, summaries_dir: str, bibtex_key: str) -> None:
    d = Path(summaries_dir)
    d.mkdir(parents=True, exist_ok=True)
    (d / f"{bibtex_key}.json").write_text(
        json.dumps(summary, indent=2, ensure_ascii=False)
    )
