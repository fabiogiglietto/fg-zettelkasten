"""fg-zettelkasten — build a topic-anchored Obsidian Zettelkasten from the toread feed.

Usage:
    python -m src.main refresh-topics
    python -m src.main bootstrap [--limit N]
    python -m src.main summarize
    python -m src.main update [--recluster]
    python -m src.main recluster
    python -m src.main export-site
    python -m src.main slack-test <bibtex-key>

See README.md and the implementation plan for architecture detail.
"""
from __future__ import annotations

import argparse
import os
import sys
import time
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


def _note_url(cfg: dict, bibtex_key: str) -> str | None:
    """Live website URL of a paper's note, for the Slack digest's Full-note link.

    The bibtex key is also the Quartz page slug, so the published URL is just
    `note_base_url/<bibtex_key>` (extensionless — Quartz serves no `.md`).
    Returns None when `slack.note_base_url` is unset so the link is omitted."""
    base = cfg.get("slack", {}).get("note_base_url")
    return f"{base.rstrip('/')}/{bibtex_key}" if base else None


def _claude(cfg: dict):
    """Build the Claude SDK wrapper from config (lazy import keeps --help cheap)."""
    from .claude_client import ClaudeClient

    cc = cfg["claude"]
    return ClaudeClient(
        summary_model=cc["summary_model"],
        reasoning_model=cc["reasoning_model"],
        assign_model=cc.get("assign_model"),
        note_model=cc.get("note_model"),
    )


def _slack_wait_expired(entry: dict, max_days: float) -> bool:
    """True once a paper has waited longer than `max_days` for its episode.

    The fallback that lets a paper whose podcast episode never appears still
    be announced. Measured from `last_processed` — when the paper was first
    seen — so the wait does not restart on unrelated re-processing."""
    ts = entry.get("last_processed")
    if not ts:
        return True
    age = datetime.now(timezone.utc) - datetime.fromisoformat(ts)
    return age.total_seconds() >= max_days * 86400


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
    # The team fork also searches team-toread's Slack-inbox Drive folder, where
    # team-submitted PDFs are uploaded (separate from the Paperpile folder).
    folders = [folder]
    inbox_folder = os.environ.get("SLACK_INBOX_DRIVE_FOLDER_ID")
    if inbox_folder:
        folders.append(inbox_folder)
    try:
        from .drive_client import DriveClient

        return DriveClient(creds, folders)
    except Exception as exc:  # noqa: BLE001 - Drive is optional, never fatal
        print(f"WARN: could not initialise Drive client ({exc}) — abstract-only")
        return None


def _pdf_text(cfg: dict, drive, paper):
    """Extracted full PDF text for `paper`, cached transiently in data/.cache/.

    Own publications carry an `open_access_pdf_url` (the green-OA PDF resolved
    from ORA) and are fetched directly; toread papers use the Paperpile Drive
    PDF. Returns None when no PDF is available.
    """
    cache_dir = Path(_abs(cfg["paths"]["cache_dir"]))
    cache_file = cache_dir / f"{paper.bibtex_key}.txt"
    if cache_file.exists():
        return cache_file.read_text(encoding="utf-8")
    max_chars = cfg["claude"].get("max_pdf_chars", 80000)

    text = None
    oa_pdf_url = (paper.academic or {}).get("open_access_pdf_url")
    if oa_pdf_url:
        from .pdf_fetcher import pdf_text_from_url

        text = pdf_text_from_url(oa_pdf_url, max_chars=max_chars)
    if text is None and drive is not None:
        text = drive.get_pdf_text(paper, max_chars=max_chars)

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


def _prune_stale_notes(notes_dir: Path, keep: set[str]) -> list[str]:
    """Delete *.md files in `notes_dir` whose slug is not in `keep`.

    Derived note directories (Topics/, Structures/) are regenerated by
    slug-named filename. Topic slugs are re-synthesized on every run, so a
    slug that disappears would otherwise leave an orphan note behind; pruning
    to exactly the slugs just written keeps reruns free of stale notes.
    """
    if not notes_dir.is_dir():
        return []
    removed = [f.name for f in notes_dir.glob("*.md") if f.stem not in keep]
    for name in removed:
        (notes_dir / name).unlink()
    return removed


