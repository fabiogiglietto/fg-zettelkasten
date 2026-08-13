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

import json
import re
import shutil
from pathlib import Path

import yaml

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
# untracked content). Paper notes carry `discovery_date` (when the paper entered
# the feed) and `year`, but no `date`, so without this every page would show the
# build date. We prefer `discovery_date` for a real per-paper date and fall back
# to `<year>-01-01` only when it is missing. Topic/Structure notes have neither
# and keep the (acceptable) build date.
_FRONTMATTER = re.compile(r"\A---\n(.*?)\n---\n", re.DOTALL)
_YEAR = re.compile(r"^year:[ \t]*(\d{4})[ \t]*$", re.MULTILINE)
_DISCOVERY = re.compile(r"^discovery_date:[ \t]*(\S+)[ \t]*$", re.MULTILINE)
_HAS_DATE = re.compile(r"^date:", re.MULTILINE)
_HAS_TITLE = re.compile(r"^title:", re.MULTILINE)


def inject_date(text: str) -> str:
    """Add a `date` frontmatter key derived from `discovery_date` (preferred) or
    `<year>-01-01` (fallback).

    No-op when the note already has a `date` key or carries neither
    `discovery_date` nor `year`.
    """
    fm = _FRONTMATTER.match(text)
    if not fm:
        return text
    block = fm.group(1)
    if _HAS_DATE.search(block):
        return text
    discovery = _DISCOVERY.search(block)
    if discovery:
        date = discovery.group(1)[:10]  # YYYY-MM-DD from the ISO timestamp
    else:
        year = _YEAR.search(block)
        if not year:
            return text
        date = f"{year.group(1)}-01-01"
    return f"---\ndate: {date}\n{block}\n---\n{text[fm.end():]}"


_BODY_H1 = re.compile(r"^# (.+?)[ \t]*$", re.MULTILINE)


def strip_duplicate_title(text: str) -> str:
    """Drop the body's leading `# Title` H1 when it duplicates the frontmatter
    `title`. Quartz renders `title` as the page H1, so the body heading would
    show the title a second time. No-op for notes without a `title` frontmatter
    (Topic/Structure notes) or whose first H1 differs from it.
    """
    fm = _FRONTMATTER.match(text)
    if not fm:
        return text
    data = yaml.safe_load(fm.group(1)) or {}
    title = data.get("title")
    if not title:
        return text
    body_start = fm.end()
    match = _BODY_H1.search(text, body_start)
    if not match or match.group(1).strip() != str(title).strip():
        return text
    # Remove the H1 line and the blank line that follows it.
    end = match.end()
    if text[end:end + 2] == "\n\n":
        end += 1
    return text[:match.start()] + text[end:].lstrip("\n")


def inject_title(text: str, suffix: str = "") -> str:
    """Promote the body's leading `# H1` to a frontmatter `title` (plus
    `suffix`) and drop the H1 line.

    Topic and Structure notes carry no `title`, so Quartz falls back to the
    file stem — and because the two kinds share a slug basename, the graph
    shows every topic as two identically-labelled nodes. The suffix keeps the
    pair distinguishable (" (Structure)"). No-op when the note already has a
    `title` or no body H1.
    """
    fm = _FRONTMATTER.match(text)
    if not fm:
        return text
    block = fm.group(1)
    if _HAS_TITLE.search(block):
        return text
    match = _BODY_H1.search(text, fm.end())
    if not match:
        return text
    title = json.dumps(match.group(1).strip() + suffix)
    end = match.end()
    if text[end:end + 2] == "\n\n":
        end += 1
    body = text[fm.end():match.start()] + text[end:].lstrip("\n")
    return f"---\ntitle: {title}\n{block}\n---\n{body}"


def inject_contributor(text: str) -> str:
    """Append a "Suggested by <name>" footer when the note carries a
    `submitted_by` frontmatter (a team-mate's Slack submission).

    A website-only presentation detail: the attribution already lives in the
    vault frontmatter, and this surfaces it at the bottom of the page. No-op for
    own publications and plain toread papers, which have no `submitted_by`.
    Runs last, on the already-cleaned body, so the footer sits below any
    `## Podcast` section. The Slack permalink is deliberately not linked — it
    points to a private workspace, useless to public visitors.
    """
    fm = _FRONTMATTER.match(text)
    if not fm:
        return text
    data = yaml.safe_load(fm.group(1)) or {}
    contributor = data.get("submitted_by")
    if not contributor:
        return text
    return f"{text.rstrip()}\n\n---\n\n*Suggested by {contributor}*\n"


