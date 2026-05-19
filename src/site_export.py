"""Export the Obsidian vault to a Quartz `content/` tree for the public website.

`export-site` is a deterministic, no-LLM stage. It copies the committed vault
notes into `quartz/content/`, strips the ```dataview``` blocks that only render
inside Obsidian, and generates a `content/index.md` homepage from the topic
register and processing state. The vault itself is never modified — Obsidian
keeps working unchanged.

Topic and Structure notes share a slug basename (e.g. `Topics/information-disorder`
and `Structures/information-disorder`), so the generated homepage links them with
explicit folder paths rather than bare basenames.
"""
from __future__ import annotations

import re
import shutil
from pathlib import Path

# ```dataview``` fenced blocks render only inside Obsidian; Quartz would print
# them verbatim. The closing fence is anchored to start-of-line so a stray
# triple-backtick inside the block cannot end the match early.
_DATAVIEW_BLOCK = re.compile(
    r"^```dataview[ \t]*\n.*?^```[ \t]*\n?", re.DOTALL | re.MULTILINE
)
# The heading that introduces the block (e.g. "## All papers (Dataview)").
_DATAVIEW_HEADING = re.compile(
    r"^#{1,6} [^\n]*[Dd]ataview[^\n]*\n?", re.MULTILINE
)


def strip_dataview(text: str) -> str:
    """Remove ```dataview``` fenced blocks and their headings from a note body."""
    text = _DATAVIEW_BLOCK.sub("", text)
    text = _DATAVIEW_HEADING.sub("", text)
    return re.sub(r"\n{3,}", "\n\n", text)


# Quartz's ContentMeta dates a note from a `date` frontmatter key (falling back
# to git/filesystem mtime — which is the build time for freshly exported,
# untracked content). Paper notes carry `year` but no `date`, so without this
# every page would show the build date. Topic/Structure notes have neither and
# keep the (acceptable) build date.
_FRONTMATTER = re.compile(r"\A---\n(.*?)\n---\n", re.DOTALL)
_YEAR = re.compile(r"^year:[ \t]*(\d{4})[ \t]*$", re.MULTILINE)
_HAS_DATE = re.compile(r"^date:", re.MULTILINE)


def inject_date(text: str) -> str:
    """Add a `date: <year>-01-01` frontmatter key to a note that has `year`.

    No-op when the note lacks a `year` field or already has a `date` key.
    """
    fm = _FRONTMATTER.match(text)
    if not fm:
        return text
    block = fm.group(1)
    if _HAS_DATE.search(block):
        return text
    year = _YEAR.search(block)
    if not year:
        return text
    return f"---\ndate: {year.group(1)}-01-01\n{block}\n---\n{text[fm.end():]}"


def topic_paper_counts(state: dict) -> dict[str, int]:
    """Map each topic slug to the number of papers assigned to it."""
    counts: dict[str, int] = {}
    for entry in state.get("papers", {}).values():
        for slug in entry.get("topics", []):
            counts[slug] = counts.get(slug, 0) + 1
    return counts


def _plural(n: int, word: str) -> str:
    return f"{n} {word}" if n == 1 else f"{n} {word}s"


def build_index(
    topics: list[dict],
    state: dict,
    structure_slugs: set[str],
    topics_dir: str,
    structures_dir: str,
) -> str:
    """Render `content/index.md`: a homepage listing Topics and Structures.

    Links use explicit `[[<dir>/<slug>|Name]]` paths because Topic and
    Structure notes collide on basename.
    """
    counts = topic_paper_counts(state)
    by_slug = {t["slug"]: t for t in topics}
    total_papers = len(state.get("papers", {}))

    lines = [
        "---",
        'title: "fg-zettelkasten"',
        "---",
        "",
        "# fg-zettelkasten",
        "",
        f"A topic-anchored Zettelkasten built from the `toread` paper feed — "
        f"{_plural(total_papers, 'paper')} across {_plural(len(topics), 'topic')}. "
        "Use the graph, backlinks, and search to explore; the entry points below "
        "group the archive by theme.",
        "",
        "## Topics",
        "",
        "Thematic registers — each lists every paper assigned to it.",
        "",
    ]
    for topic in topics:
        slug = topic["slug"]
        name = topic.get("name", slug)
        count = counts.get(slug, 0)
        desc = topic.get("description", "").strip()
        line = f"- [[{topics_dir}/{slug}|{name}]] ({_plural(count, 'paper')})"
        if desc:
            line += f" — {desc}"
        lines.append(line)

    lines += [
        "",
        "## Structures",
        "",
        "Curated narratives tracing a line of argument across the papers in a topic.",
        "",
    ]
    for slug in sorted(structure_slugs):
        name = by_slug.get(slug, {}).get("name", slug)
        lines.append(f"- [[{structures_dir}/{slug}|{name}]]")

    return "\n".join(lines) + "\n"


def export_site(
    vault_dir: Path,
    content_dir: Path,
    subdirs: list[str],
    topics: list[dict],
    state: dict,
) -> dict:
    """Populate `content_dir` from the vault and write the homepage.

    Wipes and rebuilds `content_dir`, walking only the named `subdirs` so that
    `.obsidian/` and other non-note files cannot leak into the site. Returns a
    stats dict: `{"notes": int, "stripped": int}`.
    """
    papers_dir, topics_dir, structures_dir = subdirs

    shutil.rmtree(content_dir, ignore_errors=True)
    content_dir.mkdir(parents=True, exist_ok=True)

    notes = 0
    stripped = 0
    for subdir in subdirs:
        src = vault_dir / subdir
        if not src.is_dir():
            continue
        dst = content_dir / subdir
        dst.mkdir(parents=True, exist_ok=True)
        for note in sorted(src.glob("*.md")):
            text = note.read_text(encoding="utf-8")
            cleaned = strip_dataview(text)
            if cleaned != text:
                stripped += 1
            (dst / note.name).write_text(inject_date(cleaned), encoding="utf-8")
            notes += 1

    structure_slugs = {
        p.stem for p in (vault_dir / structures_dir).glob("*.md")
    }
    index = build_index(topics, state, structure_slugs, topics_dir, structures_dir)
    (content_dir / "index.md").write_text(index, encoding="utf-8")

    return {"notes": notes, "stripped": stripped}
