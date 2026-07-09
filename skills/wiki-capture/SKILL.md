---
name: wiki-capture
description: Record crystallized knowledge into the project's saidwhen wiki (docs/knowledge/) as attributed facts — constraints, domain terms, component notes — and decisions with their evidence. Use when a design choice is settled, when the user states a fact worth keeping, or at the end of a work session to distill what should outlive it.
---

# wiki-capture

This project's wiki — an OKF bundle at `docs/knowledge/` — is its memory: knowledge the code can't express, kept trustworthy by built-in provenance.
Apply these rules — verbatim from saidwhen capture v1.0 (normative source:
`behaviors/capture.md`; CI keeps this copy in sync):

<!-- saidwhen:behavior capture v1.0 -->
## When knowledge crystallizes

1. Record each settled human answer as an **attributed fact**: a distilled
   statement in `docs/knowledge/constraints/<slug>.md` (a fact that bounds
   the design), `domain/<slug>.md` (a fact about meaning), or
   `systems/<slug>.md` (curated architecture), with `source:` (who said
   it) and `timestamp:` (when). No dialogue transcripts, no verbatim
   quotes — the distilled statement itself, attributed and dated.
2. When a decision crystallizes, write `docs/knowledge/decisions/<slug>.md`
   with `type: Decision`, `status: accepted`, a `timestamp`, a
   `## Rejected` section (with revisit triggers where they exist), and a
   link to its evidence — the attributed fact(s) or an external source.
3. Append one line to `docs/knowledge/log.md`:
   `YYYY-MM-DD  <path>  <created|updated|superseded>  <one-line reason>`.
4. Add the new concept to `docs/knowledge/index.md` if it's load-bearing.

## When superseding a decision

Never delete or silently contradict a recorded decision. Set the old
document's `status: superseded`, link it to its successor, record the new
evidence, and log the supersession.

## When work completes

Distill: which knowledge from this session deserves to outlive it? Capture
that; let the rest evaporate. The wiki is a curated library, not a
transcript.
<!-- /saidwhen:behavior capture -->

If `validator/validate.py` is available, run it on the bundle after writing.
