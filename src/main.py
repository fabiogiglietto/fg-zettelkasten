"""fg-zettelkasten — build a topic-anchored Obsidian Zettelkasten from the toread feed.

Usage:
    python -m src.main refresh-topics
    python -m src.main bootstrap [--limit N]
    python -m src.main update [--recluster]
    python -m src.main recluster

See README.md and the implementation plan for architecture detail.
"""
from __future__ import annotations

import argparse
import os
import sys
from datetime import datetime, timezone
from pathlib import Path

import yaml

try:
    from dotenv import load_dotenv

    load_dotenv()
except ImportError:  # python-dotenv optional at import time
    pass

ROOT = Path(__file__).resolve().parent.parent


def load_config(path: str = "config.yml") -> dict:
    cfg_path = Path(path)
    if not cfg_path.is_absolute():
        cfg_path = ROOT / cfg_path
    with open(cfg_path) as fh:
        return yaml.safe_load(fh)


# --- helpers --------------------------------------------------------------


def _abs(rel: str) -> str:
    """Resolve a config-relative path against the project root."""
    p = Path(rel)
    return str(p if p.is_absolute() else ROOT / p)


def _now() -> str:
    return datetime.now(timezone.utc).isoformat()


def _claude(cfg: dict):
    """Build the Claude SDK wrapper from config (lazy import keeps --help cheap)."""
    from .claude_client import ClaudeClient

    cc = cfg["claude"]
    return ClaudeClient(
        summary_model=cc["summary_model"],
        reasoning_model=cc["reasoning_model"],
    )


def _drive_client(cfg: dict):
    """Build a DriveClient from the environment, or None when unavailable.

    The Google-Drive PDF source is optional: without it papers fall back to
    abstract-only summaries rather than failing the run.
    """
    creds = os.environ.get("GOOGLE_APPLICATION_CREDENTIALS")
    folder = os.environ.get("GOOGLE_DRIVE_FOLDER_ID")
    if not creds or not folder or not Path(creds).exists():
        print("WARN: Google Drive not configured — using abstract-only summaries")
        return None
    try:
        from .drive_client import DriveClient

        return DriveClient(creds, folder)
    except Exception as exc:  # noqa: BLE001 - Drive is optional, never fatal
        print(f"WARN: could not initialise Drive client ({exc}) — abstract-only")
        return None


def _pdf_text(cfg: dict, drive, paper):
    """Extracted full PDF text for `paper`, cached transiently in data/.cache/."""
    cache_dir = Path(_abs(cfg["paths"]["cache_dir"]))
    cache_file = cache_dir / f"{paper.bibtex_key}.txt"
    if cache_file.exists():
        return cache_file.read_text(encoding="utf-8")
    if drive is None:
        return None
    text = drive.get_pdf_text(
        paper, max_chars=cfg["claude"].get("max_pdf_chars", 80000)
    )
    if text:
        # Some malformed PDFs yield lone surrogate code points that cannot be
        # UTF-8 encoded — neither for the cache file nor the Claude API request.
        text = text.encode("utf-8", "ignore").decode("utf-8")
        cache_dir.mkdir(parents=True, exist_ok=True)
        cache_file.write_text(text, encoding="utf-8")
    return text


def _related_keys(state: dict, paper_id: str, topics: list[str]) -> list[str]:
    """Bibtex keys of other papers sharing at least one topic with `paper_id`."""
    wanted = set(topics)
    out = []
    for pid, entry in state["papers"].items():
        if pid == paper_id:
            continue
        if wanted & set(entry.get("topics", [])):
            out.append(pid.split(":", 1)[-1])
    return out


def _regenerate_topic_notes(cfg: dict, register: list[dict], state: dict) -> None:
    """Deterministically rewrite every Topics/*.md register entry note."""
    from . import note_builder

    vault = _abs(cfg["vault"]["path"])
    topics_dir = cfg["vault"]["topics_dir"]
    for topic in register:
        members = [
            pid.split(":", 1)[-1]
            for pid, entry in state["papers"].items()
            if topic["slug"] in entry.get("topics", [])
        ]
        content = note_builder.build_topic_note(topic, members)
        note_builder.write_note(vault, topics_dir, topic["slug"], content)


def _rewrite_note_topics(note_path: str, topics: list[str]) -> None:
    """Update a paper note's frontmatter `topics:` line in place (no LLM)."""
    p = Path(note_path)
    if not p.exists():
        return
    lines = p.read_text(encoding="utf-8").splitlines()
    new_line = f"topics: [{', '.join(topics)}]"
    for i, line in enumerate(lines):
        if line.startswith("topics:"):
            lines[i] = new_line
            break
    p.write_text("\n".join(lines) + "\n", encoding="utf-8")


