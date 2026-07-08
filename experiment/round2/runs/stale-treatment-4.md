# RECOMMENDATION

Do not start building team workspaces yet — but do formally reopen the decision, because its own revisit trigger has fired.

The request collides with an existing accepted decision: [Single-user accounts](../../../example-stale/knowledge/decisions/single-user-accounts.md) (`status: accepted`, 2025-01-15). That decision explicitly rejected multi-user team workspaces on two pieces of evidence:

1. **No user demand** — "nobody has asked for team features" (interview, 2025-01-15). This evidence is now stale: the decision itself said "**Revisit if agencies or teams repeatedly request shared use**," and three design agencies asking in one month is exactly that trigger firing. The demand half of the decision no longer holds.
2. **Solo maintainer** — multi-tenancy (roles, invitations, permissions, team billing) was judged "the single largest complexity multiplier a task tracker can take on" for one person working a few hours a week. This evidence is a standing constraint, not a data point, and I have no signal that it has changed.

So the situation is: the revisit condition is met, but the cost side of the original rejection likely still applies. Per the project's provenance rules I should neither silently obey the old decision (ignoring three agencies would ignore the trigger the decision itself set) nor silently override it (shipping multi-tenancy against a live solo-maintainer constraint). The right move is to ask the human the delta question first (see QUESTIONS), then decide.

If the constraint is confirmed still true, my proposal for the reopened decision would be a staged approach rather than a binary yes/no:

- **Stage 0 (now, cheap): validate the demand.** Reply to the three agencies and find out what "use with their whole team" concretely means — shared task lists? assignment? just multiple logins under one invoice? Willingness to pay? Three emails is a trigger, not a specification.
- **Stage 1 (if validated): smallest viable sharing.** A single flat "workspace" where every member sees everything — no roles, no permissions, no per-item ACLs. This honors the spirit of the interview ("roles and permissions are where side projects go to die") while breaking only the part of the decision whose evidence expired. Spec impact: `specs/accounts/spec.md` ACC-1 (one user per account) and ACC-2 (strict per-user data isolation) would both need rewriting — data isolation would move from per-user to per-workspace.
- **Explicitly out of scope for the reopened decision:** roles/permissions tiers, per-project sharing, admin hierarchies, SSO. Those remain rejected under the solo-maintainer constraint unless that constraint itself changes.

Whatever the human decides, the outcome should be captured as a new/updated Decision in `knowledge/decisions/` with the new interview answers in `knowledge/interviews/`, a log line in `knowledge/log.md`, and ACC-1/ACC-2 updated to link the new provenance. (I have not written any of these — this task is evaluation-only.)

# PRIOR CONTEXT

Found and used, all under `E:\PROJEKTI\okf\example-stale\`:

- `knowledge/index.md` — entry point; TaskLite is a lightweight task tracker for freelancers, solo-maintained.
- `knowledge/decisions/single-user-accounts.md` — the accepted decision directly on point: single-user accounts only; multi-user team workspaces explicitly rejected ("no user demand as of 2025-01"; unaffordable for a solo maintainer), with the revisit trigger "Revisit if agencies or teams repeatedly request shared use." Timestamp 2025-01-15 — 18 months old as of today (2026-07-08).
- `knowledge/interviews/2025-01-15-account-model.md` — the evidence behind the decision: users are individual freelancers, nobody had asked for team features, "if agencies ever start asking to use it with their teams, we'll revisit"; and "I'm one person; roles and permissions are where side projects go to die."
- `knowledge/constraints/solo-maintainer.md` — standing constraint: one person builds and operates TaskLite a few hours per week; every design choice must minimize operational surface.
- `knowledge/log.md` — confirms nothing has changed in the knowledge base since 2025-01-15; no newer decision supersedes single-user accounts.
- `specs/accounts/spec.md` — ACC-1 (single-user accounts) and ACC-2 (per-user data isolation), both tracing their "why" to the single-user-accounts decision; these are the requirements the feature would break.

The wiki already answers several questions I therefore did not ask: whether team features were previously considered (yes — considered and rejected), why (no demand + solo-maintainer complexity), and under what condition to revisit (repeated agency/team requests — now met).

# QUESTIONS

Only the delta questions — the parts of the old evidence that time may have invalidated:

1. The single-user decision was made on 2025-01-15 partly because TaskLite is solo-maintained a few hours per week, and multi-tenancy was judged unaffordable at that capacity. **Is that still true today — are you still the sole maintainer at roughly the same hours, or has capacity (or willingness to grow it for paying teams) changed?**
2. The decision's revisit trigger was "agencies or teams **repeatedly** request shared use." Three agencies in one month looks like the trigger firing. **Do you agree the trigger has fired, and do you want to formally reopen the decision?**
3. If reopened: **would a minimal flat shared workspace (everyone sees everything, no roles or permissions) satisfy what these agencies are asking for, or have they specifically asked for roles/permissions?** This determines whether the "roles are where side projects go to die" boundary from your interview can be preserved.
