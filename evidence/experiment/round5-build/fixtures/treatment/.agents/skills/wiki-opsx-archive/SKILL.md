---
name: wiki-opsx-archive
description: Archive a completed OpenSpec change and harvest its crystallized decisions into the saidwhen knowledge bundle. Use instead of plain archive when the project has a docs/knowledge/ bundle.
---

# wiki-opsx-archive

Run the standard OpenSpec archive flow, then **harvest before you forget**:

1. Read the change's `design.md` (Decisions section) and `proposal.md`.
2. For each decision that should outlive the change, apply the capture rules
   below. **Evidence must live in the bundle — never link into
   `openspec/changes/`**: archived changes move (and are often gitignored),
   so those paths are ephemeral. If the decision's evidence was a
   conversation during this change, copy it into
   `docs/knowledge/interviews/<date>-<topic>.md` rather than pointing at change
   artifacts.
3. Harvest is distillation: a 10-task change usually yields 1–3 durable
   decisions, not 10.

Capture rules — verbatim from saidwhen capture v0.1 (normative source:
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

Finally, run the validator on the bundle (`scripts/validate.py` bundled with
the wiki-capture skill, or `validator/validate.py` in the saidwhen repo);
the bundle must pass.
