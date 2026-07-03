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


def _format_author(name: str) -> str:
    """An author name in APA form: "Eytan Bakshy" -> "Bakshy, E.",
    "Lada A. Adamic" -> "Adamic, L. A.", "Claes H. de Vreese" -> "de Vreese, C. H.".

    Heuristic: the surname is the last token plus any immediately preceding
    run of lowercase nobiliary particles (de, van, von, della, ...); the
    remaining leading tokens become initials. "Last, First" ordering may still
    format imperfectly.
    """
    parts = name.split()
    if not parts:
        return ""
    if len(parts) == 1:
        return parts[0]
    # Grow the surname backwards over any trailing run of lowercase particles.
    i = len(parts) - 1
    while i > 0 and parts[i - 1].islower():
        i -= 1
    surname = " ".join(parts[i:])
    given = parts[:i]
    if not given:
        return surname
    initials = " ".join(f"{p[0].upper()}." for p in given if p)
    return f"{surname}, {initials}"


def _format_authors(authors: list[str]) -> str:
    """Author list in APA form, joined with commas and a final " & "."""
    formatted = [_format_author(a) for a in authors if a]
    if not formatted:
        return ""
    if len(formatted) == 1:
        return formatted[0]
    return ", ".join(formatted[:-1]) + ", & " + formatted[-1]


def build_apa_citation(paper) -> str:
    """A best-effort APA-7 journal-article citation from feed fields.

    Shape: `Surname, F. M., & Surname, F. M. (Year). Title. *Journal*, *Vol*,
    pages. https://doi.org/<doi>`. Each of journal, volume, pages and the DOI
    link is optional and omitted when absent.
    """
    authors = _format_authors(paper.authors)
    year = _year_of(paper)
    title = (paper.title or "").rstrip(".")

    head = " ".join(p for p in (authors, f"({year})." if year else "") if p)
    pieces = [f"{head} {title}.".strip() if title else head]

    journal = (paper.journal or "").strip()
    volume = (str(paper.volume).strip() if paper.volume else "")
    pages = (str(paper.pages).strip().replace("--", "–") if paper.pages else "")
    if journal:
        tail = f"*{journal}*"
        if volume:
            tail += f", *{volume}*"
        if pages:
            tail += f", {pages}"
        pieces.append(tail + ".")
    elif pages:
        pieces.append(f"{pages}.")

    if paper.doi:
        pieces.append(f"https://doi.org/{paper.doi}")

    return " ".join(p for p in pieces if p).strip()


def render_citation_block(paper) -> str:
    """A blockquote holding the APA citation plus a labeled link to the paper.

    The "View paper" link is omitted when the paper has no URL. Used by both
    `build_paper_note` and the one-time backfill so the rendering stays
    consistent across new and existing notes.
    """
    lines = [f"> {build_apa_citation(paper)}"]
    if paper.url:
        lines.append(">")
        lines.append(f"> [View paper]({paper.url})")
    return "\n".join(lines)


def render_podcast_block(episode: Optional[dict], kind: Optional[str] = None) -> str:
    """The `## Podcast` section for a paper note, or "" when no episode exists.

    Always offers the standalone MP3. Spotify and Apple Podcasts links are added
    only when present in the episode record and the note is not an own
    publication (`kind == "own"`) — own-pub episodes are excluded from
    research-radio's public feed, so they never reach Spotify/Apple. Shared by
    `build_paper_note` and the one-time backfill so new and existing notes stay
    consistent.
    """
    if not episode or not episode.get("audio_url"):
        return ""
    platforms = []
    if kind != "own":
        if episode.get("spotify_url"):
            platforms.append(f"[Spotify]({episode['spotify_url']})")
        if episode.get("apple_url"):
            platforms.append(f"[Apple Podcasts]({episode['apple_url']})")
    lead = (
        "A [research-radio](https://fabiogiglietto.github.io/research-radio/) "
        "episode discusses this paper:"
    )
    if not platforms:
        # MP3 alone — keep the plain "Listen" form.
        body = f"{lead} [Listen]({episode['audio_url']})"
    else:
        links = [f"[MP3]({episode['audio_url']})", *platforms]
        body = f"{lead} 🎧 " + " · ".join(links)
    return f"## Podcast\n\n{body}\n"


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


_WIKILINK_RE = re.compile(r"\[\[([^\[\]|#]+)((?:#[^\[\]|]+)?)(?:\|([^\[\]]+))?\]\]")


def _normalize_key(target: str) -> str:
    """A bibtex key with its first 4-digit year blanked, for near-miss matching."""
    return re.sub(r"(?:19|20)\d{2}", "YYYY", target.strip(), count=1)


