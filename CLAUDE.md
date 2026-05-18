# CLAUDE.md

Guidance for Claude Code when working in this repository.

## Project

fg-zettelkasten builds an Obsidian Zettelkasten from the `toread` paper feed.
It is the **most downstream** stage of a four-repo pipeline and consumes the
published artifacts of all three upstream repos: the `toread` feed, the
`research-radio` episodes, and topic signals from `fabiogiglietto.github.io`.
All repos join papers on the `bibtex:AuthorYear-xx` id.

Full DAG and orchestration model:
https://github.com/fabiogiglietto/toread/blob/main/PIPELINE.md

## Commands

```bash
source venv/bin/activate
pip install -r requirements.txt
python -m src.main refresh-topics      # rebuild the topic register from github.io
python -m src.main bootstrap [--limit N]
python -m src.main update [--recluster]
```

## Architecture

- `src/feed_client.py`     — fetch the toread feed + the own-publications feed -> `Paper` objects
- `src/episodes_client.py` — fetch research-radio episodes -> {id: audio_url}
- `src/topics_client.py`   — synthesize the topic register from github.io signals
- `src/drive_client.py`    — fetch + extract PDF text from Paperpile's Drive folder
                             (ported verbatim from research-radio)
- `src/claude_client.py`   — Anthropic SDK wrapper; Claude does all LLM work
- `src/summarizer.py`      — full PDF -> structured summary (shared artifact)
- `src/themes.py`          — topic-anchored assignment + emergent sub-themes
- `src/note_builder.py`    — render Papers/, Topics/, Structures/ markdown
- `src/state.py`           — data/state.json persistence

## Conventions

- LLM provider split: Claude for all comprehension/writing. Gemini stays only in
  research-radio for TTS — never add a non-Claude LLM here.
- Paper note filename = bibtex key (stable wikilinks); readable title in `aliases`.
- `vault/` and `data/` (state, topics, summaries) are committed. Extracted PDF
  full text is transient (`data/.cache/`, gitignored) — never commit it.
- Topic register notes are deterministic templating; structure/hub notes are
  LLM-written and regenerate only on bootstrap/recluster.
- Own publications (Fabio's own papers, from github.io's `own-publications.json`)
  are a second source in `update`: notes tagged `kind: own`, never posted to the
  `#toread` Slack digest, and gated by the `own_publications` config block
  (a note is built only for recent or well-cited papers; backfill is capped).
- Derived notes (Topics/, Structures/) are regenerated, never appended to.
- Inputs are fetched live from published URLs, never local sibling working copies.
- Run as a module: `python -m src.main`. `src/` modules use relative imports.

## Style

- Python, standard library + the deps in `requirements.txt`. Keep it tidy.
- Match the existing module docstring + type-hint style when adding code.
