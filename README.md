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

`.env` needs `GOOGLE_APPLICATION_CREDENTIALS` (path to a Google
service-account JSON with read access to Paperpile's Drive folder — the same
account research-radio uses) and `GOOGLE_DRIVE_FOLDER_ID`.

### Claude credentials: CI only

The Anthropic API is reached through **Workload Identity Federation**, not an
API key: `update-vault.yml` mints a GitHub Actions OIDC token
(`.github/scripts/mint-oidc-token.sh`) and the SDK exchanges it for a
short-lived access token. A local machine cannot mint that token, so **every
command that calls Claude runs in CI** — dispatch it instead of running it
locally:

```bash
gh workflow run update-vault.yml                   # update
gh workflow run update-vault.yml -f recluster=true # refresh-topics + update --recluster
```

Locally, run only the steps that make no Claude call: the tests,
`export-site`, `fix-links`, `dedupe-vault` and `check-published` (report mode),
`suggest-classics`, `retract --no-structures` and
`check-retractions` (report mode, or `--apply --no-structures`). Anything else stops with
`No Anthropic credentials`, which is the intended behaviour.

Do not put `ANTHROPIC_API_KEY` in `.env`. It outranks federation in the SDK's
credential chain, so a stale key produces a 401 rather than a clear error.

## Usage

```bash
python -m src.main refresh-topics       # build the topic register from github.io
python -m src.main bootstrap            # process the whole archive (run once)
python -m src.main bootstrap --limit 5  # smoke test on the first 5 papers
python -m src.main update               # daily incremental run
python -m src.main update --recluster   # incremental + full re-cluster
python -m src.main export-site          # export the vault to quartz/content/
python -m src.main retract KEY --notice DOI --date YYYY-MM-DD  # mark a paper retracted
python -m src.main check-retractions    # report Crossref retractions / notices (--apply writes)
python -m src.main social-post --dry-run # compose the social posts for queued papers, publish nothing
```

### Social posts

Each newly-added reading-list note is announced on Mastodon, Threads,
LinkedIn and Bluesky as an instalment of a recognisable column: a masthead
line that starts with `#toread` and says the post is auto-posted
(`social.masthead`), the APA-7 citation, and the link to the note. The
LinkedIn post adds a brief description (Claude) above the citation; the
others have no room for one next to a full citation. Every post shows the note as its link card, with the
note's social image: Threads, LinkedIn and Bluesky are handed the card (the
image is uploaded to Bluesky, which does not fetch it), while Mastodon builds
it from the first link in the text — so there the note link comes before the
citation and its DOI. On Bluesky (300 characters) the card is the only link
to the note, links are shown in short form and a citation that does not fit
one post continues in a reply. `update` queues a new paper (`social_pending` in
`data/state.json`); `social-post` runs in `update-vault.yml` *after* the Pages
deploy — the platforms cache link previews, so the note must be live first —
and records where each paper went (`social: {mastodon: {url, at}, …}`), so a
paper is posted once per platform. Same scope as the Slack digest: no
classics, own publications, retracted papers or superseded stubs, and nothing
that predates the feature.

Configured by the `social` block in `config.yml`. A platform posts only when
it is enabled there **and** its token is set as a repo secret:

| Platform | Secrets | Token lifetime |
|---|---|---|
| Mastodon | `MASTODON_ACCESS_TOKEN` (scope `write:statuses`) | does not expire |
| Threads | `THREADS_ACCESS_TOKEN` (`threads_basic`, `threads_content_publish`, `threads_manage_replies`) | 60 days |
| Bluesky | `BLUESKY_APP_PASSWORD` (an app password; the handle is in `config.yml`) | does not expire |
| LinkedIn | `LINKEDIN_ACCESS_TOKEN` (`openid profile w_member_social`; the author is read from the token, or from an optional `LINKEDIN_PERSON_URN`) | 60 days |

Set the repo variables `THREADS_TOKEN_EXPIRES` / `LINKEDIN_TOKEN_EXPIRES`
(ISO dates) when minting those tokens: the ops Slack channel is warned a week
before either runs out, and again if a platform rejects its token. A rejected
token never fails the run; the paper stays queued for that platform (for
`max_age_days`) and is posted once the secret is replaced.

With `social.dry_run: true` nothing is published: the composed posts go to the
job log and the ops channel, once per paper. To post a single paper by hand,
run the workflow with the `social_key` input set to its bibtex key; add
`social_dry_run=true` to only preview it (every platform enabled in config,
token or not).

