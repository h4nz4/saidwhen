---
name: wiki-gc
description: Curate the project's saidwhen knowledge bundle (knowledge/) — merge duplicate concepts, flag stale decisions whose revisit triggers fired, repair broken links, prune the index, and list knowledge gaps. Use periodically or when the wiki feels stale.
---

# wiki-gc

This project keeps decision provenance in an OKF bundle at `knowledge/`.

Read `behaviors/gc.md` in this repo if present; otherwise apply these rules,
verbatim from saidwhen gc v0.1:

1. Merge duplicates; update every inbound link to the survivor.
2. For each accepted Decision, check timestamp and revisit triggers against
   observable reality; if stale, set `status: revisit` with a note — never
   supersede without a human answer.
3. Repair resolvable broken links; surface truly dangling ones to the human.
4. Prune and refresh `knowledge/index.md`.
5. List topics the project has opinions about that the bundle doesn't record.
6. Log every change to `knowledge/log.md`; never delete a Decision.

Finish by running `validator/validate.py` on the bundle if available.
