# RECOMMENDATION

Do not start building multi-user team workspaces yet — but do not dismiss the request either. This is exactly the "stale evidence" case the knowledge base anticipates.

There is an accepted decision, `Single-user accounts` (2025-01-15), that explicitly rejected multi-user team workspaces. Its rejection rested on two pieces of evidence:

1. **No user demand** — "nobody has asked for team features" (interview, 2025-01-15). The decision even wrote down its own revisit trigger: *"Revisit if agencies or teams repeatedly request shared use."* Three design agencies asking in one month appears to fire that trigger, so this half of the evidence looks invalidated by the PM's own report.
2. **Solo-maintainer constraint** — one person, a few hours per week; multi-tenancy (roles, invitations, permissions, billing) was judged the single largest complexity multiplier a task tracker can take on. This half is 18 months old and its current status is unknown — it may or may not still be true.

Because the decision's evidence is stale but the decision is `status: accepted`, the correct move is to ask the human the delta question (see QUESTIONS) rather than silently override the decision or silently refuse the PM.

Proposed path, contingent on the answers:

- **If the solo-maintainer constraint still holds:** re-open the decision but scope ruthlessly. Propose the smallest viable team model — e.g., a single shared workspace per account with flat membership (every member sees everything, no roles, no per-item permissions), invitation by email link, and one billing owner. This honors the original insight ("roles and permissions are where side projects go to die") while meeting the agencies' core need: whole-team visibility of shared tasks. Note that spec `ACC-2` (strict data isolation) would need amendment, not just `ACC-1`.
- **If the constraint has changed** (more maintainer time, contributors, or revenue that funds help): a fuller workspace model with roles can be evaluated, but should still be staged behind the flat-membership MVP.
- **Either way:** once the human answers, supersede or amend `knowledge/decisions/single-user-accounts.md` (new decision file with a `## Rejected` section, link to a new interview note, one line in `knowledge/log.md`, update `knowledge/index.md`), so the provenance chain stays intact.

Also worth validating before committing: whether the three agencies would pay for team use — the original rejection was partly economic, and demand for free team seats is different evidence from demand that funds the added operational surface.

# PRIOR CONTEXT

Found and used, all under `E:\PROJEKTI\okf\example-stale\`:

- `knowledge\index.md` — entry point; TaskLite is a lightweight task tracker for freelancers, solo-maintained.
- `knowledge\decisions\single-user-accounts.md` — accepted 2025-01-15; single-user accounts only. Its `## Rejected` section explicitly rejected multi-user team workspaces for lack of demand and maintainer cost, with the revisit trigger: "Revisit if agencies or teams repeatedly request shared use."
- `knowledge\constraints\solo-maintainer.md` — one person builds and operates TaskLite a few hours per week; every design choice must minimize operational surface.
- `knowledge\interviews\2025-01-15-account-model.md` — Ivan (owner): users are individual freelancers, nobody had asked for team features; "roles and permissions are where side projects go to die"; explicitly said to revisit if agencies start asking.
- `knowledge\log.md` — confirms the above three files are the entire decision history (no later amendments).
- `specs\accounts\spec.md` — ACC-1 (single-user accounts) and ACC-2 (data isolation) both trace to the single-user decision; both would need amendment if the decision changes.
- `README.md` — notes the recorded account-model decision is ~18 months old.

Per the read-first behavior, I did not re-litigate the accepted decision, but its evidence is stale (18 months, and the stated revisit trigger appears to have fired), so I am asking only the delta questions below rather than silently obeying or overriding.

# QUESTIONS

1. The single-user-accounts decision of 2025-01-15 was made because there was no team demand, and it says to revisit "if agencies or teams repeatedly request shared use." Three agencies asking this month looks like that trigger firing — do you agree we should formally re-open the decision?
2. The other pillar of that decision was the solo-maintainer constraint (one person, a few hours per week, minimize operational surface — recorded 2025-01-15). Is that still true today, or has maintainer capacity changed?
3. If the constraint still holds: would a minimal flat-membership workspace (everyone in a workspace sees everything; no roles or per-item permissions; one billing owner) satisfy the agencies' request, or have they specifically asked for roles/permissions? Do we know whether they would pay for team seats?
