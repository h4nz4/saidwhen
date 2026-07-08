# RECOMMENDATION

Do not start building team workspaces yet — but do not dismiss the request either. This exact situation is governed by an existing accepted decision whose own revisit trigger has now fired.

The knowledge base records an accepted decision, **Single-user accounts** (`knowledge/decisions/single-user-accounts.md`, 2025-01-15), which explicitly rejected multi-user team workspaces on two grounds: (1) no user demand at the time, and (2) the solo-maintainer constraint makes multi-tenancy (roles, invitations, permissions, billing) unaffordable. Critically, the rejection includes a written revisit condition: *"Revisit if agencies or teams repeatedly request shared use."* Three design agencies emailing in one month is precisely that condition firing.

Per the project's provenance rules, a decision whose evidence has gone stale must be neither silently obeyed nor silently overridden. The demand half of the evidence is now demonstrably outdated (the decision is ~18 months old and the trigger fired); the constraint half (solo maintainer, a few hours per week) may or may not still hold, and it was the load-bearing reason for the rejection. So the correct next step is to formally re-open the decision by asking the human the delta questions below, then:

- **If the solo-maintainer constraint still holds:** propose the smallest viable middle ground rather than full multi-tenancy — e.g., a single shared workspace per account with all-members-equal access (no roles, no permission matrix, invitation = one email link), keeping ACC-2's isolation boundary at the workspace level instead of the user level. Full roles/permissions/billing tiers would remain rejected, consistent with the original reasoning.
- **If the constraint has changed** (more time, contributors, or revenue justifying it): a fuller team-workspace design becomes affordable and the decision should be superseded with new evidence.

Either way, the outcome should be captured as an updated/superseding decision in `knowledge/decisions/`, a new interview record, a log entry, and an update to `specs/accounts/spec.md` (ACC-1 and ACC-2 both cite the current decision and would need revision).

# PRIOR CONTEXT

- `E:\PROJEKTI\okf\example-stale\knowledge\index.md` — entry point; lists the relevant decision, constraint, and interview.
- `E:\PROJEKTI\okf\example-stale\knowledge\decisions\single-user-accounts.md` — accepted 2025-01-15: accounts are strictly single-user; multi-user team workspaces explicitly rejected due to no demand and solo-maintainer cost, with the revisit trigger "if agencies or teams repeatedly request shared use" — which the PM's report now satisfies.
- `E:\PROJEKTI\okf\example-stale\knowledge\constraints\solo-maintainer.md` — one person builds and operates TaskLite a few hours per week; every design choice must minimize operational surface. This was the decisive cost-side argument and its current validity is unknown.
- `E:\PROJEKTI\okf\example-stale\knowledge\interviews\2025-01-15-account-model.md` — Ivan (owner): users were individual freelancers, nobody had asked for team features ("If agencies ever start asking to use it with their teams, we'll revisit"), and "roles and permissions are where side projects go to die."
- `E:\PROJEKTI\okf\example-stale\specs\accounts\spec.md` — ACC-1 (single-user accounts) and ACC-2 (data isolation) both derive from the above decision and would need to change together with it.
- `E:\PROJEKTI\okf\example-stale\knowledge\log.md` — confirms no account-model activity since 2025-01-15; the decision is 18 months old.

# QUESTIONS

1. The single-user-accounts decision was made on 2025-01-15 because, at the time, users were individual freelancers and nobody had asked for team features — with an explicit note to revisit if agencies started asking. Three agencies have now asked. Do you agree the revisit trigger has fired and the decision should be re-opened?
2. The rejection's other pillar was the solo-maintainer constraint (recorded 2025-01-15: one person, a few hours per week, minimize operational surface). Is that still true today, or has your capacity/team changed?
3. If we proceed under a still-standing solo-maintainer constraint, is a minimal shared workspace (one team per account, all members equal, no roles/permissions/billing tiers) enough to satisfy the agencies' actual need — or did their emails indicate requirements (roles, client access, per-seat billing) that make a fuller design unavoidable?
