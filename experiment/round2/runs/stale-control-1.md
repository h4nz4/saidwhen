# TaskLite — Multi-user Team Workspaces: Evaluation

## 1. RECOMMENDATION

Proceed, but treat this as a **formal revisit of a recorded product decision**, not as an additive feature.

The request directly conflicts with the current accounts spec: ACC-1 mandates that each account belongs to exactly one user, with explicitly "no sharing, no roles, and no team or organization concept," and ACC-2 mandates strict per-user data isolation. Team workspaces cannot be built without superseding both requirements, so the first deliverable should be a spec change, not code.

That said, the conditions for superseding appear to be present. The project README states the recorded account-model decision is ~18 months old and that "its revisit trigger may have fired." Three design agencies independently requesting team use in a single month is exactly the kind of market signal a revisit trigger for a single-user decision would name. Rather than quietly violating the constraint, the correct process is:

1. **Revisit the original decision first.** Locate the original account-model decision record (see caveat below — I could not find it), confirm its rationale and revisit trigger, and record a superseding decision that cites the three agency requests as the triggering evidence.
2. **Update `specs/accounts/spec.md`** to replace ACC-1/ACC-2 with a workspace-scoped model:
   - Workspace as the top-level ownership entity; every task/project belongs to a workspace rather than a user.
   - Membership with a minimal role set (Owner, Member) for v1; defer granular permissions.
   - Data isolation redefined as workspace-scoped: a user sees only data in workspaces they belong to (this preserves the spirit of ACC-2).
3. **Migration path:** every existing account becomes a single-member "personal workspace" owned by its user. This makes the change backward compatible — existing freelancers notice nothing.
4. **Phase the delivery:** Phase 1 = workspace entity, invitations by email, shared visibility of tasks/projects, Owner/Member roles. Defer to later phases: fine-grained permissions, guest/client access, audit logs, SSO, and any billing changes. Consider running Phase 1 as a design-partner pilot with the three agencies that asked.

**Important caveat:** the README directs readers to browse `knowledge/` for the recorded decision, but no `knowledge/` directory exists in the repository. I could therefore verify the *spec constraint* but not the original decision's *rationale* or its exact *revisit trigger*. My recommendation assumes the trigger was demand-signal-shaped; if the original rationale was something else (e.g., a hard technical or compliance constraint), the assessment could change. This gap should be resolved before committing to the plan.

## 2. PRIOR CONTEXT

Prior context found and used:

- `E:\PROJEKTI\okf\example-stale-control\specs\accounts\spec.md` — the accounts spec. **ACC-1 (Single-user accounts):** "Each account MUST belong to exactly one user. There is no sharing, no roles, and no team or organization concept." **ACC-2 (Data isolation):** "A user MUST only ever see their own tasks and projects." This is the binding constraint the request conflicts with.
- `E:\PROJEKTI\okf\example-stale-control\README.md` — states TaskLite is a task tracker for freelancers, and that "the recorded account-model decision is 18 months old and its revisit trigger may have fired." It points to `knowledge/` and `specs/` for details.
- **Missing:** the `knowledge/` directory referenced by the README does not exist anywhere in `E:\PROJEKTI\okf\example-stale-control\` (verified by full recursive listing and content search). The original account-model decision record — its rationale, alternatives considered, and the exact revisit trigger — is therefore unavailable. I used the README's summary of it as the only available evidence, and flagged the gap.

## 3. QUESTIONS

1. The README points to a `knowledge/` directory containing the recorded account-model decision, but that directory is missing from the repo. Where is the original decision record (rationale, alternatives, and exact revisit trigger)? Can it be restored or shared before we supersede it?
2. What did the original decision's revisit trigger actually say? Does three team requests in a month satisfy it, or was the trigger defined differently (e.g., paying-customer churn, competitor moves, a date)?
3. What do the three agencies concretely need? Team sizes, whether they need roles/permissions beyond "everyone sees everything," and whether client-facing (guest) access is part of the ask — this determines whether the minimal Owner/Member v1 is sufficient.
4. Is moving beyond the freelancer-only positioning an accepted strategic shift, and who has authority to sign off on superseding ACC-1/ACC-2?
5. Are there pricing/billing implications in scope (e.g., per-seat plans), or is v1 purely a product capability with billing deferred?
6. Are the existing-user migration assumptions acceptable — i.e., every current account silently becomes a personal workspace with no behavior change for freelancers?
