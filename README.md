# fg-zettelkasten

An Obsidian knowledge base that turns the
[toread](https://github.com/fabiogiglietto/toread) academic-paper feed into a
densely interconnected Zettelkasten, modelled on the
[Niklas Luhmann Archive](https://niklas-luhmann-archiv.de/).

Each paper becomes a richly-described note. Notes are organised under a **topic
register** synthesized from the maintainer's live research agenda
(`fabiogiglietto.github.io`), cross-linked into a navigable web, and linked to
the matching [research-radio](https://github.com/fabiogiglietto/research-radio)
podcast episode when one exists.

A second source feeds the vault: the maintainer's **own publications**, taken
from `fabiogiglietto.github.io`'s `own-publications.json`. These get notes
tagged `kind: own` — built from the paper's green open-access PDF, for recent
or well-cited papers only — but are never posted to the `#toread` Slack digest:
they are not a reading list.

## Pipeline

```
Paperpile -> toread (metadata enrichment) -> feed.json
fabiogiglietto.github.io -> research agenda + own-publications.json
        |
        v
fg-zettelkasten (Claude: topic register + full-PDF summaries + notes)
   |- vault/           Obsidian vault
   '- data/summaries/  shared structured summaries (consumed later by research-radio)
```

All projects join papers on the `bibtex:AuthorYear-xx` id.

## Setup

```bash
python -m venv venv && source venv/bin/activate
pip install -r requirements.txt
cp .env.example .env        # then fill in the keys
```

`.env` needs `ANTHROPIC_API_KEY`, `GOOGLE_APPLICATION_CREDENTIALS` (path to a
Google service-account JSON with read access to Paperpile's Drive folder — the
same account research-radio uses) and `GOOGLE_DRIVE_FOLDER_ID`.

## Usage

```bash
python -m src.main refresh-topics       # build the topic register from github.io
python -m src.main bootstrap            # process the whole archive (run once)
python -m src.main bootstrap --limit 5  # smoke test on the first 5 papers
python -m src.main update               # daily incremental run
python -m src.main update --recluster   # incremental + full re-cluster
```

## Vault layout

- `vault/Papers/`     — one note per paper, filename = bibtex key
- `vault/Topics/`     — register entry notes (the *Schlagwortregister*)
- `vault/Structures/` — hub notes narrating an argument across papers in a topic

Open `vault/` as an Obsidian vault. `data/` (state, topics, summaries) and
`vault/` are committed; extracted PDF text is transient and never committed.

## Status

Scaffold. Data-fetching modules are implemented; LLM-driven steps
(`topics_client.synthesize_register`, `summarizer.summarize_paper`,
`themes.*`, `note_builder.build_paper_note` / `build_structure_note`, the
`claude_client` SDK calls, and the `main.py` command bodies) are stubbed with
`NotImplementedError` and pointers to the implementation plan.
