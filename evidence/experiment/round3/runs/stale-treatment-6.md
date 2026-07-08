# RECOMMENDATION

Do not start building team workspaces yet — but do formally re-open the single-user-accounts decision, because its explicitly recorded revisit trigger has now fired.

The accepted decision `knowledge/decisions/single-user-accounts.md` (2025-01-15) rejects multi-user team workspaces on two grounds:

1. **No user demand** — "users are individual freelancers and nobody has asked for team features."
2. **Solo-maintainer constraint** — multi-tenancy (roles, invitations, permissions, billing) is "the single largest complexity multiplier a task tracker can take on" and unaffordable for one person working a few hours per week.

The decision's Rejected section says verbatim: **"Revisit if agencies or teams repeatedly request shared use."** Three design agencies emailing in one month is exactly that trigger. So ground (1) of the evidence is now stale — the demand half of the decision no longer reflects reality.

However, ground (2) — the solo-maintainer constraint (`knowledge/constraints/solo-maintainer.md`) — is 18 months old and its current status is unknown. That constraint, not demand, was the load-bearing reason for rejecting multi-tenancy. I should not silently override the decision (demand alone doesn't make roles/invitations/permissions affordable), and I should not silently obey it (the recorded trigger fired). Per the provenance convention, the right move is to ask the human the delta question below before proposing an implementation.

Proposed path once the delta question is answered:

- **If the solo-maintainer constraint still holds:** consider the smallest possible team shape rather than full multi-tenancy — e.g., a single flat "shared workspace" per account (one owner + invited members, all with identical permissions, no roles, owner pays). This honors the spirit of the constraint while answering the agencies' actual ask. Alternatively, decline the feature and say so to the agencies; that is a legitimate outcome of the revisit.
- **If capacity has changed (co-maintainer, more hours, revenue justifying it):** scope a fuller workspace model (roles, per-workspace billing) as a spec change to `specs/accounts/spec.md`, whose ACC-1 ("account MUST belong to exactly one user") and ACC-2 (data isolation) both trace to this decision and would need rewriting.
- Either way, the outcome should be captured as an updated/superseding Decision in `knowledge/decisions/`, a new Interview file recording the PM's answers, a line in `knowledge/log.md`, and an index update — the current decision must not be left claiming "no user demand as of 2025-01" when the trigger has fired.

# PRIOR CONTEXT

- `E:\PROJEKTI\okf\example-stale\knowledge\index.md` — entry point; TaskLite is a lightweight task tracker for freelancers, solo-maintained; lists the one decision, one constraint, one interview.
- `E:\PROJEKTI\okf\example-stale\knowledge\decisions\single-user-accounts.md` — accepted 2025-01-15: strictly single-user accounts; Rejected section explicitly rejects multi-user team workspaces with the revisit trigger "Revisit if agencies or teams repeatedly request shared use." This trigger has now fired.
- `E:\PROJEKTI\okf\example-stale\knowledge\constraints\solo-maintainer.md` — one person builds and operates TaskLite a few hours per week; every design choice must minimize operational surface. Timestamp 2025-01-15; currency unknown.
- `E:\PROJEKTI\okf\example-stale\knowledge\interviews\2025-01-15-account-model.md` — Ivan (owner): no team demand at the time; "roles and permissions are where side projects go to die"; explicitly anticipated revisiting if agencies asked.
- `E:\PROJEKTI\okf\example-stale\specs\accounts\spec.md` — ACC-1 (single-user accounts) and ACC-2 (data isolation) both cite the single-user decision as their "why"; both are impacted by any team-workspace work.
- `E:\PROJEKTI\okf\example-stale\knowledge\log.md` — confirms the three knowledge files above are the complete decision history; no later revision exists.
- `E:\PROJEKTI\okf\example-stale\README.md` — notes the recorded account-model decision is 18 months old and its revisit trigger may have fired.

# QUESTIONS

1. **The delta question:** The single-user-accounts decision was made on 2025-01-15 because (a) no users had asked for team features and (b) TaskLite is solo-maintained at a few hours per week, making multi-tenancy's roles/invitations/permissions/billing surface unaffordable. The three agency emails mean (a) is no longer true — its recorded revisit trigger has fired. Is (b) still true, i.e., is TaskLite still operated by one person at a few hours per week with no plans for additional capacity?

(No other questions. Demand, prior rationale, and the revisit condition are already answered by the wiki; scope-shaping questions such as "flat workspace vs. roles" only become relevant after the delta question is answered, and the wiki already dictates the default answer — minimal operational surface — if the constraint still holds.)
