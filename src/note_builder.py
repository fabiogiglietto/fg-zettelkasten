"""Render Obsidian markdown: paper notes, topic register notes, structure notes.

Paper notes and structure/hub notes are LLM-written (Claude). Topic register
notes are deterministic templating from state + the topic register — no LLM.
"""
from __future__ import annotations

import re
from pathlib import Path
from typing import Any, Optional


def _yaml_quote(text: str) -> str:
    """Double-quote a string for safe YAML frontmatter (titles carry colons)."""
    escaped = str(text).replace("\\", "\\\\").replace('"', '\\"')
    return f'"{escaped}"'


def _year_of(paper) -> str:
    """Best-effort publication year from the feed date or the bibtex key."""
    for source in (paper.date_published, paper.id):
        if source:
            match = re.search(r"(19|20)\d{2}", source)
            if match:
                return match.group(0)
    return ""


def render_frontmatter(fields: dict[str, Any]) -> str:
    """Render a YAML frontmatter block. Lists become `[a, b]`."""
    lines = ["---"]
    for key, val in fields.items():
        if isinstance(val, list):
            lines.append(f"{key}: [{', '.join(str(v) for v in val)}]")
        elif isinstance(val, bool):
            lines.append(f"{key}: {str(val).lower()}")
        elif val is None:
            lines.append(f"{key}:")
        else:
            lines.append(f"{key}: {val}")
    lines.append("---")
    return "\n".join(lines)


def build_topic_note(topic: dict, member_keys: list[str]) -> str:
    """Deterministically render a Topics/<slug>.md register entry note.

    A thin entry point (Luhmann *Schlagwortregister*): description + links into
    the paper web + a Dataview list. Regenerated every run; never appended to.
    """
    fm = render_frontmatter(
        {
            "type": "topic",
            "slug": topic["slug"],
            "emergent": topic.get("is_emergent", False),
        }
    )
    links = "\n".join(f"- [[{k}]]" for k in sorted(member_keys)) or "_No papers yet._"
    return f"""{fm}

# {topic['name']}

{topic.get('description', '')}

## Papers

{links}

## All papers (Dataview)

```dataview
LIST FROM "Papers"
WHERE contains(topics, "{topic['slug']}")
SORT discovery_date DESC
```
"""


_PAPER_BODY_SYSTEM = """\
You write the body of an Obsidian Zettelkasten note for a single academic \
paper, working only from the structured summary you are given. The note is a \
faithful, transformative digest — never a verbatim copy of the source.

Write GitHub-flavoured Markdown, starting at a level-2 heading (the note title \
is already set in frontmatter — do not repeat it). Include these sections:

## Summary        — a tight paragraph on what the paper is and argues.
## Key Contributions — bullet points.
## Methods        — a short paragraph or bullets.
## Findings       — bullet points.
## Connections    — 1-3 sentences placing this paper in the wider web. You are
                    given the bibtex keys of other papers under the same
                    topic(s); link the genuinely related ones inline as
                    [[bibtex-key]] wikilinks. Link only real intellectual
                    connections — if none are related, say so plainly.

Do not add frontmatter, a title heading, or a Podcast section — those are \
added by the caller. Output only the Markdown body."""


