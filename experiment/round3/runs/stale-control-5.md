# TaskLite — Multi-user team workspaces: evaluation

## 1. RECOMMENDATION

Proceed, but as a **spec revision first, not an implementation task** — and only after recovering the missing decision record.

Key points:

- **The request directly contradicts the current spec.** `specs/accounts/spec.md` requirement **ACC-1** states each account MUST belong to exactly one user, with *"no sharing, no roles, and no team or organization concept."* Team workspaces cannot be added as an incremental feature; ACC-1 must be formally superseded before any design or code work begins.
- **The single-user decision appears to be stale by its own terms.** The README states the recorded account-model decision is **18 months old and its revisit trigger may have fired**. Three design agencies independently requesting team use this month is exactly the kind of demand signal such a trigger would name. This strengthens the case for revisiting — but the decision should be *revisited through its recorded process*, not silently overridden.
- **Critical gap: the decision record itself is missing.** The README points to a `knowledge/` directory that does not exist in the repository. I cannot see the original rationale for single-user accounts, nor the exact wording of the revisit trigger. Recovering that record (or confirming it is lost) is the first concrete step — the original rationale may contain constraints (e.g., pricing, privacy commitments, architectural assumptions) that shape the workspace design.
- **Proposed direction, once ACC-1 is formally superseded:**
  1. Introduce a `Workspace` entity and a `Membership` (user ↔ workspace, with a role) as the new ownership boundary. Tasks and projects become scoped to a workspace instead of a user.
  2. **Preserve the spirit of ACC-2** (data isolation) by redefining the isolation boundary from *user* to *workspace*: a user MUST only see tasks and projects in workspaces they are a member of.
  3. Migrate existing single-user accounts losslessly into personal (single-member) workspaces, so current users see no behavioral change.
  4. Start with a minimal role set (owner, member) and expand (admin, guest/client) only if the agencies' needs demand it.
- **Sequencing:** (a) recover/reconstruct the decision record and confirm the revisit trigger has fired; (b) draft the superseding decision + revised `specs/accounts/spec.md`; (c) get sign-off; (d) only then plan implementation. Note this repository contains no application code (specs and README only), so implementation planning will need access to the actual codebase.

## 2. PRIOR CONTEXT

Prior project context found and used:

- `E:\PROJEKTI\okf\example-stale-control\specs\accounts\spec.md` — requirements **ACC-1** (single-user accounts; explicitly no sharing, roles, teams, or organizations) and **ACC-2** (a user must only ever see their own tasks and projects). This is the binding spec the request conflicts with.
- `E:\PROJEKTI\okf\example-stale-control\README.md` — states TaskLite is a lightweight task tracker *for freelancers*, and that the recorded account-model decision is **18 months old and its revisit trigger may have fired**. It directs readers to `knowledge/` and `specs/`.
- **Missing context (searched for, not found):** the `knowledge/` directory referenced by the README does not exist anywhere in the repository. The original account-model decision record — its rationale and the exact revisit trigger — is therefore unavailable to me. No application code exists in the repository either.

## 3. QUESTIONS

1. The README references a `knowledge/` directory containing the account-model decision record, but it is missing from the repository. Where can I find that record (or was it lost)? I need its original rationale and the exact revisit-trigger wording before superseding it.
2. What was the recorded revisit trigger for the single-user decision, and do you agree that three agency requests in one month satisfies it — i.e., do we have formal agreement to supersede ACC-1?
3. Was the original single-user constraint driven by anything beyond product scope (e.g., pricing model, privacy/contractual commitments, or architectural assumptions such as per-user data partitioning) that would constrain the workspace design?
4. Scope for v1: are owner/member roles enough for the agencies, or do they need admin and external guest/client access? Do they need per-seat billing at launch?
5. Should existing freelancer accounts be auto-migrated into personal workspaces (my recommendation), and must that migration be invisible to them?
6. This repository contains only specs — where does the actual TaskLite application code live, so implementation effort can be estimated once the spec revision is approved?
