"""Build the topic register — the Luhmann *Schlagwortregister* — from the user's
research agenda published on fabiogiglietto.github.io.

Signals are fetched live from the published repo, never the local working copy.
"""
from __future__ import annotations

import json
from pathlib import Path

import requests


def fetch_signals(
    base_url: str, signal_paths: list[str], timeout: int = 30
) -> dict[str, str]:
    """Fetch each research-agenda signal file; return {path: raw_text}.

    A missing signal is skipped with a warning rather than failing the run.
    """
    signals: dict[str, str] = {}
    for rel in signal_paths:
        url = f"{base_url.rstrip('/')}/{rel}"
        try:
            resp = requests.get(url, timeout=timeout)
            resp.raise_for_status()
            signals[rel] = resp.text
        except requests.RequestException as exc:
            print(f"WARN: could not fetch {url}: {exc}")
    return signals


_SYNTHESIS_SYSTEM = """\
You are a research librarian curating a Zettelkasten topic register — the \
Schlagwortregister of a Niklas-Luhmann-style archive. From a researcher's \
published agenda you distil a small, stable taxonomy of working topics that a \
stream of academic papers will be filed under.

Rules:
- Produce a curated taxonomy, not an exhaustive index. Each topic must be a \
genuine working theme, broad enough to gather many papers yet specific enough \
to be meaningful.
- Weight strongly toward the *current* agenda: projects with `status: Active`, \
recent news, and recent publications outweigh the full historical record.
- Topic slugs are lowercase, hyphenated, stable identifiers (e.g. \
`information-disorder`). Names are short Title Case phrases. Descriptions are \
one or two sentences explaining what the topic covers and why it matters to \
this researcher.
- `source_signals` lists the signal filenames that motivated the topic.
- Output ONLY a JSON array, no prose or markdown fences. Each element:
  {"slug": ..., "name": ..., "description": ..., "source_signals": [...]}
"""


def synthesize_register(
    signals: dict[str, str], claude, topics_cfg: dict
) -> list[dict]:
    """Use Claude to synthesize the signals into the topic register.

    Produces `min_topics`..`max_topics` working topics. The prompt weights
    toward the *current* agenda — `status: Active` projects, recent news and
    publications — not the full historical record in publications.yml.

    Returns a list of dicts:
        {slug, name, description, source_signals, is_emergent: false}
    """
    min_topics = topics_cfg.get("min_topics", 6)
    max_topics = topics_cfg.get("max_topics", 12)

    parts = [
        f"Produce between {min_topics} and {max_topics} working topics.",
        "",
        "Research-agenda signals follow, each delimited by its filename:",
    ]
    for path, text in signals.items():
        parts.append(f"\n===== {path} =====\n{text.strip()}")
    prompt = "\n".join(parts)

    topics = claude.complete_json(
        model=claude.reasoning_model,
        system=_SYNTHESIS_SYSTEM,
        prompt=prompt,
        max_tokens=8192,
    )

    register: list[dict] = []
    for topic in topics:
        register.append(
            {
                "slug": topic["slug"],
                "name": topic["name"],
                "description": topic.get("description", ""),
                "source_signals": topic.get("source_signals", []),
                "is_emergent": False,
            }
        )
    return register


def load_topics(path: str) -> list[dict]:
    p = Path(path)
    return json.loads(p.read_text()) if p.exists() else []


def save_topics(topics: list[dict], path: str) -> None:
    p = Path(path)
    p.parent.mkdir(parents=True, exist_ok=True)
    p.write_text(json.dumps(topics, indent=2, ensure_ascii=False))