def _regenerate_topic_notes(cfg: dict, register: list[dict], state: dict) -> None:
    """Deterministically rewrite every Topics/*.md register entry note."""
    from . import note_builder

    vault = _abs(cfg["vault"]["path"])
    topics_dir = cfg["vault"]["topics_dir"]
    written: set[str] = set()
    for topic in register:
        members = [
            pid.split(":", 1)[-1]
            for pid, entry in state["papers"].items()
            if topic["slug"] in entry.get("topics", [])
        ]
        content = note_builder.build_topic_note(topic, members)
        note_builder.write_note(vault, topics_dir, topic["slug"], content)
        written.add(topic["slug"])
    stale = _prune_stale_notes(Path(vault) / topics_dir, written)
    if stale:
        print(f"  pruned {len(stale)} stale topic note(s)")


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


def _sanitize_vault_links(cfg: dict, verbose: bool = False) -> dict:
    """Repair / de-link unresolved [[wikilinks]] in paper and structure notes.

    LLM-written "Connections" sometimes link bibtex keys absent from the vault
    (year-typos or invented citations). This pass resolves every wikilink
    against the actual note filenames on disk — no LLM, idempotent.
    """
    from . import note_builder

    vault = Path(_abs(cfg["vault"]["path"]))
    papers_dir = vault / cfg["vault"]["papers_dir"]
    structures_dir = vault / cfg["vault"]["structures_dir"]
    topics_dir = vault / cfg["vault"]["topics_dir"]

    known = {f.stem for f in papers_dir.glob("*.md")}
    known |= {f.stem for f in topics_dir.glob("*.md")}

    notes_changed = 0
    repaired: dict[str, str] = {}
    delinked: set[str] = set()
    for note_dir in (papers_dir, structures_dir):
        for note in sorted(note_dir.glob("*.md")):
            original = note.read_text(encoding="utf-8")
            fixed, changes = note_builder.sanitize_links(original, known)
            if not changes:
                continue
            note.write_text(fixed, encoding="utf-8")
            notes_changed += 1
            for change in changes:
                if change[0] == "repaired":
                    repaired[change[1]] = change[2]
                else:
                    delinked.add(change[1])
            if verbose:
                detail = ", ".join(
                    f"{c[1]}->{c[2]}" if c[0] == "repaired" else f"-{c[1]}"
                    for c in changes
                )
                print(f"  {note.name}: {detail}")
    return {
        "notes_changed": notes_changed,
        "repaired": repaired,
        "delinked": sorted(delinked),
    }


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


def _generate_structure_notes(
    cfg, register, state, papers_by_key, summaries, claude, force: bool = False
):
    """Render one Structures/<slug>.md hub note per non-empty topic.

    With `processing.incremental_recluster` on, a topic whose inputs (name,
    description, membership, member digests, model) are unchanged since the
    last run keeps its existing note instead of re-billing the LLM call."""
    from . import note_builder, themes, state as state_mod

    incremental = cfg.get("processing", {}).get("incremental_recluster", False)
    vault = _abs(cfg["vault"]["path"])
    structures_dir = cfg["vault"]["structures_dir"]
    fps = state.setdefault("structure_fps", {})
    written: set[str] = set()
    generated = skipped = 0
    for topic in register:
        members = _topic_members(topic["slug"], state, papers_by_key)
        if not members:
            continue
        member_keys = [p.bibtex_key for p in members]
        digests = "\n".join(
            themes.summary_digest(summaries.get(k, {})) for k in sorted(member_keys)
        )
        fp = state_mod.structure_fingerprint(
            topic, member_keys, digests, claude.reasoning_model
        )
        note_file = Path(vault) / structures_dir / f"{topic['slug']}.md"
        if (incremental and not force
                and fps.get(topic["slug"]) == fp and note_file.exists()):
            written.add(topic["slug"])  # keep — _prune_stale_notes must not delete it
            skipped += 1
            continue
        note = note_builder.build_structure_note(
            topic, members, summaries, claude, claude.reasoning_model
        )
        note_builder.write_note(vault, structures_dir, topic["slug"], note)
        fps[topic["slug"]] = fp
        written.add(topic["slug"])
        generated += 1
    # Fingerprints of topics that vanished (or emptied out) go with their notes.
    for slug in list(fps):
        if slug not in written:
            del fps[slug]
    if incremental:
        print(f"  structure notes: {generated} generated, {skipped} skipped (unchanged)")
    stale = _prune_stale_notes(Path(vault) / structures_dir, written)
    if stale:
        print(f"  pruned {len(stale)} stale structure note(s)")


