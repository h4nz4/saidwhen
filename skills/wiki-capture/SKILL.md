---
name: wiki-capture
description: Record a crystallized decision, interview answer, or constraint into the project's saidwhen knowledge bundle (docs/knowledge/). Use when a design choice is settled with the user, when the user answers scoping questions worth keeping, or at the end of a work session to distill what should outlive it.
---

# wiki-capture

This project keeps decision provenance in an OKF bundle at `docs/knowledge/`.
Apply these rules — verbatim from saidwhen capture v0.1 (normative source:
`behaviors/capture.md`; CI keeps this copy in sync):

<!-- saidwhen:behavior capture v0.1 -->
## When a decision crystallizes

1. Write `docs/knowledge/decisions/<slug>.md` with `type: Decision`,
   `status: accepted`, a `timestamp`, a `## Rejected` section (with revisit
   triggers where they exist), and a link to its evidence (interview answer,
   constraint, or source).
2. If the human gave you new answers, record them in
   `docs/knowledge/interviews/<date>-<topic>.md` with `type: Interview`.
3. Append one line to `docs/knowledge/log.md`:
   `YYYY-MM-DD  <path>  <created|updated|superseded>  <one-line reason>`.
4. Add the new concept to `docs/knowledge/index.md` if it's load-bearing.

## When superseding a decision

Never delete or silently contradict a recorded decision. Set the old
document's `status: superseded`, link it to its successor, record the new
evidence, and log the supersession.

## When work completes

Distill: which decisions from this session deserve to outlive it? Capture
those; let the rest evaporate. The wiki is a curated library, not a transcript.
<!-- /saidwhen:behavior capture -->

If `validator/validate.py` is available, run it on the bundle after writing.
