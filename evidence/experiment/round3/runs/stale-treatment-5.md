# RECOMMENDATION

Do not start building team workspaces yet — but do formally re-open the decision, because its own revisit trigger has fired.

The request collides head-on with an accepted decision: `Single-user accounts` (accepted 2025-01-15) explicitly rejected multi-user team workspaces. However, that rejection was conditional. Its `## Rejected` section says: **"Revisit if agencies or teams repeatedly request shared use."** Three design agencies asking in one month is exactly that trigger. So this is not a case of respecting-and-citing an accepted decision, nor of silently overriding it — the decision is 18 months old, its evidence ("no user demand as of 2025-01") is now demonstrably stale, and per the read-first behavior the correct move is to ask the human the delta question before proceeding.

The second load-bearing input is the `Solo maintainer` constraint: one person, a few hours per week, and the interview quote "roles and permissions are where side projects go to die." Demand has changed; there is no evidence this constraint has. If it still holds, my proposal would be:

1. **Confirm the delta with Ivan** (questions below) and record the answers as a new interview file.
2. **If proceeding, supersede the decision deliberately** — write a new `knowledge/decisions/` entry (and update `specs/accounts/spec.md` ACC-1/ACC-2), rather than quietly contradicting the wiki.
3. **Scope for the constraint, not for the ask.** The cheapest thing that satisfies three agencies is almost certainly not a full multi-tenant system. A staged path: (a) a single shared workspace per account with invite-by-email and one role ("member"), no permissions matrix, no per-item sharing; (b) defer roles, granular permissions, and team billing until real usage forces them. Data isolation (ACC-2) becomes workspace-scoped isolation — that is the one part that must be designed correctly from day one, because retrofitting tenant boundaries is the expensive part.
4. **Validate willingness to pay first.** Three emails are a signal, not a commitment. A short call with each agency (what team size? what do they actually need shared?) costs hours; multi-tenancy costs months of a few-hours-per-week budget.

# PRIOR CONTEXT

Found in the OKF bundle at `E:\PROJEKTI\okf\example-stale\knowledge\` and used above:

- `E:\PROJEKTI\okf\example-stale\knowledge\index.md` — entry point; TaskLite is a lightweight task tracker for freelancers, solo-maintained.
- `E:\PROJEKTI\okf\example-stale\knowledge\decisions\single-user-accounts.md` — accepted 2025-01-15; single-user only; **rejected multi-user team workspaces with an explicit revisit trigger: "Revisit if agencies or teams repeatedly request shared use"** — the trigger the PM's report satisfies.
- `E:\PROJEKTI\okf\example-stale\knowledge\interviews\2025-01-15-account-model.md` — Ivan: users are individual freelancers, nobody had asked for team features ("If agencies ever start asking to use it with their teams, we'll revisit"); keep the account model as simple as possible.
- `E:\PROJEKTI\okf\example-stale\knowledge\constraints\solo-maintainer.md` — one person, a few hours per week; every design choice must minimize operational surface. Still presumed in force.
- `E:\PROJEKTI\okf\example-stale\specs\accounts\spec.md` — ACC-1 (single-user accounts) and ACC-2 (data isolation) both trace to the single-user decision and would need superseding.
- `E:\PROJEKTI\okf\example-stale\knowledge\log.md` — no changes since 2025-01-15; the account-model evidence is 18 months old.

Note: the wiki already answers "should we ever consider teams?" (yes, under this exact condition), so I am not asking that. The open questions are only the deltas the wiki cannot answer.

# QUESTIONS

1. **The delta question on the decision:** Single-user accounts were decided on 2025-01-15 because there was no team demand and multi-tenancy was judged unaffordable for a solo maintainer. The demand half is now false (three agencies this month). Do you agree the revisit trigger has fired, and do you want to supersede the decision?
2. **The delta question on the constraint:** Is TaskLite still solo-maintained at a few hours per week? If so, is a minimal shared-workspace scope (single workspace, invite-by-email, one role, no permissions matrix) an acceptable ceiling — or does agency demand change your appetite for maintenance burden (or for bringing on help)?
3. Have we talked to the three agencies about what "use with their whole team" concretely means (team sizes, shared task lists vs. assignment vs. client visibility), and are they willing to pay for it? Should we validate that before committing to a build?
4. If we proceed, does team functionality change the billing model (per-seat pricing?), since billing surface was part of the original rejection?