def cmd_refresh_topics(cfg: dict, args) -> int:
    """Rebuild the topic register from the live github.io research-agenda signals."""
    from . import topics_client, state as state_mod

    topics_file = _abs(cfg["paths"]["topics_file"])
    state_file = _abs(cfg["paths"]["state_file"])
    state = state_mod.load_state(state_file)

    signals = topics_client.fetch_signals(
        cfg["inputs"]["github_io_base"], cfg["inputs"]["github_io_signals"]
    )
    if not signals:
        raise RuntimeError("no research-agenda signals could be fetched")
    sig_hash = state_mod.signals_hash(signals)

    existing = topics_client.load_topics(topics_file)
    skip_unchanged = cfg.get("topics", {}).get("skip_unchanged_signals", False)
    if (skip_unchanged and existing
            and state.get("register_signals_hash") == sig_hash):
        # The github.io agenda is byte-identical to what the last synthesis
        # saw. Re-running the LLM would only re-word the same topics — and
        # needlessly invalidate every assignment fingerprint downstream.
        register = existing
        print(f"refresh-topics: signals unchanged — register kept "
              f"({len(register)} topics, no Claude call)")
    else:
        claude = _claude(cfg)
        register = topics_client.synthesize_register(signals, claude, cfg["topics"])
        # Anchor topics are re-synthesized; emergent topics (created at
        # bootstrap/recluster) are carried over so existing assignments survive.
        register = register + [t for t in existing if t.get("is_emergent")]
        topics_client.save_topics(register, topics_file)
        state["register_signals_hash"] = sig_hash
        state_mod.save_state(state, state_file)
        print(f"refresh-topics: {len(register)} topics written to the register")

    _regenerate_topic_notes(cfg, register, state)
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
    episodes = episodes_client.fetch_episodes(cfg["inputs"]["episodes_url"])
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
    reg_fp = state_mod.register_fingerprint(register)
    unassigned = []
    for paper in papers:
        slugs = themes.assign_paper(
            paper, summaries[paper.bibtex_key], register, claude, claude.assign_model
        )
        state["papers"][paper.id]["topics"] = slugs
        state["papers"][paper.id]["assign_fp"] = state_mod.assign_fingerprint(
            reg_fp, themes.summary_digest(summaries[paper.bibtex_key]),
            claude.assign_model,
        )
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
            episodes.get(paper.id), claude, claude.note_model,
        )
        note_builder.write_note(vault, papers_dir, paper.bibtex_key, note)

    _regenerate_topic_notes(cfg, register, state)
    papers_by_key = {p.bibtex_key: p for p in papers}
    _generate_structure_notes(cfg, register, state, papers_by_key, summaries, claude)

    sanitised = _sanitize_vault_links(cfg)
    print(
        f"  link sanitiser: {len(sanitised['repaired'])} repaired, "
        f"{len(sanitised['delinked'])} de-linked"
    )

    state_mod.save_state(state, _abs(cfg["paths"]["state_file"]))
    print("bootstrap: done")
    return 0