# --- commands -------------------------------------------------------------
# Each command is a thin orchestrator over src/* modules.


def _build_register(cfg: dict, claude) -> list[dict]:
    """Fetch the live github.io signals and synthesize the anchor topics."""
    from . import topics_client

    signals = topics_client.fetch_signals(
        cfg["inputs"]["github_io_base"], cfg["inputs"]["github_io_signals"]
    )
    if not signals:
        raise RuntimeError("no research-agenda signals could be fetched")
    return topics_client.synthesize_register(signals, claude, cfg["topics"])


def _topic_members(slug: str, state: dict, papers_by_key: dict) -> list:
    """The `Paper` objects assigned to `slug`, in feed order."""
    return [
        papers_by_key[key]
        for pid, entry in state["papers"].items()
        for key in (pid.split(":", 1)[-1],)
        if slug in entry.get("topics", []) and key in papers_by_key
    ]


def _generate_structure_notes(cfg, register, state, papers_by_key, summaries, claude):
    """Render one Structures/<slug>.md hub note per non-empty topic."""
    from . import note_builder

    vault = _abs(cfg["vault"]["path"])
    structures_dir = cfg["vault"]["structures_dir"]
    for topic in register:
        members = _topic_members(topic["slug"], state, papers_by_key)
        if not members:
            continue
        note = note_builder.build_structure_note(
            topic, members, summaries, claude, claude.reasoning_model
        )
        note_builder.write_note(vault, structures_dir, topic["slug"], note)


def cmd_refresh_topics(cfg: dict, args) -> int:
    """Rebuild the topic register from the live github.io research-agenda signals."""
    from . import topics_client, state as state_mod

    claude = _claude(cfg)
    register = _build_register(cfg, claude)

    # Anchor topics are re-synthesized; emergent topics (created at
    # bootstrap/recluster) are carried over so existing assignments survive.
    topics_file = _abs(cfg["paths"]["topics_file"])
    emergent = [t for t in topics_client.load_topics(topics_file) if t.get("is_emergent")]
    register = register + emergent

    topics_client.save_topics(register, topics_file)
    state = state_mod.load_state(_abs(cfg["paths"]["state_file"]))
    _regenerate_topic_notes(cfg, register, state)
    print(f"refresh-topics: {len(register)} topics written to the register")
    return 0


def cmd_bootstrap(cfg: dict, args) -> int:
    """Process the whole archive: register, per-paper notes, themes, hub notes."""
    from . import (
        feed_client,
        episodes_client,
        topics_client,
        summarizer,
        themes,
        note_builder,
        state as state_mod,
    )

    claude = _claude(cfg)
    drive = _drive_client(cfg)

    register = _build_register(cfg, claude)
    papers = feed_client.fetch_feed(cfg["inputs"]["feed_url"])
    episodes = episodes_client.fetch_episode_audio(cfg["inputs"]["episodes_url"])
    if args.limit:
        papers = papers[: args.limit]
    print(f"bootstrap: {len(papers)} papers, {len(register)} anchor topics")

    summaries_dir = _abs(cfg["paths"]["summaries_dir"])
    papers_dir = cfg["vault"]["papers_dir"]
    state = {"papers": {}, "last_full_cluster": _now(), "papers_since_cluster": 0}
    summaries: dict[str, dict] = {}

    # 1. summarize every paper (full PDF when available, else abstract).
    #    Reuse an existing summary when present so an interrupted run can be
    #    resumed without re-billing the per-paper Claude pass.
    for i, paper in enumerate(papers, 1):
        cached = summarizer.load_summary(summaries_dir, paper.bibtex_key)
        if cached is not None:
            print(f"  [{i}/{len(papers)}] cached   {paper.bibtex_key}")
            summary = cached
        else:
            print(f"  [{i}/{len(papers)}] summarize {paper.bibtex_key}")
            text = _pdf_text(cfg, drive, paper)
            summary = summarizer.summarize_paper(
                paper, text, claude, claude.summary_model
            )
            summarizer.save_summary(summary, summaries_dir, paper.bibtex_key)
        summaries[paper.bibtex_key] = summary
        podcast = paper.id in episodes
        state["papers"][paper.id] = {
            "note_path": f"{papers_dir}/{paper.bibtex_key}.md",
            "topics": [],
            "pdf_source": summary["pdf_source"],
            "content_hash": state_mod.content_hash(paper.abstract, podcast),
            "podcast_linked": podcast,
            "last_processed": _now(),
        }

    # 2. topic-anchored assignment + emergent sub-themes.
    unassigned = []
    for paper in papers:
        slugs = themes.assign_paper(
            paper, summaries[paper.bibtex_key], register, claude, claude.reasoning_model
        )
        state["papers"][paper.id]["topics"] = slugs
        if not slugs:
            unassigned.append(paper)

    emergent = themes.find_emergent(
        unassigned, summaries, claude, claude.reasoning_model,
        cfg["topics"]["emergent_min_papers"],
    )
    for topic in emergent:
        register.append(
            {
                "slug": topic["slug"],
                "name": topic["name"],
                "description": topic["description"],
                "source_signals": [],
                "is_emergent": True,
            }
        )
        for key in topic["members"]:
            entry = state["papers"].get(f"bibtex:{key}")
            if entry is not None:
                entry["topics"].append(topic["slug"])

    topics_client.save_topics(register, _abs(cfg["paths"]["topics_file"]))
    print(f"  {len(unassigned)} unassigned, {len(emergent)} emergent topic(s)")

    # 3. render paper notes, then regenerate Topics/ and Structures/.
    vault = _abs(cfg["vault"]["path"])
    for paper in papers:
        entry = state["papers"][paper.id]
        related = _related_keys(state, paper.id, entry["topics"])
        note = note_builder.build_paper_note(
            paper, summaries[paper.bibtex_key], entry["topics"], related,
            episodes.get(paper.id), claude, claude.reasoning_model,
        )
        note_builder.write_note(vault, papers_dir, paper.bibtex_key, note)

    _regenerate_topic_notes(cfg, register, state)
    papers_by_key = {p.bibtex_key: p for p in papers}
    _generate_structure_notes(cfg, register, state, papers_by_key, summaries, claude)

    state_mod.save_state(state, _abs(cfg["paths"]["state_file"]))
    print("bootstrap: done")
    return 0