def build_paper_note(
    paper,
    summary: dict,
    topics: list[str],
    related_keys: list[str],
    podcast_url: Optional[str],
    claude,
    model: str,
) -> str:
    """Render a Papers/<bibtex-key>.md note (LLM-assisted).

    Claude writes the body — summary, contributions, methods, findings, a
    "Connections" section with inline [[bibtex-key]] links to `related_keys`,
    and a "Podcast" section when `podcast_url` is set. Filename is the bibtex
    key; the readable title goes in frontmatter `aliases`.
    """
    academic = paper.academic or {}
    fm = render_frontmatter(
        {
            "title": _yaml_quote(paper.title),
            "aliases": [_yaml_quote(paper.title)],
            "authors": [_yaml_quote(a) for a in paper.authors],
            "year": _year_of(paper),
            "doi": paper.doi or "",
            "bibtex_key": paper.bibtex_key,
            "topics": topics,
            "citation_count": academic.get("citation_count", 0),
            "open_access": bool(academic.get("open_access", False)),
            "source_url": paper.url or "",
            "podcast_url": podcast_url or "",
            "pdf_available": summary.get("pdf_source") == "drive",
            "discovery_date": paper.discovery_date or "",
        }
    )

    summary_json = "\n".join(
        f"{k}: {v}" for k, v in summary.items() if k != "pdf_source"
    )
    related = ", ".join(related_keys) if related_keys else "(none)"
    topic_list = ", ".join(topics) if topics else "(unassigned)"
    prompt = (
        f"Paper title: {paper.title}\n"
        f"Authors: {', '.join(paper.authors) or 'unknown'}\n"
        f"Register topics: {topic_list}\n"
        f"Other papers under these topics (bibtex keys): {related}\n\n"
        f"Structured summary:\n{summary_json}"
    )

    body = claude.complete(
        model=model,
        system=_PAPER_BODY_SYSTEM,
        prompt=prompt,
        max_tokens=4096,
    ).strip()

    note = f"{fm}\n\n# {paper.title}\n\n{body}\n"
    if podcast_url:
        note += (
            f"\n## Podcast\n\n"
            f"A research-radio episode discusses this paper: "
            f"[Listen]({podcast_url})\n"
        )
    return note


_STRUCTURE_SYSTEM = """\
You write a Structure note — a hub note in a Niklas-Luhmann-style Zettelkasten. \
A structure note narrates the *line of argument* running across a set of papers \
filed under one topic: how they speak to each other, where they agree and \
diverge, what arc of inquiry they trace. It is a synthesis, not a list of \
abstracts.

Write GitHub-flavoured Markdown, starting at a level-2 heading (the topic title \
is already set in frontmatter — do not repeat it). Reference papers inline as \
[[bibtex-key]] wikilinks, using the keys given to you. Aim for several tight \
paragraphs under a few thematic headings. Output only the Markdown body — no \
frontmatter, no title heading."""


def build_structure_note(topic: dict, papers: list, summaries: dict, claude, model: str) -> str:
    """Render a Structures/<slug>.md hub note — a Claude-written narrative across
    the papers in a topic. Regenerated only on bootstrap/recluster."""
    fm = render_frontmatter(
        {
            "type": "structure",
            "slug": topic["slug"],
            "topic": _yaml_quote(topic["name"]),
        }
    )

    blocks = []
    for paper in papers:
        digest_summary = summaries.get(paper.bibtex_key, {})
        bits = [f"===== {paper.bibtex_key} =====", f"Title: {paper.title}"]
        for field in ("abstract", "key_claims", "findings", "framing"):
            value = digest_summary.get(field)
            if not value:
                continue
            if isinstance(value, list):
                value = "; ".join(str(v) for v in value)
            bits.append(f"{field}: {value}")
        blocks.append("\n".join(bits))

    prompt = (
        f"Topic: {topic['name']}\n"
        f"Topic description: {topic.get('description', '')}\n\n"
        f"The {len(papers)} papers filed under this topic follow.\n\n"
        + "\n\n".join(blocks)
    )

    body = claude.complete(
        model=model,
        system=_STRUCTURE_SYSTEM,
        prompt=prompt,
        max_tokens=8192,
    ).strip()

    return f"{fm}\n\n# {topic['name']}\n\n{body}\n"


def write_note(vault_dir: str, subdir: str, filename: str, content: str) -> Path:
    """Write `content` to vault_dir/subdir/filename.md and return the path."""
    path = Path(vault_dir) / subdir / f"{filename}.md"
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(content, encoding="utf-8")
    return path
