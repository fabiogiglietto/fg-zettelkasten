# Vendored patches

This directory vendors **Quartz v4** (https://github.com/jackyzha0/quartz).
The files below carry local edits that upstream Quartz does not have.
**Re-apply every patch after any Quartz upgrade** (upgrading by copying a new
Quartz tree over this directory silently reverts them), then verify.

## 1. `quartz/util/glob.ts` — `gitignore: false` in the globby options

**What:** the `globby(...)` call in `glob()` passes `gitignore: false`
(upstream default is `true`).

**Why:** the site content lives in `quartz/content/`, which is `.gitignore`d
because it is regenerated from `vault/` by `python -m src.main export-site`.
With `gitignore: true` Quartz would skip the entire content tree and build an
empty site. `ignorePatterns` from `quartz.config.ts` still filters
independently.

**Re-apply:** in `quartz/util/glob.ts`, add `gitignore: false` (with its
explanatory comment — search this repo's git history for "vendored edit") to
the globby options.

**Verify:** `python -m src.main export-site && cd quartz && npx quartz build`
— the build must emit pages for the vault notes, not an empty `public/`.

---

Adding a new patch? Edit the file with a `// fg-zettelkasten: vendored edit`
comment at the change site and add a section here: what, why, how to
re-apply, how to verify.
