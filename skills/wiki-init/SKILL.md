---
name: wiki-init
description: Set up saidwhen decision provenance in a project — scaffold the knowledge/ bundle and optionally install the ambient AGENTS.md snippet. Use when a project has no knowledge/ directory and the user wants decision provenance, or asks to "set up saidwhen".
---

# wiki-init

Bootstrap this project's decision provenance (saidwhen v0.1).

1. If `knowledge/` already exists, stop — nothing to init; suggest the
   wiki-explore / wiki-capture skills instead.
2. Copy `assets/knowledge-skeleton/` to the project root as `knowledge/`
   (`index.md` and `log.md`). Fill index.md's one-line project description
   from the repo's README if one exists.
3. **Offer — as an explicit choice, don't do it silently** — to append
   `assets/snippet.md` to the project's `AGENTS.md` (or `CLAUDE.md`).
   The snippet is the ambient always-on form of the read-first and capture
   rules; recommend it when the user's agent loads skills conditionally or
   not at all. Skipping it is fine — the wiki-explore and wiki-capture
   skills carry the same rules.
4. Log the scaffold: append a `created` line for each file to
   `knowledge/log.md`.

The first decision usually arrives minutes later — capture it with
wiki-capture, evidence first.
