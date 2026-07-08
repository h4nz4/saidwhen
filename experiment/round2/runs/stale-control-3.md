# TaskLite — Multi-User Team Workspaces: Evaluation

## 1. RECOMMENDATION

Proceed, but treat this as a deliberate revisit of a recorded architectural decision — not as an ordinary feature addition.

The current spec (`specs/accounts/spec.md`) explicitly forbids what is being asked for: ACC-1 mandates single-user accounts with "no sharing, no roles, and no team or organization concept," and ACC-2 defines data isolation at the individual-user boundary. Team workspaces therefore require amending the accounts spec itself before any implementation work begins. The README indicates the single-user account model was a recorded decision made roughly 18 months ago with a revisit trigger attached, and that the trigger "may have fired" — three design agencies independently requesting team use in one month is exactly the kind of market signal such a trigger would describe. So the decision is due for re-evaluation, and the demand evidence supports changing it.

Proposed path:

1. **Formally revisit and supersede the single-user decision.** Record a new decision (with rationale and the demand evidence from the three agencies) that replaces the 18-month-old one, rather than silently contradicting it.
2. **Amend the accounts spec first.** Replace ACC-1/ACC-2 with a workspace-centric model:
   - A *workspace* is the new ownership boundary for tasks and projects. Every account gets a personal workspace (preserving today's behavior for existing freelancer users — zero migration disruption for them).
   - A workspace has one or more *members*; membership carries a role (at minimum Owner/Admin/Member; keep the role set minimal for v1).
   - Data isolation (the successor to ACC-2) is redefined at the workspace boundary: a user sees only the tasks and projects of workspaces they belong to.
3. **Phase the implementation:**
   - **Phase 1 (MVP for the agencies):** workspace entity, invitations by email, shared visibility of tasks/projects within a workspace, minimal roles.
   - **Phase 2:** task assignment to members, per-project permissions if demand warrants, billing per seat.
4. **Keep the freelancer experience unchanged by default.** TaskLite's identity is "lightweight tracker for freelancers"; team features should be additive (a personal workspace that behaves exactly as today) so the core audience feels no added complexity.

Rough sizing: this is a foundational data-model change (ownership moves from user to workspace), so it touches auth, every query path, and likely pricing. It is a multi-week effort, not a quick feature — which is another reason to get the spec amendment agreed before writing code.

## 2. PRIOR CONTEXT

- `E:\PROJEKTI\okf\example-stale-control\specs\accounts\spec.md` — the governing accounts spec. ACC-1 (single-user accounts, explicitly "no team or organization concept") and ACC-2 (data isolation per user) directly conflict with the request and must be amended, not worked around.
- `E:\PROJEKTI\okf\example-stale-control\README.md` — states TaskLite is a lightweight task tracker for freelancers, and that the recorded account-model decision is 18 months old with a revisit trigger that may have fired. It points to `knowledge/` and `specs/` for details.
- **Missing context:** the README directs readers to a `knowledge/` directory, but no such directory exists in the project. The original decision record — its rationale for choosing single-user, and the exact wording of its revisit trigger — could not be found. My recommendation therefore infers the decision's existence and intent from the README and spec alone.

## 3. QUESTIONS

1. The README references a `knowledge/` directory containing the recorded account-model decision, but it does not exist in the repo. Where is that decision record (and its revisit trigger) kept? I want to confirm the original rationale for single-user and the trigger's exact conditions before formally superseding it.
2. What was the revisit trigger for the single-user decision? If it was something like "N team requests within a period," three agency requests in one month may satisfy it — but I'd like to verify rather than assume.
3. What team size are the three agencies talking about (3–10 people vs. 50+)? This determines whether a minimal roles model (Owner/Member) suffices for v1 or whether we need admin tooling from the start.
4. Is there a pricing/billing dimension to this (per-seat plans), or is monetization out of scope for the first iteration?
5. Do the agencies need collaboration features beyond shared visibility (task assignment, comments, activity feeds), or is "everyone on the team sees the same projects and tasks" enough for an MVP?
6. Are there existing-user migration constraints I should know about — e.g., must current freelancer accounts remain untouched, or is an automatic "personal workspace" wrapper acceptable?