## Vault layout

- `vault/Papers/`     — one note per paper, filename = bibtex key
- `vault/Topics/`     — register entry notes (the *Schlagwortregister*)
- `vault/Structures/` — hub notes narrating an argument across papers in a topic

Open `vault/` as an Obsidian vault. `data/` (state, topics, summaries) and
`vault/` are committed; extracted PDF text is transient and never committed.

## Writing from the kasten (Claude Code skill)

The repo ships a Claude Code skill, **`zettel-paper`**, that drafts new papers,
literature reviews, and syntheses *from* the vault the Luhmann way — pulling a
thread of linked notes that already forms an argument and turning it into prose,
citing only real notes with traceable DOIs. It lives in
`.claude/skills/zettel-paper/` and is auto-discovered when you open this repo in
[Claude Code](https://claude.com/claude-code) — no install step.

Just ask in plain language; the skill triggers on intent, e.g.:

- "Draft a literature review on coordinated inauthentic behavior from the kasten."
- "What non-obvious paper could I write from these notes?"
- "Turn the platform-governance Structure into a framing piece."

It works from the **public** notes and summaries, so collaborators can run it on
a fresh clone. An optional full-text path reads a named paper's PDF from the
kasten's Google Drive folders (`skill.fulltext_folders` in `config.yml`: the
Paperpile To Read and Classics folders, plus the Slack inbox on a team fork),
via the Claude Google Drive connector. It works for anyone the folders are
shared with, and degrades to the published summaries when a folder isn't
accessible or the agent has no Drive connector.

### Using it on Claude.ai or in Claude Cowork

The skill isn't only for Claude Code. A pre-built upload bundle —
[`zettel-paper-skill.zip`](zettel-paper-skill.zip) — is committed at the repo
root, so collaborators can load it as an Agent Skill on
**[Claude.ai](https://claude.ai)** (web / desktop Chat) or in
**[Claude Cowork](https://www.anthropic.com/product/claude-cowork)** without
cloning anything. Both run it in a sandboxed shell that clones this **public**
repo and executes a standard-library Python script; neither auto-discovers the
repo's `.claude/skills/`, so add the skill once:

- **Pro / Max:** download `zettel-paper-skill.zip` and upload it as a personal
  Skill in your Claude account settings (under *Skills* / *Capabilities*). It then
  works in Claude.ai Chat, Cowork, and Claude Code.
- **Team / Enterprise:** an admin provisions it org-wide via
  *Organization settings → Skills*, and every member gets it.

The bundle is built from `.claude/skills/zettel-paper/` by
`scripts/build_skill_bundle.py`, which retargets it from the `skill:` block of
`config.yml` (name, repo, bundle file) so a fork ships a skill that drafts from
its own kasten. A CI workflow (`.github/workflows/skill-bundle.yml`) rebuilds and
commits it whenever the skill, that config block or the script changes on `main`,
so it never goes stale. (To rebuild by hand: `python -m scripts.build_skill_bundle`.)
The website homepage describes the skill and how to install it
(`skill.homepage`). Invoke it
the same way ("draft a review on X from the kasten"). The full-text Google Drive
path needs the folders shared with the reader's Google account; without that,
the skill drafts from the public summaries.

## Website

The vault is also published as a public website with [Quartz](https://quartz.jzhao.xyz/)
— interactive graph, backlinks, search, and topic/structure landing pages — at
**https://fabiogiglietto.github.io/fg-zettelkasten/**. The `update-vault` GitHub
Action rebuilds and deploys it on every run.

```bash
python -m src.main export-site                 # vault/ -> quartz/content/
cd quartz && npm ci && npx quartz build --serve # preview at localhost:8080
```

`export-site` is deterministic (no LLM): it copies the vault notes into
`quartz/content/`, strips Obsidian-only `dataview` blocks, and generates the
homepage. The vault itself is never modified. Quartz needs Node 22+; the
generated `quartz/content/` and `quartz/public/` are not committed.

## Status

Scaffold. Data-fetching modules are implemented; LLM-driven steps
(`topics_client.synthesize_register`, `summarizer.summarize_paper`,
`themes.*`, `note_builder.build_paper_note` / `build_structure_note`, the
`claude_client` SDK calls, and the `main.py` command bodies) are stubbed with
`NotImplementedError` and pointers to the implementation plan.