def cmd_summarize(cfg: dict, args) -> int:
    """Pipeline stage 1: ensure every feed paper has a structured summary.

    Produces data/summaries/<key>.json and stops — no themes, notes or Slack.
    research-radio consumes these summaries as a podcast-script scaffold, so
    they must exist *before* the podcast is generated; hence this runs ahead
    of research-radio in the chain. `update` (which runs after the podcast)
    reuses these summaries and stays self-sufficient: run on its own, the
    daily fallback cron still summarizes anything this stage missed."""
    from . import feed_client, summarizer

    claude = _claude(cfg)
    drive = _drive_client(cfg)
    summaries_dir = _abs(cfg["paths"]["summaries_dir"])

    papers = feed_client.fetch_feed(cfg["inputs"]["feed_url"])
    pending = [
        p for p in papers
        if summarizer.load_summary(summaries_dir, p.bibtex_key) is None
    ]
    print(f"summarize: {len(pending)} of {len(papers)} paper(s) need a summary")
    for i, paper in enumerate(pending, 1):
        print(f"  [{i}/{len(pending)}] summarize {paper.bibtex_key}")
        text = _pdf_text(cfg, drive, paper)
        summary = summarizer.summarize_paper(
            paper, text, claude, claude.summary_model
        )
        summarizer.save_summary(summary, summaries_dir, paper.bibtex_key)
    print("summarize: done")
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
        slack_client,
        state as state_mod,
    )

    claude = _claude(cfg)
    drive = _drive_client(cfg)

    # Post a digest of each newly-added paper to Slack only when the feature is
    # enabled in config *and* a webhook secret is present (so local runs and
    # contributors without the secret are unaffected).
    # Digest scope/timing knobs — defaults are the fg-chain behavior; the
    # team fork sets digest_scope: "team" and episode_wait_days: 0.
    digest_scope = cfg.get("slack", {}).get("digest_scope", "all")
    episode_wait_days = cfg.get("slack", {}).get("episode_wait_days", 2)
    post_to_slack = bool(cfg.get("slack", {}).get("enabled")) and bool(
        os.environ.get("SLACK_WEBHOOK_URL")
    )

    topics_file = _abs(cfg["paths"]["topics_file"])
    register = topics_client.load_topics(topics_file)
    state = state_mod.load_state(_abs(cfg["paths"]["state_file"]))
    if not register:
        print("update: no topic register — run refresh-topics or bootstrap first")
        return 1
    # Fingerprint of the assignment inputs shared by every paper this run;
    # lets Monday's recluster skip papers assigned against the same register.
    reg_fp = state_mod.register_fingerprint(register)

    papers = feed_client.fetch_feed(cfg["inputs"]["feed_url"])
    episodes = episodes_client.fetch_episodes(cfg["inputs"]["episodes_url"])
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

    # Duplicate safety net (multi-user archive): a brand-new id may refer to a
    # paper already in the vault under a different id — e.g. a team-mate's Slack
    # submission of a paper Fabio already curates. team-toread replies "already
    # in the archive" at ingest time, but races/older notes can slip through, so
    # we also skip here by normalized DOI/title. Changed papers keep their id and
    # are never deduped.
    dup_index = state_mod.dedup_index(state)
    # Augment with the seeded corpus: notes whose state entry predates the
    # per-entry doi/title fields (the ~hundreds of papers a team fork is seeded
    # with) are only indexable from their frontmatter. Without this, a re-submit
    # of an already-archived paper is missed at launch — the common case.
    for k, v in state_mod.dedup_index_from_notes(Path(vault) / papers_dir).items():
        dup_index.setdefault(k, v)
    deduped = []
    for paper in new_papers:
        existing = state_mod.find_duplicate(dup_index, paper.doi, paper.title)
        if existing:
            print(f"  dedup: {paper.bibtex_key} duplicates {existing} "
                  f"— skipping")
            continue
        deduped.append(paper)
    new_papers = deduped
    print(f"update: {len(new_papers)} new, {len(changed_papers)} changed")

    summaries: dict[str, dict] = {}

    # New papers: summarize + assign to existing register topics. Reuse the
    # summary produced by the `summarize` stage when present, so the pipeline
    # never bills the per-paper Claude summary twice; fall back to summarizing
    # here so the daily `update` cron remains self-sufficient.
    for paper in new_papers:
        summary = summarizer.load_summary(summaries_dir, paper.bibtex_key)
        if summary is None:
            text = _pdf_text(cfg, drive, paper)
            summary = summarizer.summarize_paper(
                paper, text, claude, claude.summary_model
            )
            summarizer.save_summary(summary, summaries_dir, paper.bibtex_key)
        summaries[paper.bibtex_key] = summary
        slugs = themes.assign_paper(
            paper, summary, register, claude, claude.assign_model
        )
        podcast = paper.id in episodes
        entry = {
            "note_path": f"{papers_dir}/{paper.bibtex_key}.md",
            "topics": slugs,
            "assign_fp": state_mod.assign_fingerprint(
                reg_fp, themes.summary_digest(summary), claude.assign_model
            ),
            # DOI + title persisted so dedup_index can catch a later id that
            # refers to the same paper.
            "doi": paper.doi or "",
            "title": paper.title,
            "pdf_source": summary["pdf_source"],
            "content_hash": state_mod.content_hash(paper.abstract, podcast),
            "podcast_linked": podcast,
            "slack_posted": False,
            # Queued for a #toread digest. Scope depends on config
            # (`slack.digest_scope`): "all" (fg default) queues every new
            # paper; "team" (mine) queues only team Slack submissions —
            # Paperpile-origin papers flow through both kastens' pipelines
            # and fg-zettelkasten already announces them, so the team kasten
            # posting them too would double-post in #toread.
            "slack_pending": (paper.is_team_submission
                              if digest_scope == "team" else True),
            "last_processed": _now(),
        }
        # A team-mate's Slack submission: tag it `kind: team` and carry the
        # submitter through to the note frontmatter (published for attribution).
        if paper.is_team_submission:
            entry["kind"] = "team"
            entry["submitted_by"] = paper.submitted_by
        state["papers"][paper.id] = entry

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
            episodes.get(paper.id), claude, claude.note_model,
            kind=entry.get("kind"),
        )
        note_builder.write_note(vault, papers_dir, paper.bibtex_key, note)

    # --- Slack digests ----------------------------------------------------
    # Post each queued paper's digest to #toread exactly once. Scope and
    # timing come from config:
    #   - digest_scope "all" (fg default): every new paper, held until its
    #     research-radio episode appears so the post carries the 🎧 Listen
    #     link, with `episode_wait_days` as the fallback deadline.
    #   - digest_scope "team" + episode_wait_days 0 (mine): only team Slack
    #     submissions, posted immediately — research-radio never sources the
    #     Slack-inbox folder, so a team paper never gets an episode and
    #     waiting would only delay every post.
    # `slack_pending` marks a paper as awaiting its digest (set when first
    # seen, cleared once posted); `slack_posted` keeps the post idempotent
    # across retries.
    #
    # Papers predating this flag are classified by their `slack_posted` key:
    # an entry that carries `slack_posted` was created by the Slack-era
    # `update` path, so a never-posted one (Weinbrand-style: digest failed,
    # `slack_posted: False`) is still owed a post and counts as pending; an
    # entry with no `slack_posted` key at all is pre-Slack bootstrap backlog
    # and must stay excluded so deploying this feature does not flood #toread.
    if post_to_slack:
        for paper in papers:
            entry = state["papers"].get(paper.id)
            if entry is None or entry.get("slack_posted"):
                continue
            # In "team" scope only team Slack submissions are announced —
            # see the queueing comment above. This also guards any backlog
            # queued under a wider scope, so flipping the config does not
            # flood #toread.
            if digest_scope == "team" and not paper.is_team_submission:
                continue
            # Hold for the research-radio episode (or the fallback deadline)
            # when an episode wait is configured.
            if (episode_wait_days > 0 and paper.id not in episodes
                    and not _slack_wait_expired(entry, episode_wait_days)):
                continue
            pending = entry.get("slack_pending")
            if pending is None:
                pending = "slack_posted" in entry  # Slack-era, never posted
            if not pending:
                continue
            summary = summaries.get(paper.bibtex_key) or summarizer.load_summary(
                summaries_dir, paper.bibtex_key
            )
            if summary is None:
                print(f"  slack: no summary for {paper.bibtex_key}, skipping")
                continue
            try:
                ep = episodes.get(paper.id) or {}
                posted = slack_client.post_paper(
                    os.environ["SLACK_WEBHOOK_URL"], paper, summary,
                    entry["topics"], ep.get("audio_url"),
                    _note_url(cfg, paper.bibtex_key), ep.get("apple_url"),
                )
            except Exception as exc:  # noqa: BLE001 - Slack must never break the build
                posted = False
                print(f"  slack: unexpected error for {paper.bibtex_key} ({exc})")
            if posted:
                entry["slack_posted"] = True
                entry.pop("slack_pending", None)
                # Persist immediately: if a later paper crashes the run before
                # the save_state at the end, this one must not be re-posted on
                # the next cron retry.
                state_mod.save_state(state, _abs(cfg["paths"]["state_file"]))
                print(f"  slack: posted {paper.bibtex_key} to #toread")
                time.sleep(0.5)  # incoming-webhook rate limit is ~1/s

    # --- Own publications -------------------------------------------------
    # Fabio's own papers (from fabiogiglietto.github.io), processed as a
    # second source: vault notes only, never a Slack digest (they are not a
    # reading list). Eligible papers are recent or well-cited; a per-run cap
    # keeps the first backfill from being a cost spike.
    own_cfg = cfg.get("own_publications", {})
    own_new, own_changed = [], []
    if own_cfg.get("enabled", True):
        try:
            own_papers = feed_client.fetch_own_publications(
                cfg["inputs"]["own_publications_url"]
            )
        except Exception as exc:  # noqa: BLE001 - a second source must never break the run
            own_papers = []
            print(f"update: could not fetch own-publications feed ({exc})")

        min_year = own_cfg.get("min_year", 2020)
        min_citations = own_cfg.get("min_citations", 5)
        for paper in own_papers:
            if not feed_client.is_note_eligible(paper, min_year, min_citations):
                continue
            podcast = paper.id in episodes
            new_hash = state_mod.content_hash(paper.abstract, podcast)
            entry = state["papers"].get(paper.id)
            if entry is None:
                own_new.append(paper)
            elif entry.get("content_hash") != new_hash:
                own_changed.append(paper)

        # Cap only new papers (each costs a Claude summary); changed papers are
        # cheap re-renders and are always processed. The feed is newest-first,
        # so deferred new papers are the older ones — picked up on later runs.
        max_per_run = own_cfg.get("max_per_run", 10)
        if len(own_new) > max_per_run:
            deferred = len(own_new) - max_per_run
            own_new = own_new[:max_per_run]
            print(f"update: own-papers backfill capped at {max_per_run} "
                  f"({deferred} deferred to later runs)")
    print(f"update: {len(own_new)} new, {len(own_changed)} changed own paper(s)")

    # New own papers: summarize (abstract-only unless a Drive PDF matches),
    # assign topics, create state. No Slack post — see comment above.
    for paper in own_new:
        summary = summarizer.load_summary(summaries_dir, paper.bibtex_key)
        if summary is None:
            text = _pdf_text(cfg, drive, paper)
            summary = summarizer.summarize_paper(
                paper, text, claude, claude.summary_model
            )
            summarizer.save_summary(summary, summaries_dir, paper.bibtex_key)
        summaries[paper.bibtex_key] = summary
        slugs = themes.assign_paper(
            paper, summary, register, claude, claude.assign_model
        )
        podcast = paper.id in episodes
        state["papers"][paper.id] = {
            "note_path": f"{papers_dir}/{paper.bibtex_key}.md",
            "topics": slugs,
            "assign_fp": state_mod.assign_fingerprint(
                reg_fp, themes.summary_digest(summary), claude.assign_model
            ),
            "kind": "own",
            "doi": paper.doi or "",
            "title": paper.title,
            "pdf_source": summary["pdf_source"],
            "content_hash": state_mod.content_hash(paper.abstract, podcast),
            "podcast_linked": podcast,
            "last_processed": _now(),
        }

    # Changed own papers: refresh the state hash (e.g. a podcast episode appeared).
    for paper in own_changed:
        podcast = paper.id in episodes
        entry = state["papers"][paper.id]
        entry["podcast_linked"] = podcast
        entry["content_hash"] = state_mod.content_hash(paper.abstract, podcast)
        entry["last_processed"] = _now()

    # Re-render the note for every new or changed own paper (frontmatter kind: own).
    own_touched = own_new + own_changed
    for paper in own_touched:
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
            episodes.get(paper.id), claude, claude.note_model, kind="own",
        )
        note_builder.write_note(vault, papers_dir, paper.bibtex_key, note)

    # Own papers are deliberately *not* counted toward papers_since_cluster:
    # the capped backfill would otherwise trigger reclusters mid-drain. They
    # still get an initial topic assignment above and are folded into the
    # structure on the weekly Monday recluster.
    state["papers_since_cluster"] = (
        state.get("papers_since_cluster", 0) + len(new_papers)
    )
    if touched or own_touched:
        _regenerate_topic_notes(cfg, register, state)

    threshold = cfg["processing"]["recluster_threshold"]
    do_recluster = args.recluster or state["papers_since_cluster"] >= threshold
    state_mod.save_state(state, _abs(cfg["paths"]["state_file"]))

    if not touched and not own_touched and not do_recluster:
        print("update: nothing to do")
        return 0

    if do_recluster:
        _recluster(cfg, claude, drive, force=getattr(args, "full", False))

    sanitised = _sanitize_vault_links(cfg)
    print(
        f"  link sanitiser: {len(sanitised['repaired'])} repaired, "
        f"{len(sanitised['delinked'])} de-linked"
    )
    print("update: done")
    return 0


