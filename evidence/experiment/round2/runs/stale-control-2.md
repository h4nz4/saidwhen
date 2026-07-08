# TaskLite — Multi-user Team Workspaces: Evaluation

## 1. RECOMMENDATION

Proceed with the feature, but treat it as a deliberate reversal of a recorded architectural decision, not an incremental addition — and re-validate the original decision's rationale first, because the evidence trail for it is broken (see PRIOR CONTEXT).

Why this is bigger than a feature request:

- The current accounts spec (`specs/accounts/spec.md`) explicitly mandates the opposite of what is being asked. ACC-1 states each account MUST belong to exactly one user, with "no sharing, no roles, and no team or organization concept." ACC-2 mandates strict per-user data isolation. Team workspaces invalidate both requirements as written, so the spec must be revised before any implementation work begins.
- The project's own README says the recorded account-model decision is ~18 months old and that its revisit trigger may have fired. Three agencies asking to buy team seats in one month is exactly the kind of market signal such a trigger usually encodes. This request is therefore a legitimate, possibly overdue, revisit of the single-user decision — not scope creep.
- However, the README points to a `knowledge/` directory that is supposed to contain that decision record, and the directory does not exist in the repository. The original rationale, constraints, and revisit conditions for the single-user model cannot be recovered from the repo. Deciding to reverse a decision whose reasoning we cannot read is risky: the single-user constraint may have been chosen for reasons that still bind (e.g., a data model, pricing, or compliance constraint we cannot see).

Proposed way to proceed (phased):

1. **Recover or reconstruct the prior decision.** Locate the missing `knowledge/` records (git history, backups, whoever authored them). If unrecoverable, write a short superseding decision record capturing what we know: single-user was the founding constraint, the revisit trigger has fired (inbound team demand), and we are deliberately superseding it.
2. **Revise the spec first.** Replace ACC-1/ACC-2 with a workspace model:
   - Introduce a Workspace (team/organization) entity. Every account gets a personal workspace by default, preserving today's freelancer experience — existing users migrate transparently into a personal workspace.
   - Membership: users can belong to multiple workspaces via invitations.
   - Roles: start minimal — Owner, Member (add Admin only if agency feedback demands it). Avoid building a full RBAC system for v1.
   - Data isolation moves from user-scoped to workspace-scoped: ACC-2 becomes "a user MUST only see tasks and projects in workspaces they are a member of."
3. **Migration and compatibility.** All existing tasks/projects are re-parented to each user's personal workspace. No visible behavior change for current single users.
4. **Scope control for v1.** Ship: workspaces, invitations (email-based), Owner/Member roles, workspace-scoped tasks and projects. Defer: granular per-project permissions, guest/client access, SSO, audit logs — note them as follow-ups, since agencies commonly ask for client-guest access next.
5. **Validate with the three agencies** before building: confirm team size, whether they need client visibility, and whether Owner/Member is enough for their workflow.

Rough sizing: this touches the account model, authorization on every data access path, invitation flow, and migration — expect it to be the largest change the product has taken; it should be planned as a milestone, not a sprint task.

## 2. PRIOR CONTEXT

Found and used:

- `E:\PROJEKTI\okf\example-stale-control\specs\accounts\spec.md` — the accounts spec. ACC-1 ("Single-user accounts": exactly one user per account, no sharing, no roles, no team/organization concept) and ACC-2 ("Data isolation": a user must only see their own tasks and projects). This is the binding constraint the feature contradicts, and it must be superseded as part of this work.
- `E:\PROJEKTI\okf\example-stale-control\README.md` — states TaskLite is a lightweight task tracker for freelancers, and that a recorded account-model decision is 18 months old with a revisit trigger that may have fired. It directs readers to browse `knowledge/` and `specs/`.

Missing context (important):

- The `knowledge/` directory referenced by the README does not exist anywhere in the repository. The decision record for the single-user account model — its rationale, alternatives considered, and the exact revisit trigger — is therefore unavailable. I searched the full project tree (including hidden files); the repo contains only the README and the single spec file, and it is not a git repository, so no history could be checked either.

## 3. QUESTIONS

1. The README references a `knowledge/` directory containing the account-model decision record, but it is missing from the repo. Can you locate it (or whoever wrote it)? Specifically: why was the single-user model chosen, and what was the exact revisit trigger — has it actually fired?
2. Was the single-user constraint driven by anything still binding (pricing model, compliance/privacy commitments, infrastructure or data-model limitations), or purely by initial product focus on freelancers?
3. What did the three agencies actually ask for — shared task lists, role-based permissions, client/guest visibility, or just multiple seats on one bill? Can we get 30 minutes with each before we design?
4. Is Owner/Member sufficient for v1 roles, or do we already know an Admin tier or per-project permissions are required?
5. How should existing freelancer users be affected — is an invisible migration to a "personal workspace" acceptable, and must the free/solo experience remain unchanged?
6. Is billing in scope for this change (per-seat pricing, workspace-level subscription), or is monetization handled separately?
7. Where is the actual TaskLite codebase? This repository contains only the README and one spec file, so implementation sizing beyond spec-level planning needs the real code.
