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
import sys
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


# --- commands -------------------------------------------------------------
# Each command is a thin orchestrator over src/* modules. The data-fetching
# pieces are implemented; the LLM-driven steps raise NotImplementedError with a
# pointer to the relevant plan section.


def cmd_refresh_topics(cfg: dict, args) -> int:
    """Rebuild the topic register from the live github.io research-agenda signals."""
    # TODO (plan §"Topic register"):
    #   from . import topics_client, note_builder
    #   signals  = topics_client.fetch_signals(cfg["inputs"]["github_io_base"],
    #                                          cfg["inputs"]["github_io_signals"])
    #   register = topics_client.synthesize_register(signals, _claude(cfg), cfg["topics"])
    #   topics_client.save_topics(register, cfg["paths"]["topics_file"])
    #   regenerate vault/Topics/*.md via note_builder.build_topic_note
    raise NotImplementedError("refresh-topics — see plan §'Topic register'")


def cmd_bootstrap(cfg: dict, args) -> int:
    """Process the whole archive: register, per-paper notes, themes, hub notes."""
    # TODO (plan §"bootstrap"): refresh topics -> per-paper summarize+note ->
    #   topic-anchored assignment -> regenerate Topics/ and Structures/.
    raise NotImplementedError("bootstrap — see plan §'bootstrap'")


def cmd_update(cfg: dict, args) -> int:
    """Daily incremental run: new/changed papers only."""
    # TODO (plan §"update"): diff feed vs state by id and content_hash ->
    #   summarize+note new papers -> assign to existing topics ->
    #   regenerate Topics/ ; if args.recluster, full recluster.
    raise NotImplementedError("update — see plan §'update'")


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