def _recluster(cfg: dict, claude, drive, force: bool = False) -> None:
    """Full re-cluster: rebuild the register, re-assign every processed paper,
    regenerate Topics/ and Structures/. Paper note bodies are not re-summarised
    (cost) — only their frontmatter `topics:` is updated in place.

    With `processing.incremental_recluster` on, the register maintained by
    `refresh-topics` is reused (no second synthesis) and per-paper assignment,
    emergent clustering, and structure notes are skipped when their input
    fingerprints are unchanged. `force=True` (--full) re-bills everything."""
    from . import feed_client, topics_client, summarizer, themes, state as state_mod

    incremental = cfg.get("processing", {}).get("incremental_recluster", False)
    print("recluster: rebuilding the register and re-clustering the archive")
    if incremental:
        # Reuse the register refresh-topics maintains — on Mondays it ran
        # minutes earlier in the same workflow, so synthesizing again here
        # would re-bill identical inputs. Includes carried emergent topics,
        # so papers can be filed directly into established emergent topics.
        register = topics_client.load_topics(_abs(cfg["paths"]["topics_file"]))
        if not register:
            register = _build_register(cfg, claude)
    else:
        register = _build_register(cfg, claude)
    state = state_mod.load_state(_abs(cfg["paths"]["state_file"]))
    summaries_dir = _abs(cfg["paths"]["summaries_dir"])

    papers = [
        p for p in feed_client.fetch_feed(cfg["inputs"]["feed_url"])
        if p.id in state["papers"]
    ]
    # Own publications already in state are reclustered alongside toread papers,
    # so the weekly recluster folds them into the topic structure too.
    own_cfg = cfg.get("own_publications", {})
    if own_cfg.get("enabled", True):
        try:
            own = feed_client.fetch_own_publications(
                cfg["inputs"]["own_publications_url"]
            )
            papers += [p for p in own if p.id in state["papers"]]
        except Exception as exc:  # noqa: BLE001 - never break recluster on a fetch error
            print(f"recluster: could not fetch own-publications feed ({exc})")
    summaries: dict[str, dict] = {}
    for paper in papers:
        s = summarizer.load_summary(summaries_dir, paper.bibtex_key)
        if s is not None:
            summaries[paper.bibtex_key] = s

    reg_fp = state_mod.register_fingerprint(register)
    unassigned = []
    assigned = skipped = 0
    for paper in papers:
        summary = summaries.get(paper.bibtex_key)
        if summary is None:
            continue
        entry = state["papers"][paper.id]
        fp = state_mod.assign_fingerprint(
            reg_fp, themes.summary_digest(summary), claude.assign_model
        )
        if incremental and not force and entry.get("assign_fp") == fp:
            slugs = entry.get("topics", [])
            skipped += 1
        else:
            slugs = themes.assign_paper(
                paper, summary, register, claude, claude.assign_model
            )
            entry["topics"] = slugs
            entry["assign_fp"] = fp
            assigned += 1
        if not slugs:
            unassigned.append(paper)
    print(f"recluster: {assigned} assigned, {skipped} skipped (unchanged inputs)")

    emergent_fp = state_mod.emergent_fingerprint(
        reg_fp, [p.bibtex_key for p in unassigned], claude.reasoning_model
    )
    if incremental and not force and state.get("emergent_fp") == emergent_fp:
        # Same register + same unassigned set as last time — re-running the
        # clustering call would reproduce the same (non-)finding.
        print(f"recluster: emergent clustering skipped "
              f"({len(unassigned)} unassigned, inputs unchanged)")
        emergent = []
    else:
        emergent = themes.find_emergent(
            unassigned, summaries, claude, claude.reasoning_model,
            cfg["topics"]["emergent_min_papers"],
        )
        state["emergent_fp"] = emergent_fp
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

    if incremental:
        # The reused register carries emergent topics over; a reassignment can
        # empty one out — prune register entries no paper references any more.
        live = {s for e in state["papers"].values() for s in e.get("topics", [])}
        empty = [t["slug"] for t in register
                 if t.get("is_emergent") and t["slug"] not in live]
        if empty:
            register = [t for t in register if t["slug"] not in empty]
            print(f"recluster: pruned {len(empty)} empty emergent topic(s)")

    topics_client.save_topics(register, _abs(cfg["paths"]["topics_file"]))

    # Checkpoint: the assignment/emergent fingerprints just seeded are the
    # expensive part of this run — persist them now so a transient failure in
    # the structure-note pass below doesn't throw them away (a re-run would
    # otherwise re-bill every assignment call).
    state_mod.save_state(state, _abs(cfg["paths"]["state_file"]))

    # Update each paper note's frontmatter topics in place (no re-summary).
    vault = Path(_abs(cfg["vault"]["path"]))
    for paper in papers:
        entry = state["papers"][paper.id]
        _rewrite_note_topics(str(vault / entry["note_path"]), entry["topics"])

    _regenerate_topic_notes(cfg, register, state)
    papers_by_key = {p.bibtex_key: p for p in papers}
    _generate_structure_notes(
        cfg, register, state, papers_by_key, summaries, claude, force=force
    )

    state["last_full_cluster"] = _now()
    state["papers_since_cluster"] = 0
    state_mod.save_state(state, _abs(cfg["paths"]["state_file"]))
    print(f"recluster: {len(register)} topics, {len(emergent)} emergent")