def _read_paper_meta(text: str) -> dict | None:
    """Extract the fields needed for the homepage 'Latest papers' list.

    Returns None for notes without a parseable frontmatter or without a
    `discovery_date` — those can't be ranked by recency — and for superseded
    notes, which are redirect stubs: they keep their original discovery date so
    the tombstone stays a faithful record, which would otherwise let a
    just-superseded paper occupy a "Latest papers" slot with an empty page.
    """
    fm = _FRONTMATTER.match(text)
    if not fm:
        return None
    data = yaml.safe_load(fm.group(1)) or {}
    if not data.get("discovery_date") or data.get("superseded_by"):
        return None
    aliases = data.get("aliases") or []
    title = aliases[0] if aliases else data.get("title", "")
    return {
        "title": title,
        "discovery_date": data["discovery_date"],
        "topics": data.get("topics") or [],
    }


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
    recent_papers: list[tuple[str, dict]],
    papers_dir: str,
    site_title: str = "fg-zettelkasten",
) -> str:
    """Render `content/index.md`: a homepage listing recent papers, Topics and Structures.

    Links use explicit `[[<dir>/<slug>|Name]]` paths because Topic and
    Structure notes collide on basename.
    """
    counts = topic_paper_counts(state)
    by_slug = {t["slug"]: t for t in topics}
    total_papers = len(state.get("papers", {}))

    lines = [
        "---",
        f'title: "{site_title}"',
        "---",
        "",
        f"A topic-anchored Zettelkasten built from the `toread` paper feed — "
        f"{_plural(total_papers, 'paper')} across {_plural(len(topics), 'topic')}. "
        "The name follows the [Niklas Luhmann archive](https://niklas-luhmann-archiv.de/) "
        "model: each Topic is a *Schlagwort* (keyword) register that links back to every "
        "paper it covers. Use the graph, backlinks, and search to explore; the entry "
        "points below group the archive by theme.",
        "",
    ]

    if recent_papers:
        lines += [
            "## Latest papers",
            "",
            "Most recent additions to the feed.",
            "",
        ]
        for stem, meta in recent_papers:
            date = str(meta["discovery_date"])[:10]
            topic_names = [
                by_slug[s]["name"] for s in meta["topics"] if s in by_slug
            ]
            line = f"- [[{papers_dir}/{stem}|{meta['title']}]] — {date}"
            if topic_names:
                line += f" · {', '.join(topic_names)}"
            lines.append(line)
        lines.append("")

    lines += [
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
    site_title: str = "fg-zettelkasten",
) -> dict:
    """Populate `content_dir` from the vault and write the homepage.

    Wipes and rebuilds `content_dir`, walking only the named `subdirs` so that
    `.obsidian/` and other non-note files cannot leak into the site. Returns a
    stats dict: `{"notes": int, "stripped": int}`.
    """
    papers_dir, topics_dir, structures_dir = subdirs
    # Topic and Structure notes share slug basenames and identical H1s; the
    # suffix keeps their graph-node labels apart.
    title_suffix = {topics_dir: "", structures_dir: " (Structure)"}

    shutil.rmtree(content_dir, ignore_errors=True)
    content_dir.mkdir(parents=True, exist_ok=True)

    notes = 0
    stripped = 0
    paper_meta: list[tuple[str, dict]] = []
    for subdir in subdirs:
        src = vault_dir / subdir
        if not src.is_dir():
            continue
        dst = content_dir / subdir
        dst.mkdir(parents=True, exist_ok=True)
        for note in sorted(src.glob("*.md")):
            text = note.read_text(encoding="utf-8")
            cleaned = strip_duplicate_title(strip_dataview(text))
            if subdir in title_suffix:
                cleaned = inject_title(cleaned, title_suffix[subdir])
            if cleaned != text:
                stripped += 1
            exported = inject_contributor(inject_date(cleaned))
            (dst / note.name).write_text(exported, encoding="utf-8")
            notes += 1
            if subdir == papers_dir:
                meta = _read_paper_meta(text)
                if meta is not None:
                    paper_meta.append((note.stem, meta))

    paper_meta.sort(key=lambda item: item[1]["discovery_date"], reverse=True)
    recent_papers = paper_meta[:5]

    structure_slugs = {
        p.stem for p in (vault_dir / structures_dir).glob("*.md")
    }
    index = build_index(
        topics,
        state,
        structure_slugs,
        topics_dir,
        structures_dir,
        recent_papers,
        papers_dir,
        site_title=site_title,
    )
    (content_dir / "index.md").write_text(index, encoding="utf-8")

    return {"notes": notes, "stripped": stripped}
