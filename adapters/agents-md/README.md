# AGENTS.md adapter

The lowest-common-denominator install: works with any agent that reads
AGENTS.md-style instruction files (Claude Code, Cursor, Copilot, Codex, …).

## Install (3 steps)

1. Create a `knowledge/` directory in your repo with an `index.md` and
   `log.md` (copy [example/knowledge/](../../example/knowledge/) as a starting
   skeleton).
2. Paste the contents of [snippet.md](snippet.md) into your project's
   `AGENTS.md` (or `CLAUDE.md`).
3. Optionally vendor [validator/validate.py](../../validator/validate.py) and
   run it in CI.

That's it. Your agent now reads the wiki before asking, and writes decisions
when they crystallize.

## Sync rule

`snippet.md` embeds the normative wording from
[behaviors/read-first.md](../../behaviors/read-first.md) and
[behaviors/capture.md](../../behaviors/capture.md) — the single source of
truth. Do not edit the behavioral wording here; change `behaviors/` and
re-embed. Semantic behavior changes require re-validation (see
[CONTRIBUTING.md](../../CONTRIBUTING.md)).
