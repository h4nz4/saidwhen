---
name: wiki-gc
description: Curate the project's saidwhen wiki (docs/knowledge/) — merge duplicate concepts, flag stale decisions whose revisit triggers fired, audit architecture (Component) pages for drift, repair broken links, prune the index, and list knowledge gaps. Use periodically or when the wiki feels stale.
---

# wiki-gc

This project's wiki — an OKF bundle at `docs/knowledge/` — is its memory: knowledge the code can't express, kept trustworthy by built-in provenance.
Apply these rules — verbatim from saidwhen gc v1.0 (normative source:
`behaviors/gc.md`; CI keeps this copy in sync):

<!-- saidwhen:behavior gc v1.0 -->
## The pass

1. **Merge duplicates.** Two documents describing the same fact become one;
   update every inbound link to the survivor.
2. **Flag stale decisions.** For each `status: accepted` Decision, check its
   timestamp and revisit triggers against what you can observe (code, issues,
   recent facts). If a trigger appears to have fired or the evidence has
   plausibly aged out, set `status: revisit` and note why — do NOT supersede
   without a human answer.
3. **Audit Component pages.** Check each `systems/` page against the current
   codebase. A page that no longer matches reality is flagged for review —
   a log entry and, where sensible, a note in the page — never silently
   trusted and never silently rewritten.
4. **Repair links.** Every relative link must resolve. Fix moved targets;
   surface genuinely dangling references to the human rather than deleting
   silently.
5. **Prune the index.** `index.md` lists load-bearing concepts; remove entries
   that no longer earn the space, add ones that do.
6. **Identify gaps.** Note topics the project clearly has opinions about that
   the bundle doesn't record — these are capture targets for the next session.

## Rules

- Every change made by this pass appends a line to `docs/knowledge/log.md`.
- This pass never deletes a Decision — supersession preserves history.
- Run the validator after the pass; the bundle must still conform.
<!-- /saidwhen:behavior gc -->

Finish by running `validator/validate.py` on the bundle if available.
