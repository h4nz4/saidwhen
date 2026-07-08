---
name: wiki-explore
description: Consult the project's saidwhen knowledge bundle (knowledge/) before planning, proposing, or asking the user anything. Use at the start of any feature evaluation, design discussion, or requirements question — and whenever a request might touch a recorded decision.
---

# wiki-explore

This project keeps decision provenance in an OKF bundle at `knowledge/`.
Apply these rules — verbatim from saidwhen read-first v0.1 (normative source:
`behaviors/read-first.md`; CI keeps this copy in sync):

<!-- saidwhen:behavior read-first v0.1 -->
## Before planning or asking anything

1. Read `knowledge/index.md`. Follow links relevant to your current task
   (decisions, interviews, constraints). Budget: read what's relevant, not
   the whole bundle.
2. **Never ask the human a question the wiki already answers.** If an
   interview or constraint answers it, cite the file and move on.
3. When your task touches an existing `Decision`:
   - `status: accepted` and its evidence still plausible → respect it. Do not
     re-litigate. Cite it.
   - Evidence may be stale (old timestamp, changed circumstances) → do NOT
     silently obey and do NOT silently override. Ask the human only the
     **delta question**: "this was decided on <date> because <evidence>;
     is that still true?"

## When the wiki is silent

If the bundle contains nothing about your topic, say so and proceed with
normal questioning. **Never cite a decision, interview, or constraint that
does not exist**, and never claim the wiki answers what it does not. Recorded
constraints that genuinely apply to the new topic still apply.
<!-- /saidwhen:behavior read-first -->

After exploring, if decisions crystallize, use the wiki-capture skill.
