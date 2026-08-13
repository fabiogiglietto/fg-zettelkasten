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
python -m src.main export-site         # export vault/ -> quartz/content/ for the website
python -m src.main dedupe-vault        # report notes that are the same work (--apply to merge)
python -m src.main check-published     # ask OpenAlex if a preprint note is now published
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
- `src/supersede.py`       — decide when two records are the same work; tombstone merge
- `src/openalex_client.py` — look up whether a preprint has since been published
- `src/note_builder.py`    — render Papers/, Topics/, Structures/ markdown
- `src/site_export.py`     — export the vault to `quartz/content/` for the website
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
  `#toread` Slack digest, gated by the `own_publications` config block. A note
  is built only for a paper that has a green-OA PDF (`open_access_pdf_url`,
  resolved from ORA) *and* is recent or well-cited; the PDF is its summary
  source (`pdf_fetcher.py`). Backfill is capped per run.
- Working paper -> published version: a paper re-added in published form under a
  new bibtex key is merged into that key. The published note gets `supersedes:`;
  the working-paper note is replaced by a stub carrying `superseded_by:` and
  `topics: []` — the file stays so inbound `[[wikilinks]]` and the live site URL
  keep resolving, but it leaves the Topics registers. Direction is decided by
  publication status, never arrival order, so a preprint added *after* the
  journal version is itself tombstoned. A cheap prefilter (title / author-token /
  abstract-jaccard) proposes pairs; Claude decides, and only an unhedged yes is
  applied. Verdicts — including negatives — are cached in
  `state["supersede_decisions"]` so a rejected pair is never re-billed.
  `check-published` covers papers published without anyone re-adding them: those
  have no upstream bibtex key, so the note is upgraded *in place* (new DOI,
  `preprint_doi` kept, `published_venue` recorded) rather than replaced — never
  mint bibtex keys locally, `toread` owns that namespace.
- Derived notes (Topics/, Structures/) are regenerated, never appended to.
- Inputs are fetched live from published URLs, never local sibling working copies.
- Run as a module: `python -m src.main`. `src/` modules use relative imports.
- Website: `quartz/` vendors Quartz v4 (Node 22+) to publish the vault to GitHub
  Pages. `export-site` regenerates `quartz/content/` from `vault/` — deterministic,
  no LLM, never modifies the vault. Generated dirs (`quartz/content/`,
  `quartz/public/`) are gitignored; the build + deploy run in `update-vault.yml`.
  `quartz/util/glob.ts` carries one vendored edit (`gitignore: false`) — re-apply
  it on Quartz upgrades.

## Style

- Python, standard library + the deps in `requirements.txt`. Keep it tidy.
- Match the existing module docstring + type-hint style when adding code.
\nuse fable subagents when you need more intelligence
