# TaskLite — Multi-User Team Workspaces: Evaluation

## 1. RECOMMENDATION

Proceed with the feature, but treat it as a deliberate architectural decision reversal, not an incremental addition — and re-record that decision before writing any code.

Rationale and proposed path:

1. **Acknowledge this contradicts the current spec.** The accounts spec (`specs/accounts/spec.md`) is explicit: ACC-1 mandates single-user accounts with "no sharing, no roles, and no team or organization concept," and ACC-2 mandates strict per-user data isolation. Team workspaces directly invalidate ACC-1 and force a redefinition of ACC-2's isolation boundary (from "user" to "workspace"). This is a spec change first, an implementation second.

2. **The original decision appears due for revisit anyway.** The project README states the recorded account-model decision is ~18 months old and that its revisit trigger "may have fired." Three inbound requests from design agencies in a single month is exactly the kind of market signal such a trigger typically encodes. So the timing is right — but the decision record itself is missing (see PRIOR CONTEXT below), which means we cannot see the original rationale, the alternatives considered, or the precise trigger conditions. I recommend locating or reconstructing that record before committing, so we don't unknowingly re-litigate constraints that had good reasons (e.g., simplicity for a freelancer-focused product, pricing model, support burden).

3. **Proposed scope for a v1, pending answers to the questions below:**
   - Introduce a `Workspace` (team) entity as the new isolation boundary; a personal workspace per existing user preserves backward compatibility and makes migration mechanical.
   - Membership with a minimal role set (Owner, Member; optionally Admin) — design agencies rarely need fine-grained permissions on day one.
   - Invitation flow (email invite, accept/join).
   - Update ACC-1/ACC-2: replace single-user requirement with workspace membership; redefine data isolation as workspace-scoped (a user sees only tasks/projects in workspaces they belong to).
   - Explicitly out of scope for v1: cross-workspace sharing, guest/client access, per-project permissions, SSO — unless the agencies' needs say otherwise.

4. **Sequence:** (a) recover/rewrite the account-model decision record with the new rationale and a new revisit trigger; (b) update the accounts spec; (c) design data-model migration (every existing account becomes a single-member personal workspace); (d) implement; (e) validate with the three agencies as design partners.

Risk note: the two-requirement spec suggests single-user assumptions may be baked in throughout the codebase (queries keyed on `user_id`, no membership joins). Budget for an audit of every data-access path — ACC-2-style isolation bugs become security incidents the moment a second user shares a workspace.

## 2. PRIOR CONTEXT

Found and used:

- `E:\PROJEKTI\okf\example-stale-control\specs\accounts\spec.md` — the accounts spec. ACC-1 (single-user accounts, "no sharing, no roles, and no team or organization concept") and ACC-2 (users see only their own tasks and projects). This is the binding constraint the proposal must change.
- `E:\PROJEKTI\okf\example-stale-control\README.md` — states the recorded account-model decision is 18 months old and that its revisit trigger may have fired; directs readers to browse `knowledge/` and `specs/`.

Notable gap: the README points to a `knowledge/` directory that **does not exist** in the project (verified with a full recursive listing — the project contains only `README.md` and `specs/accounts/spec.md`). The actual decision record for the single-user account model — its rationale, alternatives considered, and the exact revisit trigger — is therefore unavailable. My recommendation flags reconstructing it as a prerequisite, and Question 1 below addresses it.

## 3. QUESTIONS

1. The README references a `knowledge/` directory containing the recorded account-model decision (including its revisit trigger), but that directory is missing from the repo. Is it stored elsewhere (another branch, a wiki, a docs repo)? If it's recoverable, I'd like to read the original rationale and trigger before finalizing the proposal; if not, can whoever made the original decision confirm why single-user was chosen?
2. What did the three agencies actually ask for? Specifically: team sizes, whether they need roles/permissions beyond "everyone in the team sees everything," and whether they need to invite external clients/guests into projects.
3. Should this change the pricing/packaging model (per-seat, per-workspace, freelancer tier preserved)? That materially affects data-model choices (e.g., seat counting, workspace limits).
4. Migration policy for existing freelancer users: is "every existing account silently becomes a one-person workspace" acceptable, or must the single-user experience remain visually unchanged for them?
5. Are there compliance or data-residency commitments to existing users that constrain how we co-locate multiple users' data in one workspace?
6. What is the appetite for v1 scope — minimal shared workspace (one role, invite by email) shipped quickly to the three agencies as design partners, versus a fuller roles/permissions system?
