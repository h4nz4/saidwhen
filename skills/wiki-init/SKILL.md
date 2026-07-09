---
name: wiki-init
description: Set up the saidwhen project wiki — scaffold the docs/knowledge/ OKF bundle (decisions, constraints, domain, systems), optionally install the ambient AGENTS.md snippet and a CI validate+render workflow. Use when a project has no docs/knowledge/ directory and the user wants a project wiki, agent memory, or asks to "set up saidwhen".
---

# wiki-init

Bootstrap this project's wiki (saidwhen v1.0): one OKF bundle that serves
agents as project memory, the spec workflow as its knowledge layer, and
humans via rendered views.

1. If `docs/knowledge/` already exists, stop — nothing to init; suggest the
   wiki-explore / wiki-capture skills instead.
2. Copy `assets/knowledge-skeleton/` to `docs/knowledge/` (`index.md`,
   `log.md`, and the `decisions/`, `constraints/`, `domain/`, `systems/`
   directories). Fill index.md's one-line project description from the
   repo's README if one exists.
3. **Offer — as an explicit choice, don't do it silently** — to append
   `assets/snippet.md` to the project's `AGENTS.md` (or `CLAUDE.md`).
   The snippet is the ambient always-on form of the read-first and capture
   rules; recommend it when the user's agent loads skills conditionally or
   not at all. Skipping it is fine — the wiki-explore and wiki-capture
   skills carry the same rules.
4. **Offer CI** (explicit choice again): a workflow step that validates the
   bundle on every push (`python validate.py docs/knowledge` — the
   wiki-capture skill bundles the validator) and, if the wiki-render skill
   is installed, compiles the wiki site so humans always have a current
   view.
5. **Existing codebase?** Offer the wiki-bootstrap skill to populate the
   fresh wiki from what's already there — architecture pages, glossary,
   use cases — generated under its no-invented-whys rules.
6. Log the scaffold: append a `created` line for each file to
   `docs/knowledge/log.md`.

The first knowledge usually arrives minutes later — capture it with
wiki-capture: attributed facts first, then the decision that rests on them.