def cmd_recluster(cfg: dict, args) -> int:
    """Force a full re-cluster of the whole archive."""
    args.recluster = True
    return cmd_update(cfg, args)


def cmd_fix_links(cfg: dict, args) -> int:
    """Repair / de-link unresolved [[wikilinks]] across the vault."""
    result = _sanitize_vault_links(cfg, verbose=True)
    print(
        f"fix-links: {result['notes_changed']} note(s) updated — "
        f"{len(result['repaired'])} target(s) repaired, "
        f"{len(result['delinked'])} de-linked"
    )
    for old, new in sorted(result["repaired"].items()):
        print(f"  repaired:  {old} -> {new}")
    for target in result["delinked"]:
        print(f"  de-linked: {target}")
    return 0


def cmd_export_site(cfg: dict, args) -> int:
    """Export the vault to quartz/content/ for the public Quartz website."""
    from . import site_export, topics_client, state as state_mod

    vault = cfg["vault"]
    vault_dir = Path(_abs(vault["path"]))
    subdirs = [vault["papers_dir"], vault["topics_dir"], vault["structures_dir"]]
    content_dir = ROOT / "quartz" / "content"

    topics = topics_client.load_topics(_abs(cfg["paths"]["topics_file"]))
    state = state_mod.load_state(_abs(cfg["paths"]["state_file"]))

    site_title = cfg.get("vault", {}).get("site_title", "fg-zettelkasten")
    stats = site_export.export_site(vault_dir, content_dir, subdirs, topics,
                                    state, site_title=site_title)
    print(
        f"export-site: {stats['notes']} note(s) -> "
        f"{content_dir.relative_to(ROOT)} "
        f"({stats['stripped']} with dataview blocks stripped)"
    )
    return 0


