# RECOMMENDATION

Do not start building multi-user team workspaces yet — but do formally reopen the single-user-accounts decision, because its own revisit trigger has now fired.

The knowledge base contains an accepted decision, `single-user-accounts` (2025-01-15), which rejected multi-user team workspaces on two grounds: (1) no user demand at the time, and (2) multi-tenancy is unaffordable for a solo maintainer. Crucially, the rejection carries an explicit revisit condition: **"Revisit if agencies or teams repeatedly request shared use."** Three design agencies asking in one month is precisely that condition. So this is not a case of re-litigating a settled decision, nor of silently overriding it — the decision is 18 months old, its demand-side evidence is demonstrably stale, and the recorded trigger obligates a re-evaluation.

However, only half the evidence is stale. The demand premise ("nobody has asked for team features") is now false. The cost premise — the solo-maintainer constraint ("roles and permissions are where side projects go to die") — may still be fully true, and it was the stronger of the two reasons. Demand alone does not make multi-tenancy affordable.

Proposed path:

1. Confirm with the owner whether the solo-maintainer constraint still holds (see QUESTIONS). This is the delta question required before proceeding.
2. If the constraint still holds, favor the smallest thing that captures agency demand without full multi-tenancy, in roughly this order of preference:
   - **Do nothing / waitlist**: reply to the agencies, gauge willingness to pay, collect requirements. Zero build cost, converts demand into evidence.
   - **Shared workspace, no roles**: one account usable by a whole team (shared login or simple member list, everyone equal, no permissions, no invitations flow, no per-seat billing). Violates ACC-1 minimally while avoiding the roles/permissions surface Ivan explicitly feared.
   - **Full multi-tenancy** (organizations, invitations, roles, per-seat billing): only if the constraint has materially changed (more time, revenue to fund it, or a co-maintainer), because this is the exact complexity multiplier the decision rejected.
3. Whatever is decided, update the knowledge base: supersede or amend `decisions/single-user-accounts.md`, record the new owner answers as an interview, update `specs/accounts/spec.md` (ACC-1/ACC-2 both hinge on the old decision), and append to `log.md`.

# PRIOR CONTEXT

Found and used, all under `E:\PROJEKTI\okf\example-stale\`:

- `knowledge\index.md` — entry point; TaskLite is a task tracker for freelancers, solo-maintained; links to the decision, constraint, and interview below.
- `knowledge\decisions\single-user-accounts.md` — accepted 2025-01-15. Accounts are strictly single-user; multi-user team workspaces explicitly rejected ("no user demand as of 2025-01", permission/invitation/billing surface unaffordable for a solo maintainer), with the revisit trigger: "Revisit if agencies or teams repeatedly request shared use." That trigger has now fired.
- `knowledge\constraints\solo-maintainer.md` — one person builds and operates TaskLite a few hours per week; every design choice must minimize operational surface. This constraint is independent of demand and may still hold.
- `knowledge\interviews\2025-01-15-account-model.md` — Ivan (owner): users are individual freelancers, nobody had asked for team features; "If agencies ever start asking to use it with their teams, we'll revisit"; "roles and permissions are where side projects go to die."
- `knowledge\log.md` — confirms all three artifacts date from 2025-01-15; nothing newer exists (the decision is ~18 months old).
- `specs\accounts\spec.md` — ACC-1 (single-user accounts) and ACC-2 (data isolation) both cite the single-user-accounts decision as their "why"; both would need revision if the decision changes.

Per the read-first behavior: the decision's evidence is stale on the demand side, so I am neither silently obeying nor silently overriding it — I am asking only the delta questions below.

# QUESTIONS

1. The single-user decision was made on 2025-01-15 partly because "nobody has asked for team features" — that part is clearly no longer true. The other reason was the solo-maintainer constraint: you build and run TaskLite alone, a few hours per week, and said roles/permissions are unaffordable at that capacity. **Is that still true today**, or has your capacity changed (more time, revenue to fund the work, a collaborator)?

2. In January 2025 you said "if agencies ever start asking to use it with their teams, we'll revisit." Three agencies asked this month. **Do you want to formally reopen the decision now**, and if so, is a minimal shared-workspace model (one shared team space, no roles/permissions/invitations) an acceptable middle ground, or is it full multi-tenancy or nothing?

3. Have any of the three agencies indicated **willingness to pay** for team use? If team workspaces would come with revenue, that changes what maintenance burden is affordable and which option in the recommendation applies.
