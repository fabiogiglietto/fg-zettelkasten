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
    # TODO: build the synthesis prompt from `signals`; call
    #       claude.complete_json(model=claude.reasoning_model, ...).
    raise NotImplementedError("topics_client.synthesize_register")


def load_topics(path: str) -> list[dict]:
    p = Path(path)
    return json.loads(p.read_text()) if p.exists() else []


def save_topics(topics: list[dict], path: str) -> None:
    p = Path(path)
    p.parent.mkdir(parents=True, exist_ok=True)
    p.write_text(json.dumps(topics, indent=2, ensure_ascii=False))