def cmd_slack_test(cfg: dict, args) -> int:
    """Post one paper's digest to Slack — verify Block Kit rendering / re-post."""
    from . import (
        feed_client, episodes_client, summarizer, slack_client,
        state as state_mod,
    )

    webhook = os.environ.get("SLACK_WEBHOOK_URL")
    if not webhook:
        print("slack-test: SLACK_WEBHOOK_URL is not set")
        return 1

    key = args.bibtex_key
    papers = feed_client.fetch_feed(cfg["inputs"]["feed_url"])
    paper = next((p for p in papers if p.bibtex_key == key), None)
    if paper is None:
        print(f"slack-test: no paper with bibtex key {key!r} in the feed")
        return 1

    summary = summarizer.load_summary(_abs(cfg["paths"]["summaries_dir"]), key)
    if summary is None:
        print(f"slack-test: no cached summary for {key} — run `update` first")
        return 1

    state = state_mod.load_state(_abs(cfg["paths"]["state_file"]))
    topics = state["papers"].get(paper.id, {}).get("topics", [])
    episodes = episodes_client.fetch_episodes(cfg["inputs"]["episodes_url"])

    ep = episodes.get(paper.id) or {}
    ok = slack_client.post_paper(
        webhook, paper, summary, topics, ep.get("audio_url"),
        _note_url(cfg, key), ep.get("apple_url"),
    )
    print(f"slack-test: {'posted' if ok else 'FAILED'} {key} to the webhook")
    return 0 if ok else 1


