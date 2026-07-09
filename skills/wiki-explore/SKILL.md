---
name: wiki-explore
description: Consult the project's saidwhen wiki (docs/knowledge/) — the project's memory — before planning, proposing, reading code for context, or asking the user anything. Use at the start of any feature evaluation, design discussion, or requirements question in a project with a docs/knowledge/ bundle.
---

# wiki-explore

This project's wiki — an OKF bundle at `docs/knowledge/` — is its memory: knowledge the code can't express, kept trustworthy by built-in provenance.
Apply these rules — verbatim from saidwhen read-first v1.0 (normative source:
`behaviors/read-first.md`; CI keeps this copy in sync):

<!-- saidwhen:behavior read-first v1.0 -->
## Before planning, asking, or spelunking code

1. Read `docs/knowledge/index.md`. Follow links relevant to your current
   task (decisions, constraints, terms, components). Budget: read what's
   relevant, not the whole bundle — and read it BEFORE deriving project
   context from source files.
2. **Never ask the human a question the wiki already answers.** If a
   recorded fact or constraint answers it, cite the file and move on.
3. When your task touches an existing `Decision`:
   - `status: accepted` and its evidence still plausible → respect it. Do not
     re-litigate. Cite it.
   - Evidence may be stale (old timestamp, changed circumstances) → do NOT
     silently obey and do NOT silently override. Ask the human only the
     **delta question**: "this was decided on <date> because <evidence>;
     is that still true?"

## When the wiki is silent

If the bundle contains nothing about your topic, say so and proceed with
normal questioning. **Never cite a decision, fact, or constraint that does
not exist**, and never claim the wiki answers what it does not. Recorded
constraints that genuinely apply to the new topic still apply.
<!-- /saidwhen:behavior read-first -->

After exploring, if decisions crystallize, use the wiki-capture skill.
