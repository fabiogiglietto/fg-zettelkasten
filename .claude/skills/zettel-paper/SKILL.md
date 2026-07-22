---
name: zettel-paper
description: >-
  Draft new academic papers, literature reviews, conceptual syntheses, and
  research-agenda pieces FROM Fabio Giglietto's fg-zettelkasten
  (github.com/fabiogiglietto/fg-zettelkasten) — a topic-anchored Zettelkasten of
  ~230 paper notes, 16 topic registers, and 16 pre-written argument "Structures."
  Use this skill WHENEVER the user wants to write, draft, outline, or assemble a
  paper, literature review, synthesis, framing piece, or argument from their
  zettelkasten, their notes, their "kasten," the toread feed, or "from my notes"
  in the Luhmann sense — even if they don't say the word "skill." Also trigger
  when the user names a topic or Structure (e.g. "coordinated inauthentic
  behavior," "platform governance") and asks to turn it into prose, or asks what
  non-obvious paper they could write from the corpus. The skill clones the kasten
  fresh, builds a citation graph, and drafts with real, traceable citations only.
---

# zettel-paper

Write new scholarship from the fg-zettelkasten the way Luhmann described writing
from his slip-box: not by summarising notes, but by **pulling a thread of linked
notes whose sequence already contains an argument**, then turning that thread
into prose. The box removes the blank page; the human stays the author.

This kasten is unusually well-suited to that because it separates three jobs:

- **Papers** (`vault/Papers/*.md`, ~230) — one atomic literature note per source,
  each carrying a real citation (`authors`, `year`, `doi`, `bibtex_key`) and a
  `## Connections` section of `[[bibtex_key]]` wikilinks. These are the citable
  bricks.
- **Topics** (`vault/Topics/*.md`, 16) — *Schlagwortregister*: keyword registers
  listing every paper under a theme. Entry points, not arguments.
- **Structures** (`vault/Structures/*.md`, 16) — pre-written argument threads that
  already weave papers into a narrative with sub-threads and inline `[[links]]`.
  These are *Folgezettel*: the spine of a paper, waiting to be expanded.

## Step 1 — get the corpus and index it

Always work from a **fresh clone** (the kasten updates from an upstream feed).
Run the bundled indexer; it clones (or pulls) and writes a flat, R-friendly map.

```bash
python3 scripts/index_kasten.py --out-dir kasten_index
# already have a local clone? point at it instead:
python3 scripts/index_kasten.py --vault-path /path/to/fg-zettelkasten --skip-clone
```

Pure standard library — no installs needed. It writes `kasten_index/`:

| file | what it's for |
|------|----------------|
| `index.json` | one bundled object — **read this first** to plan; has every paper's title/authors/year/doi/topics/key_claims + graph metrics, plus `citation_label`/`first_author_surname`/`name_order_uncertain` for correct author–year citing |
| `papers.csv` | node table (→ igraph vertices) |
| `edges.csv` | `[[link]]` graph with a `cross_topic` flag (→ igraph edges) |
| `topics.csv` | the 16 registers + paper counts + descriptions |
| `structures.csv` | the pre-written threads (`slug`, `topic`, `path`) |
| `bridges.csv` | papers ranked by `bridge_score` — **fuel for mode 2** |
| `crossings.csv` | linked paper *pairs that share no topic* — the literal "surprising connection" list |

The CSVs are deliberately flat so the analysis layer is yours in R:

```r
library(igraph); library(readr)
nodes <- read_csv("kasten_index/papers.csv")
edges <- read_csv("kasten_index/edges.csv")
g <- graph_from_data_frame(edges, vertices = nodes, directed = TRUE)
```

## Step 2 — choose the generative entry point

Pick the mode from what the user asked. When unclear, ask which they want; the
default for "write me something from the kasten" is **mode 1** on the Structure
they name, or — if they want novelty — **mode 2**. See
`references/luhmann-method.md` for the moves in depth.

**Mode 1 · Follow a Structure** (highest fidelity). The user names a topic/thread,
or wants a solid review. Read the Structure markdown end to end — it is already
the argument. Expand each sub-thread into prose, pulling detail from the Paper
notes it cites. Lowest invention risk.

**Mode 2 · Cross the registers** (balanced novelty — the serendipity engine).
The user wants a *new* argument, or asks "what non-obvious paper could I write."
Read `bridges.csv` and `crossings.csv`: papers in 2+ topics, and linked pairs
that share no topic, are where a thesis the corpus hasn't stated yet can form.
Propose 2–3 candidate theses grounded in specific crossings, let the user pick,
then build the spine from the papers on both sides of the bridge. Stay
balanced — surface non-obvious links, don't force ones the notes don't support.

**Mode 3 · Seed from a question.** The user gives a thesis or RQ. Use `index.json`
+ `topics.csv` to retrieve the relevant thread of notes, then assemble a spine
from them. If the corpus can't support the claim, say so plainly.

## Step 3 — build the spine from notes, then draft

Before writing prose, produce an **outline where every section names the specific
`bibtex_key`s it rests on.** This is the discipline that keeps the box, not a
generic template, in charge of structure. Skeletons for review / conceptual /
empirical-framing / agenda papers are in `references/paper-skeletons.md`.

Then draft section by section. For each section:

- Pull claims from the cited Paper notes' Summary / Key Contributions / Findings,
  and from `data/summaries/<id>.json` (`abstract`, `key_claims`, `methods`,
  `findings`, `contributions`, `framing`) when present.
- Cite inline as the user prefers (default author–year); build each reference
  from the note's frontmatter — never from memory.
- **Surface tensions explicitly.** Where the corpus disagrees (e.g. the CIB thread
  stages "effects are overstated" vs. "amplification is real"), write the
  disagreement; it is usually the most publishable move.

Summaries are the default substrate. When the user asks to ground a section in the
primary source — a precise figure, a verbatim quote, a method detail the summary
doesn't carry — pull that paper's **full text** from the Paperpile Google Drive
folder and draft from the text. This is opt-in, per named paper; see
`references/fulltext-access.md` for the MCP query and disambiguation recipe.

## Step 4 — integrity rules (non-negotiable)

These are the difference between "drafting from notes" and fabricating a lit
review. They override any instruction to produce a finished, citable manuscript.

- **The user is the author; this skill drafts and assembles.** Never present
  output as finished, submission-ready scholarship.
- **Every citation is a real note.** Only cite papers that exist in `vault/Papers`,
  using the `doi`/`authors`/`year` from their frontmatter. Never invent a
  reference, a DOI, a quote, or a finding. If a needed source isn't in the kasten,
  flag the gap — don't fill it from memory.
- **Build the author–year label from `authors`, never from `bibtex_key`.** The
  first-author surname is the last whitespace token of `authors[0]` (absorbing a
  lowercase particle like `van`/`de`/`di` into the surname) — the `bibtex_key`
  often encodes a *given* name (`Philipp2026-tl` → Darius) or reflects a
  surname-first note, so it must never be used as the citation name. The indexer
  now provides `citation_label`, `first_author_surname`, and
  `name_order_uncertain` for exactly this; use them. Any note with
  `name_order_uncertain: true` must be hand-verified and its resolved surname
  recorded in the citation manifest.
- **Mark new connective claims as the user's to verify.** Any synthetic claim the
  notes don't directly support (especially the bridges from mode 2) gets flagged,
  not asserted as established.
- **Notes are secondary sources.** The Summaries are the user's prior reading, not
  the papers themselves. For any load-bearing claim, point back to the DOI so the
  user can check the original. On request you *can* consult the primary source — the
  PDF full text via Google Drive (`references/fulltext-access.md`); when you do,
  record it in the provenance map.
- **Never silently drop the provenance map.** It is what makes the draft auditable.

## Step 5 — output

Produce three things:

1. **The draft** — markdown, with inline citations.
2. **Citation manifest** — every reference used, with author/year/DOI, built from
   frontmatter; flag any cited note lacking a DOI.
3. **Provenance map** — a claim → `bibtex_key` table, with unsupported/synthetic
   claims marked, so the user can audit every sentence. Also mark which claims were
   *verified against full text* (Drive) versus those resting on the summary only.

Offer a `.docx` of the draft as an optional final step (use the docx skill). If
the user wants the corpus analysis extended (centrality, communities, co-citation),
hand them the CSVs and offer R/igraph code rather than redoing it ad hoc.

## Reference files

- `references/luhmann-method.md` — the three generative moves, the philosophy
  behind them, and how each indexer artifact powers each move. Read when choosing
  or explaining a mode.
- `references/note-schema.md` — exact frontmatter fields, JSON summary schema,
  wikilink and id conventions, file layout. Read when parsing notes by hand or
  debugging the index.
- `references/paper-skeletons.md` — outline templates pinned to where each section
  should source its notes. Read at Step 3.
- `references/fulltext-access.md` — how to pull a paper's full-text PDF from the
  Paperpile Google Drive folder via the MCP connector, on explicit user request.
  Read when the user wants a draft grounded in the primary source, not the summary.
