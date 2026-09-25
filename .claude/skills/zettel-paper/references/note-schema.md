# Note schema and conventions

The exact shapes the indexer relies on. Read this when parsing notes by hand,
debugging the index, or extending the skill. All repos in the upstream pipeline
join papers on the `bibtex_key` id.

## Repo layout (after `git clone --depth 1`)

```
fg-zettelkasten/
├── vault/
│   ├── Papers/      <bibtex_key>.md      (~230 literature notes)
│   ├── Topics/      <slug>.md            (16 keyword registers)
│   └── Structures/  <slug>.md            (16 argument threads)
├── data/
│   ├── summaries/   <bibtex_key>.json    (structured per-paper summary)
│   ├── topics.json  (list of topic objects)
│   └── state.json
└── src/, scripts/   (the upstream Python pipeline — do NOT touch)
```

The skill is a **read-only downstream consumer** of `vault/` and `data/`. It never
runs `src/main` or alters ingestion/clustering.

## Paper note frontmatter (`vault/Papers/<id>.md`)

```yaml
title: "Attributing coordinated social media manipulation: ..."
aliases: ["..."]
authors: ["Daniel Thiele", "Miriam Milzner", "Annett Heft", ...]
year: 2025
doi: 10.1177/14614448251350100
bibtex_key: Thiele2025-ol
topics: [coordinated-inauthentic-behavior, information-disorder]   # ← topic membership
citation_count: 4
open_access: false
source_url: https://doi.org/...
podcast_url: https://github.com/.../Thiele2025-ol.mp3
pdf_available: true
discovery_date: 2025-07-15T00:00:00Z
```

Body sections (markdown `##`): **Summary**, **Key Contributions**, **Methods**,
**Findings**, **Connections**, **Podcast**. The `## Connections` paragraph is
prose containing `[[bibtex_key]]` wikilinks to sibling papers — this is the edge
list. Build citations from `authors` + `year` + `doi`; there is **no .bib file**.

A retracted paper keeps its note but gains two frontmatter fields and a
`> [!warning] Retracted` callout under the H1; its `topics` is `[]`:

```yaml
retracted: 2026-05-07
retraction_notice: 10.1093/pnasnexus/pgag137   # DOI of the retraction notice
```

The indexer skips these notes and every link into them; they appear only in
`index.json` → `do_not_cite`.

A paper with a non-retracting notice stays in the index, flagged:

```yaml
editorial_notices: [expression_of_concern, correction]   # carried into index.json
```

with a `> [!caution] Editorial notices` callout under the H1 listing each
notice's type, date and DOI.

## Wikilink syntax

`[[Thiele2025-ol]]`, optionally `[[id|alias]]` or `[[id#section]]`. The indexer's
regex captures the id before any `|` or `#`. ~1,419 links across the Papers.

## Two id formats

- `AuthorYear-xx` (two-letter suffix, e.g. `Thiele2025-ol`) — papers from the
  `toread` feed.
- `AuthorYear-<hash>` (e.g. `Giglietto2020-9d8acdd7`) — the author's **own**
  publications, joined from a separate feed. Treat identically; they resolve to
  real notes in `vault/Papers` and tend to score high as bridges.

## Structured summary (`data/summaries/<id>.json`)

Cleaner than parsing the markdown body; prefer it when present.

```json
{
  "abstract":      "…",
  "key_claims":    ["…", "…"],
  "methods":       "…",
  "findings":      ["…"]  or  "…",
  "contributions": ["…"],
  "framing":       "…",
  "pdf_source":    "…"
}
```

The indexer loads this by `bibtex_key` then by filename stem, and folds the first
five `key_claims` into `index.json`. The fuller `abstract`/`methods`/`findings`
are read on demand at drafting time, not bundled.

The summary is the user's condensed reading, not the paper itself. When a draft
needs the primary source, the full-text PDF is reachable via Google Drive on
explicit request — see `fulltext-access.md`.

## Topic register (`vault/Topics/<slug>.md`)

```yaml
type: topic
slug: coordinated-inauthentic-behavior
emergent: false
```

Body: a one-paragraph description, then `## Papers` as a list of `[[links]]`.
**Don't derive membership from this list** — derive it from each paper's
`topics[]` frontmatter (authoritative, used by the indexer). `data/topics.json`
supplies each topic's `name` and `description`.

## Structure thread (`vault/Structures/<slug>.md`)

```yaml
type: structure
slug: coordinated-inauthentic-behavior
topic: "Coordinated Inauthentic Behavior"
```

Body: a titled overview paragraph, then `##` sub-threads, each a prose argument
citing papers via `[[links]]` in a deliberate order. This is the *Folgezettel* —
read it whole for Move 1.

## Gotchas

- Titles may contain escaped quotes; the CSV writer escapes them per RFC 4180 —
  `read_csv`/`read.csv` parse them correctly even when raw `cat` looks doubled.
- A `[[link]]` can point at a note not in `vault/Papers` (rare). The indexer flags
  these as dangling (`target_in_vault=0` in `edges.csv`) and excludes them from
  crossings. Never cite a dangling target.
- `findings`/`contributions` are sometimes a string, sometimes a list — handle both.
