# Behavior: read-first

You are working in a project that keeps its decision provenance in an OKF
bundle at `docs/knowledge/`. Follow these rules.

<!-- saidwhen:behavior read-first v0.1 -->
## Before planning or asking anything

1. Read `docs/knowledge/index.md`. Follow links relevant to your current task
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

## When decisions are made

Capture them — follow [capture.md](capture.md).