def cmd_update(cfg: dict, args) -> int:
    """Daily incremental run: new/changed papers only."""
    from . import (
        feed_client,
        episodes_client,
        topics_client,
        summarizer,
        themes,
        note_builder,
        state as state_mod,
    )

    claude = _claude(cfg)
    drive = _drive_client(cfg)

    topics_file = _abs(cfg["paths"]["topics_file"])
    register = topics_client.load_topics(topics_file)
    state = state_mod.load_state(_abs(cfg["paths"]["state_file"]))
    if not register:
        print("update: no topic register — run refresh-topics or bootstrap first")
        return 1

    papers = feed_client.fetch_feed(cfg["inputs"]["feed_url"])
    episodes = episodes_client.fetch_episode_audio(cfg["inputs"]["episodes_url"])
    summaries_dir = _abs(cfg["paths"]["summaries_dir"])
    papers_dir = cfg["vault"]["papers_dir"]
    vault = _abs(cfg["vault"]["path"])

    # Diff the feed against state by id and by content hash.
    new_papers, changed_papers = [], []
    for paper in papers:
        podcast = paper.id in episodes
        new_hash = state_mod.content_hash(paper.abstract, podcast)
        entry = state["papers"].get(paper.id)
        if entry is None:
            new_papers.append(paper)
        elif entry.get("content_hash") != new_hash:
            changed_papers.append(paper)
    print(f"update: {len(new_papers)} new, {len(changed_papers)} changed")

    summaries: dict[str, dict] = {}

    # New papers: summarize + assign to existing register topics.
    for paper in new_papers:
        text = _pdf_text(cfg, drive, paper)
        summary = summarizer.summarize_paper(
            paper, text, claude, claude.summary_model
        )
        summarizer.save_summary(summary, summaries_dir, paper.bibtex_key)
        summaries[paper.bibtex_key] = summary
        slugs = themes.assign_paper(
            paper, summary, register, claude, claude.reasoning_model
        )
        podcast = paper.id in episodes
        state["papers"][paper.id] = {
            "note_path": f"{papers_dir}/{paper.bibtex_key}.md",
            "topics": slugs,
            "pdf_source": summary["pdf_source"],
            "content_hash": state_mod.content_hash(paper.abstract, podcast),
            "podcast_linked": podcast,
            "last_processed": _now(),
        }

    # Changed papers: refresh the state hash (e.g. a podcast episode appeared).
    for paper in changed_papers:
        podcast = paper.id in episodes
        entry = state["papers"][paper.id]
        entry["podcast_linked"] = podcast
        entry["content_hash"] = state_mod.content_hash(paper.abstract, podcast)
        entry["last_processed"] = _now()

    # Re-render the note for every new or changed paper.
    touched = new_papers + changed_papers
    for paper in touched:
        entry = state["papers"][paper.id]
        summary = summaries.get(paper.bibtex_key) or summarizer.load_summary(
            summaries_dir, paper.bibtex_key
        )
        if summary is None:
            print(f"  WARN: no summary for {paper.bibtex_key}, skipping note")
            continue
        related = _related_keys(state, paper.id, entry["topics"])
        note = note_builder.build_paper_note(
            paper, summary, entry["topics"], related,
            episodes.get(paper.id), claude, claude.reasoning_model,
        )
        note_builder.write_note(vault, papers_dir, paper.bibtex_key, note)

    state["papers_since_cluster"] = (
        state.get("papers_since_cluster", 0) + len(new_papers)
    )
    if touched:
        _regenerate_topic_notes(cfg, register, state)

    threshold = cfg["processing"]["recluster_threshold"]
    do_recluster = args.recluster or state["papers_since_cluster"] >= threshold
    state_mod.save_state(state, _abs(cfg["paths"]["state_file"]))

    if not touched and not do_recluster:
        print("update: nothing to do")
        return 0

    if do_recluster:
        _recluster(cfg, claude, drive)

    print("update: done")
    return 0