def sanitize_links(text: str, known_targets: set[str]) -> tuple[str, list[tuple]]:
    """Repair or de-link every [[wikilink]] whose target is not a real note.

    A target that — ignoring its 4-digit year — matches exactly one known
    target is repaired to it (recovers LLM year-typos). Any other unknown
    target is de-linked to plain text. `known_targets` is the set of resolvable
    note names (paper bibtex keys + topic slugs). Returns (sanitized_text,
    changes), where each change is ("repaired", old, new) or ("delinked", old).
    """
    norm_index: dict[str, list[str]] = {}
    for known in known_targets:
        norm_index.setdefault(_normalize_key(known), []).append(known)

    changes: list[tuple] = []

    def _replace(match: "re.Match[str]") -> str:
        target = match.group(1).strip()
        section = match.group(2) or ""
        alias = match.group(3)
        if target in known_targets:
            return match.group(0)
        candidates = norm_index.get(_normalize_key(target), [])
        if len(candidates) == 1:
            new = candidates[0]
            changes.append(("repaired", target, new))
            return f"[[{new}{section}|{alias}]]" if alias else f"[[{new}{section}]]"
        changes.append(("delinked", target))
        return alias if alias else target

    return _WIKILINK_RE.sub(_replace, text), changes


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

Only ever write a [[...]] wikilink whose target is one of the bibtex keys \
explicitly provided to you, copied exactly. Never invent or guess a key, and \
never link an author name or a citation — refer to any paper not in that list \
as plain text.

Do not add frontmatter, a title heading, or a Podcast section — those are \
added by the caller. Output only the Markdown body."""


def build_paper_note(
    paper,
    summary: dict,
    topics: list[str],
    related_keys: list[str],
    podcast: Optional[dict],
    claude,
    model: str,
    kind: Optional[str] = None,
) -> str:
    """Render a Papers/<bibtex-key>.md note (LLM-assisted).

    Claude writes the body — summary, contributions, methods, findings, a
    "Connections" section with inline [[bibtex-key]] links to `related_keys`,
    and a "Podcast" section when `podcast` (an `episodes_client` record) is set.
    Filename is the bibtex key; the readable title goes in frontmatter `aliases`.

    `kind` adds a frontmatter `kind:` field when set — used to mark the
    author's own publications (`kind: own`) and team-mates' Slack submissions
    (`kind: team`); toread papers leave it unset. A team submission also gets
    `submitted_by`/`slack_permalink` frontmatter from the paper, surfaced on the
    site for attribution.
    """
    academic = paper.academic or {}
    fields: dict[str, Any] = {
        "title": _yaml_quote(paper.title),
        "aliases": [_yaml_quote(paper.title)],
        "authors": [_yaml_quote(a) for a in paper.authors],
        "year": _year_of(paper),
        "doi": paper.doi or "",
        "bibtex_key": paper.bibtex_key,
    }
    if kind:
        fields["kind"] = kind
    if getattr(paper, "submitted_by", None):
        fields["submitted_by"] = _yaml_quote(paper.submitted_by)
        if getattr(paper, "slack_permalink", None):
            fields["slack_permalink"] = paper.slack_permalink
    fields.update(
        {
            "topics": topics,
            "citation_count": academic.get("citation_count", 0),
            "open_access": bool(academic.get("open_access", False)),
            "source_url": paper.url or "",
            "podcast_url": (podcast or {}).get("audio_url") or "",
            "pdf_available": summary.get("pdf_source") == "drive",
            "discovery_date": paper.discovery_date or "",
        }
    )
    fm = render_frontmatter(fields)

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

    note = f"{fm}\n\n# {paper.title}\n\n{render_citation_block(paper)}\n\n{body}\n"
    podcast_block = render_podcast_block(podcast, kind)
    if podcast_block:
        note += f"\n{podcast_block}"
    return note


_STRUCTURE_SYSTEM = """\
You write a Structure note — a hub note in a Niklas-Luhmann-style Zettelkasten. \
A structure note narrates the *line of argument* running across a set of papers \
filed under one topic: how they speak to each other, where they agree and \
diverge, what arc of inquiry they trace. It is a synthesis, not a list of \
abstracts.

Write GitHub-flavoured Markdown, starting at a level-2 heading (the topic title \
is already set in frontmatter — do not repeat it). Reference papers inline as \
[[bibtex-key]] wikilinks, using only the exact bibtex keys given to you, copied \
verbatim — never invent or guess a key; mention anything else as plain text. \
Aim for several tight paragraphs under a few thematic headings. Output only the \
Markdown body — no frontmatter, no title heading."""


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
