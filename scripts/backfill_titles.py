"""One-time backfill: decode HTML-escaped titles in existing paper notes.

Until 2026-09 the toread feed published titles HTML-escaped (`&quot;`,
`&#x27;`), and `feed_client` copied them verbatim, so the entities reached note
frontmatter, the H1, the citation block — and the published Quartz page, which
escaped them a second time (`&amp;quot;`). Both the escaper (upstream) and the
copy (`feed_client._text`) are fixed, but note rendering is keyed on the
abstract, not the title, so already-built notes never regenerate on their own.

This walks `vault/Papers/*.md`, decodes each note's own frontmatter title, and
rewrites every place that title appears — frontmatter `title`/`aliases` (through
`note_builder._yaml_quote`, since a decoded title carries bare `"`), the H1, the
citation blockquote, and any supersede-stub mention. Deriving the correct title
from the note itself keeps tombstone stubs (absent from the feed) in scope.

Also repairs `data/state.json`: a stored escaped title normalizes to the literal
word `quot`, which silently breaks dedup for that paper.

Idempotent — a note with no entities in its title is left untouched.

Run from the repo root:  python -m scripts.backfill_titles
"""
from __future__ import annotations

import html
import json
import re
import sys
from pathlib import Path

import yaml

from src import note_builder

_FRONTMATTER = re.compile(r"\A---\n(.*?)\n---\n", re.DOTALL)
_TITLE_LINE = re.compile(r"^title: .*$", re.MULTILINE)
_ALIASES_LINE = re.compile(r"^aliases: \[.*\]$", re.MULTILINE)


def _fix_note(path: Path) -> str | None:
    """Rewrite `path` in place if its title carries HTML entities.

    Returns the decoded title when the note changed, else None.
    """
    text = path.read_text(encoding="utf-8")
    match = _FRONTMATTER.match(text)
    if not match:
        return None
    try:
        frontmatter = yaml.safe_load(match.group(1)) or {}
    except yaml.YAMLError:
        print(f"  WARN: unparseable frontmatter in {path.name}")
        return None

    escaped = str(frontmatter.get("title") or "")
    decoded = html.unescape(escaped)
    if not escaped or decoded == escaped:
        return None

    head, body = text[: match.end()], text[match.end() :]
    # Frontmatter goes through the renderer's quoting: the decoded title can
    # carry a bare `"`, which a plain substitution would leave as invalid YAML.
    quoted = note_builder._yaml_quote(decoded)
    head = _TITLE_LINE.sub(f"title: {quoted}", head, count=1)
    head = _ALIASES_LINE.sub(f"aliases: [{quoted}]", head, count=1)
    # The body carries the title verbatim (H1, citation, stub mentions); a
    # literal replace leaves any other entity in the prose alone.
    body = body.replace(escaped, decoded)

    path.write_text(head + body, encoding="utf-8")
    return decoded


def _fix_state(state_file: Path) -> int:
    """Decode escaped `title` fields in state entries. Returns the count."""
    if not state_file.exists():
        return 0
    state = json.loads(state_file.read_text(encoding="utf-8"))
    fixed = 0
    for entry in state.get("papers", {}).values():
        title = entry.get("title")
        if not title:
            continue
        decoded = html.unescape(str(title))
        if decoded != title:
            entry["title"] = decoded
            fixed += 1
    if fixed:
        state_file.write_text(
            json.dumps(state, indent=2, ensure_ascii=False), encoding="utf-8"
        )
    return fixed


def main() -> int:
    cfg = yaml.safe_load(Path("config.yml").read_text(encoding="utf-8"))
    papers_dir = Path(cfg["vault"]["path"]) / cfg["vault"]["papers_dir"]

    fixed = 0
    for note in sorted(papers_dir.glob("*.md")):
        decoded = _fix_note(note)
        if decoded:
            fixed += 1
            print(f"  {note.stem}: {decoded}")

    state_fixed = _fix_state(Path(cfg["paths"]["state_file"]))
    print(f"backfill-titles: {fixed} note(s), {state_fixed} state entry(ies) decoded")
    return 0


if __name__ == "__main__":
    sys.exit(main())