# --- CLI ------------------------------------------------------------------


def build_parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(prog="fg-zettelkasten", description=__doc__)
    parser.add_argument("--config", default="config.yml", help="path to config.yml")
    sub = parser.add_subparsers(dest="command", required=True)

    p_bootstrap = sub.add_parser("bootstrap", help="process the whole archive (run once)")
    p_bootstrap.add_argument(
        "--limit", type=int, default=None, help="process only the first N papers"
    )

    sub.add_parser(
        "summarize", help="pipeline stage 1: summarize new papers, then stop"
    )

    p_update = sub.add_parser("update", help="incremental daily run")
    p_update.add_argument(
        "--recluster", action="store_true", help="also run a full re-cluster"
    )
    p_update.add_argument(
        "--full", action="store_true",
        help="with --recluster: ignore fingerprints and re-bill every call",
    )

    sub.add_parser("refresh-topics", help="rebuild the topic register from github.io")
    p_recluster = sub.add_parser("recluster", help="force a full re-cluster")
    p_recluster.add_argument(
        "--full", action="store_true",
        help="ignore fingerprints and re-bill every call",
    )
    sub.add_parser("fix-links", help="repair/de-link unresolved [[wikilinks]] in the vault")
    sub.add_parser("export-site", help="export the vault to quartz/content/ for the website")

    p_slack = sub.add_parser(
        "slack-test", help="post one paper's digest to the Slack webhook"
    )
    p_slack.add_argument("bibtex_key", help="bibtex key of a paper already processed")
    return parser


def main(argv=None) -> int:
    args = build_parser().parse_args(argv)
    cfg = load_config(args.config)

    commands = {
        "bootstrap": cmd_bootstrap,
        "summarize": cmd_summarize,
        "update": cmd_update,
        "refresh-topics": cmd_refresh_topics,
        "recluster": cmd_recluster,
        "fix-links": cmd_fix_links,
        "export-site": cmd_export_site,
        "slack-test": cmd_slack_test,
    }
    return commands[args.command](cfg, args) or 0


if __name__ == "__main__":
    sys.exit(main())
