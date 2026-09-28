# Full-text access via Google Drive

The notes and `data/summaries/<id>.json` are the kasten's *prior reading* —
deliberately condensed. The **full text** of most papers lives as a PDF in one
of the kasten's **Google Drive** folders (the same folders the pipeline
extracts from). This file is how the skill reaches the primary source when a
draft needs more than the summary carries.

Access is through the **claude.ai Google Drive MCP connector**
(`mcp__claude_ai_Google_Drive__*`), which reads the Drive of whoever is signed
in to it. There is **no** local script, credential, or pip install for this
path, and it only exists where that connector does (Claude.ai, Desktop,
Cowork, Claude Code with the connector). Elsewhere, say so and stay on the
summaries.

## When to use it

**Only when the user explicitly asks**, for a *named, load-bearing* paper —
e.g. "pull the full text of Thiele2025-ol," "check what the paper actually
reports," "I need an exact quote/figure/method detail from X." It is never a
default step: note summaries remain the substrate for every draft. Don't fetch
full text proactively, in bulk, or "to be safe."

## The Drive folders

The PDFs are split across the folders below; search all of them. The list is
generated from `skill.fulltext_folders` in the kasten's `config.yml`. **If you
are running from inside a checkout of the kasten** (e.g. Claude Code opened on
the repo), that file's list is the authoritative one — read it and use its ids
instead of the ones below.

<!-- fulltext-folders:start -->
| folder | id | filenames |
|---|---|---|
| Paperpile To Read | `1gluNDqRQkyqxa_WIASaaoNEItrDlETkn` | Paperpile (`Author [et al.] Year - Title.pdf`) |
| Paperpile Classics | `1lIoUsLp3UXS8V0k1LC5yCPFor5Ql00Ro` | Paperpile (`Author [et al.] Year - Title.pdf`) |
<!-- fulltext-folders:end -->

- **Paperpile filenames:** `[FirstAuthor] [Year] - [Title].pdf`, or for multiple
  authors `[FirstAuthor] et al. [Year] - [Title].pdf`.
  Examples: `Matias 2025 - How public involvement can improve the science of AI.pdf`,
  `Pierri et al. 2025 - Research opportunities and challenges.pdf`.
- **Slack-inbox filenames** (papers a team member suggested in Slack): the
  bibtex key comes first, `[bibtex_key] - [FirstAuthor] [Year] - [Title].pdf`,
  e.g. `Smith2026-sl3k - Smith et al. 2026 - A study of X.pdf`. Match these on the
  key, which is exact.
- **Prerequisite:** each folder must be shared with the Google account the
  claude.ai Drive connector is signed in to (a team member: ask the kasten's
  owner). If a folder-scoped search returns *nothing* (or `get_file_metadata`
  on the folder id says "not found"), that's an **access** problem — the folder
  isn't shared with the connected account — not a sign the paper is missing.
  Say so rather than concluding the PDF doesn't exist.

## Find the PDF

You already have the note's `bibtex_key`, `title`, `authors`, and `year` (in
`index.json` and the note frontmatter). Build one
`mcp__claude_ai_Google_Drive__search_files` query scoped to the folders. Match
either the bibtex key (Slack-inbox files) or the first author's **surname** plus
one or two **distinctive title words** (Paperpile files) — not the whole title,
since filenames truncate and vary:

```
(parentId = '<folder id>' or parentId = '<folder id>' or …)
  and mimeType = 'application/pdf'
  and (title contains '<bibtex_key>'
       or (title contains '<first-author surname>'
           and title contains '<distinctive title word>'))
```

If the title search misses (unusual punctuation, abbreviated title), retry with
a different title word, or fall back to `fullText contains '<distinctive phrase>'`
within the same folders.

## Disambiguate (don't read the wrong PDF)

This mirrors `src/drive_client.py::find_pdf`, applied by judgment rather than a
score:

1. Prefer the candidate whose **filename title clearly matches** the note title.
2. Confirm the **author surname** and the **year** appear in the filename.
3. An author with several papers in the folder (e.g. `Giglietto`,
   `Bak-Coleman`) will return multiple hits — the year plus a title word should
   isolate the right one.
4. If several candidates survive, or none clearly matches, **report the
   ambiguity and ask** — never guess a PDF. Reading the wrong paper is worse than
   falling back to the summary.

## Read it

Once you have the file id, use
`mcp__claude_ai_Google_Drive__read_file_content(fileId)` — it supports
`application/pdf` and returns a natural-language text representation, so no
download/parse step is needed. For very large PDFs the returned text may be
**truncated** (per the tool's own caveat); if a needed section is missing, say so
rather than assuming the paper omits it.

## Integrity (extends SKILL.md Step 4)

- Full text is a **primary source** — you may quote it and cite exact figures.
  Quote precisely and sparingly; attribute to the paper, not the note.
- Still build the **reference** from the note's frontmatter
  (`authors`/`year`/`doi`) — the Drive filename is not a citation.
- In the **provenance map**, mark which claims were *verified against full text*
  versus those resting on the summary. This is the whole point: it tells the user
  exactly which sentences have been checked against the source.
- If the connector is unavailable (e.g. a headless/cron run) or no PDF matches,
  **say so and fall back to the summary** — degrade, never fabricate.
