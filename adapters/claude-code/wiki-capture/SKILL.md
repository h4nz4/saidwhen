---
name: wiki-capture
description: Record a crystallized decision, interview answer, or constraint into the project's saidwhen knowledge bundle (knowledge/). Use when a design choice is settled with the user, when the user answers scoping questions worth keeping, or at the end of a work session to distill what should outlive it.
---

# wiki-capture

This project keeps decision provenance in an OKF bundle at `knowledge/`.

Read `behaviors/capture.md` in this repo if present; otherwise apply these
rules, verbatim from saidwhen capture v0.1:

1. Write `knowledge/decisions/<slug>.md` with `type: Decision`,
   `status: accepted`, a `timestamp`, a `## Rejected` section (with revisit
   triggers where they exist), and a link to its evidence (interview answer,
   constraint, or source).
2. Record new human answers in `knowledge/interviews/<date>-<topic>.md` with
   `type: Interview`.
3. Append one line to `knowledge/log.md`:
   `YYYY-MM-DD  <path>  <created|updated|superseded>  <one-line reason>`.
4. Add load-bearing concepts to `knowledge/index.md`.
5. Never delete or silently contradict a recorded decision — supersede it
   (`status: superseded`, link to successor, log it).
6. Distill, don't transcribe: capture what should outlive the session.

If `validator/validate.py` is available, run it on the bundle after writing.