def _recluster(cfg: dict, claude, drive) -> None:
    """Full re-cluster: rebuild the register, re-assign every processed paper,
    regenerate Topics/ and Structures/. Paper note bodies are not re-summarised
    (cost) — only their frontmatter `topics:` is updated in place."""
    from . import feed_client, topics_client, summarizer, themes, state as state_mod

    print("recluster: rebuilding the register and re-clustering the archive")
    register = _build_register(cfg, claude)
    state = state_mod.load_state(_abs(cfg["paths"]["state_file"]))
    summaries_dir = _abs(cfg["paths"]["summaries_dir"])

    papers = [
        p for p in feed_client.fetch_feed(cfg["inputs"]["feed_url"])
        if p.id in state["papers"]
    ]
    summaries: dict[str, dict] = {}
    for paper in papers:
        s = summarizer.load_summary(summaries_dir, paper.bibtex_key)
        if s is not None:
            summaries[paper.bibtex_key] = s

    unassigned = []
    for paper in papers:
        summary = summaries.get(paper.bibtex_key)
        if summary is None:
            continue
        slugs = themes.assign_paper(
            paper, summary, register, claude, claude.reasoning_model
        )
        state["papers"][paper.id]["topics"] = slugs
        if not slugs:
            unassigned.append(paper)

    emergent = themes.find_emergent(
        unassigned, summaries, claude, claude.reasoning_model,
        cfg["topics"]["emergent_min_papers"],
    )
    for topic in emergent:
        register.append(
            {
                "slug": topic["slug"],
                "name": topic["name"],
                "description": topic["description"],
                "source_signals": [],
                "is_emergent": True,
            }
        )
        for key in topic["members"]:
            entry = state["papers"].get(f"bibtex:{key}")
            if entry is not None:
                entry["topics"].append(topic["slug"])

    topics_client.save_topics(register, _abs(cfg["paths"]["topics_file"]))

    # Update each paper note's frontmatter topics in place (no re-summary).
    vault = Path(_abs(cfg["vault"]["path"]))
    for paper in papers:
        entry = state["papers"][paper.id]
        _rewrite_note_topics(str(vault / entry["note_path"]), entry["topics"])

    _regenerate_topic_notes(cfg, register, state)
    papers_by_key = {p.bibtex_key: p for p in papers}
    _generate_structure_notes(cfg, register, state, papers_by_key, summaries, claude)

    state["last_full_cluster"] = _now()
    state["papers_since_cluster"] = 0
    state_mod.save_state(state, _abs(cfg["paths"]["state_file"]))
    print(f"recluster: {len(register)} topics, {len(emergent)} emergent")


def cmd_recluster(cfg: dict, args) -> int:
    """Force a full re-cluster of the whole archive."""
    args.recluster = True
    return cmd_update(cfg, args)


# --- CLI ------------------------------------------------------------------


def build_parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(prog="fg-zettelkasten", description=__doc__)
    parser.add_argument("--config", default="config.yml", help="path to config.yml")
    sub = parser.add_subparsers(dest="command", required=True)

    p_bootstrap = sub.add_parser("bootstrap", help="process the whole archive (run once)")
    p_bootstrap.add_argument(
        "--limit", type=int, default=None, help="process only the first N papers"
    )

    p_update = sub.add_parser("update", help="incremental daily run")
    p_update.add_argument(
        "--recluster", action="store_true", help="also run a full re-cluster"
    )

    sub.add_parser("refresh-topics", help="rebuild the topic register from github.io")
    sub.add_parser("recluster", help="force a full re-cluster")
    return parser


def main(argv=None) -> int:
    args = build_parser().parse_args(argv)
    cfg = load_config(args.config)

    commands = {
        "bootstrap": cmd_bootstrap,
        "update": cmd_update,
        "refresh-topics": cmd_refresh_topics,
        "recluster": cmd_recluster,
    }
    return commands[args.command](cfg, args) or 0


if __name__ == "__main__":
    sys.exit(main())
