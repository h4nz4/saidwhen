# TaskLite — Multi-user Team Workspaces: Evaluation

## 1. RECOMMENDATION

Proceed — but treat this as a deliberate revision of a recorded product decision, not a routine feature addition.

The current spec directly forbids what is being asked. `specs/accounts/spec.md` requires ACC-1: "Each account MUST belong to exactly one user. There is no sharing, no roles, and no team or organization concept." Team workspaces cannot be built without superseding that requirement, so the first deliverable should be a spec change proposal, not code.

That said, the signal to revisit is strong and legitimate. The project README describes the single-user account model as a recorded decision that is ~18 months old and whose revisit trigger "may have fired" — three design agencies independently requesting team use in one month is exactly the kind of demand evidence that fires such a trigger. Important caveat: the README points to a `knowledge/` directory that should contain the decision record, but that directory does not exist in this checkout, so I could not read the original rationale or the exact revisit conditions. Before committing to a design, that record should be located (or confirmed lost), because the reason single-user was chosen matters: if it was scope/simplicity, we can proceed confidently; if it was a hard constraint (billing model, compliance, storage architecture), the cost picture changes.

Proposed approach, assuming the original decision was scope-driven:

- **Data model**: introduce a `Workspace` entity. Users join workspaces via a `Membership` (user, workspace, role). Tasks and projects belong to a workspace rather than directly to a user.
- **Preserve the isolation guarantee**: rewrite ACC-2 rather than delete it — isolation moves from "per user" to "per workspace": a user MUST only see data in workspaces they are a member of. The intent of ACC-2 survives; only the boundary changes.
- **Migration**: on rollout, every existing account gets an auto-created personal workspace containing its existing tasks/projects. Solo freelancers (the current user base) see zero behavior change.
- **Phasing**:
  - Phase 1 — workspaces, email invites, shared visibility, two roles (owner, member).
  - Phase 2 — finer permissions (admin role, per-project access) if demand warrants.
  - Phase 3 — external guest/client access, which design agencies very commonly need for client review; deliberately out of scope for v1 unless the agencies say otherwise.
- **Process**: supersede ACC-1 with a new recorded decision that documents the trigger (agency demand), the migration plan, and a new revisit condition; update `specs/accounts/spec.md` accordingly before implementation starts.

Rough risk assessment: the main costs are the tenancy migration (every query gains a workspace scope — this is where data-leak bugs live, so ACC-2's isolation guarantee needs explicit test coverage) and the pricing/billing implications of multi-seat use, which are product decisions outside the spec as it stands.

## 2. PRIOR CONTEXT

- `E:\PROJEKTI\okf\example-stale-control\specs\accounts\spec.md` — the accounts spec. ACC-1 mandates single-user accounts with no sharing, roles, or team/organization concept; ACC-2 mandates that a user must only ever see their own tasks and projects. This is the requirement the new feature conflicts with, and ACC-2 is the guarantee that must be preserved in workspace-scoped form.
- `E:\PROJEKTI\okf\example-stale-control\README.md` — states that the recorded account-model decision is 18 months old and "its revisit trigger may have fired," and directs the reader to `knowledge/` and `specs/`.
- **Missing context (relevant negative finding)**: the `knowledge/` directory referenced by the README does not exist in this project checkout. The original decision record — its rationale for single-user and its exact revisit trigger — could not be found. I searched the full project tree; the only files present are the README and the accounts spec. My recommendation therefore relies on the spec text and the README's summary, not on the underlying decision record.

## 3. QUESTIONS

1. The README references a decision record under `knowledge/`, but that directory doesn't exist in the repo. Where is the original account-model decision record (its rationale and revisit trigger), or has it been lost? Can someone share it before we finalize the design?
2. Was single-user chosen purely for scope/simplicity, or were there harder constraints (billing model, data architecture, compliance) that would make multi-tenancy expensive to retrofit?
3. For the three agencies: is a flat "all workspace members see all workspace tasks/projects" model acceptable for v1, or do they need roles/permissions beyond owner vs. member from day one?
4. Do the agencies need external client/guest access (common for design agencies sharing progress with clients), or is this strictly internal-team collaboration for now?
5. Should existing solo accounts be silently migrated into personal workspaces (my recommendation), or do you want single-user mode kept as a distinct product tier — and relatedly, is per-seat pricing planned, since that affects how memberships are modeled?
