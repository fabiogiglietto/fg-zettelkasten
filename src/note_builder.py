"""Render Obsidian markdown: paper notes, topic register notes, structure notes.

Paper notes and structure/hub notes are LLM-written (Claude). Topic register
notes are deterministic templating from state + the topic register — no LLM.
"""
from __future__ import annotations

from pathlib import Path
from typing import Any, Optional


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
    # TODO: assemble frontmatter via render_frontmatter() + Claude-written body.
    raise NotImplementedError("note_builder.build_paper_note")


def build_structure_note(topic: dict, papers: list, summaries: dict, claude, model: str) -> str:
    """Render a Structures/<slug>.md hub note — a Claude-written narrative across
    the papers in a topic. Regenerated only on bootstrap/recluster."""
    # TODO: Claude narrative synthesis across the topic's papers.
    raise NotImplementedError("note_builder.build_structure_note")


def write_note(vault_dir: str, subdir: str, filename: str, content: str) -> Path:
    """Write `content` to vault_dir/subdir/filename.md and return the path."""
    path = Path(vault_dir) / subdir / f"{filename}.md"
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(content, encoding="utf-8")
    return path
