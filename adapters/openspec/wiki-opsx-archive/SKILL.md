---
name: wiki-opsx-archive
description: Archive a completed OpenSpec change and harvest its crystallized decisions into the saidwhen knowledge bundle. Use instead of plain archive when the project has a knowledge/ bundle.
---

# wiki-opsx-archive

Run the standard OpenSpec archive flow, then **harvest before you forget**:

1. Read the change's `design.md` (Decisions section) and `proposal.md`.
2. For each decision that should outlive the change, apply
   `behaviors/capture.md`: write `knowledge/decisions/<slug>.md`
   (`type: Decision`, `status: accepted`, `timestamp`, `## Rejected` with
   revisit triggers, link to evidence). If the decision's evidence was a
   conversation with the user during this change, record it as
   `knowledge/interviews/<date>-<topic>.md`.
3. Supersede — never contradict — any existing decisions the change replaced.
4. Append `knowledge/log.md` lines and update `knowledge/index.md`.
5. Run `validator/validate.py knowledge` if available; the bundle must pass.

Harvest is distillation: a 10-task change usually yields 1–3 durable
decisions, not 10.
