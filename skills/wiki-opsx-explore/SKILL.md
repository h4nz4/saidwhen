---
name: wiki-opsx-explore
description: OpenSpec explore mode backed by the saidwhen wiki — think through ideas grounded in the project's recorded decisions, constraints, terms, and components, and pull that context into proposals. Use instead of plain explore when the project has a docs/knowledge/ bundle.
---

# wiki-opsx-explore

Enter OpenSpec explore mode (thinking partner; investigate, don't implement),
with one addition: **the wiki comes first.** Before exploring any topic,
apply these rules — verbatim from saidwhen read-first v1.0 (normative source:
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

During exploration:

- Ground options against recorded constraints — cite files, not memory.
- When the user answers a scoping question, note it as capture material.
- When a decision crystallizes, offer to record it (the wiki-capture skill /
  capture behavior). The user decides; don't auto-capture.

When exploration flows into an OpenSpec proposal, the wiki feeds it:

- Pull the relevant Terms, Constraints, Components, and Decisions into the
  proposal's context **by link** — recorded constraints shape the proposal
  without the user restating them, and the reviewer can follow every claim
  to its source.
- Delta-spec requirements SHOULD carry a why-link to the decision that
  produced them — `([why](<path>))` **inside the requirement's prose**,
  written relative to the MAIN spec location
  (`openspec/specs/<capability>/`), so delta→main sync copies it verbatim
  and it resolves after archive.
- design.md decisions cite their interview/constraint evidence inline at
  write time — harvest at archive then becomes mechanical.
