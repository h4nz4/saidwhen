# Evaluation: Real-time collaborative editing for TaskLite

## 1. RECOMMENDATION

**Do not commit to building full real-time collaborative editing yet.** Clarify the underlying user problem first, then deliver collaboration in stages — because in this codebase the feature has no foundation to stand on, and "live co-editing" is one of the most expensive interpretations of "work on tasks together."

Reasoning and proposed path:

**a. The project is not ready for this feature — prerequisites are missing.**
The current spec surface (see PRIOR CONTEXT) defines only authentication: magic-link login for a single user class, with 30-day sessions. There is no spec for:
- **Client accounts or roles.** "Clients" do not exist as a concept anywhere in the project. Before anything can be edited *with* a client, we need an identity/permission model: are clients full users, invited guests, or link-based viewers? This interacts directly with AUTH-1 (magic links could naturally extend to guest invites, which is a point in our favor).
- **Sharing/authorization.** No spec covers who may see or modify a task.
- **A task data model.** There is no tasks spec at all, so there is nothing yet that defines what "editing a task" means (title? description? status? comments?).

**b. Interrogate the request before choosing machinery.**
"Work on tasks live together" usually decomposes into needs that are much cheaper than character-level co-editing:
1. **Shared visibility** — the client can see the task list/status at all (requires sharing + roles only).
2. **Freshness** — changes appear without a manual refresh (server-push updates: SSE/WebSocket broadcasting "task changed, re-fetch"; last-write-wins per field).
3. **Awareness** — presence indicators, "Ana is viewing/editing this task."
4. **True concurrent text editing** — Google-Docs-style simultaneous typing in a task description (requires CRDT/OT, e.g., Yjs; persistent socket infrastructure; conflict handling; offline semantics; substantial testing).

For a lightweight freelancer task tracker, levels 1–3 likely deliver ~90% of the perceived value at ~20% of the cost. Tasks are small objects edited in short bursts, typically by two people who are rarely typing in the same field at the same instant. Level 4 should be pursued only if evidence shows real simultaneous-typing conflicts.

**c. Proposed staged plan:**
- **Phase 0 (spec work, required first):** Write specs for the task model, client identity/roles, and sharing/permissions. Extend the auth spec for client invitations (magic links fit well here).
- **Phase 1:** Task sharing + client access with clear permissions.
- **Phase 2:** Live updates via WebSocket/SSE with per-field last-write-wins, plus presence ("client is viewing") and optimistic UI. Add lightweight edit-locking or "X is editing" hints to avoid silent overwrites.
- **Phase 3 (only if validated by usage):** CRDT-based collaborative text editing (e.g., Yjs) scoped to the task description field only.

**d. Flag the positioning risk.** TaskLite is described as a *lightweight* tracker for freelancers. Real-time collaboration infrastructure (stateful socket servers, sync engines) meaningfully increases hosting cost and operational complexity, which may conflict with the product's lightweight positioning. This trade-off deserves an explicit product decision, recorded in the project's decision log.

## 2. PRIOR CONTEXT

The project contains very little prior context; everything found and used:

- `E:\PROJEKTI\okf\example-control\README.md` — Describes TaskLite as "a fictional lightweight task tracker for freelancers" demonstrating the Provenance Convention, and says to browse `knowledge/` and `specs/` where "every requirement links to the decision that created it." **Note:** the referenced `knowledge/` directory does not exist in this copy of the project, so no decision history or prior human answers were available to consult.
- `E:\PROJEKTI\okf\example-control\specs\auth\spec.md` — The only spec present. AUTH-1: magic-link login, no passwords stored. AUTH-2: sessions expire after 30 days of inactivity. Used to (a) infer that magic links can extend naturally to client invitations, and (b) confirm that no client/role/sharing concept exists yet.
- No source code, no other specs (no task model spec, no collaboration/sharing spec), no ADRs or decision records were found anywhere in the project.

Because the README promises decision provenance but the `knowledge/` directory is missing, I could not check whether real-time collaboration, client access, or a lightweight-architecture constraint was previously discussed or ruled out. This gap is itself a finding.

## 3. QUESTIONS

1. **What is the actual problem we're solving?** Have freelancers reported conflicts/staleness when editing simultaneously with clients, or is the pain more basic — that clients currently have no access to tasks at all? (This determines whether we need Phase 1, Phase 2, or Phase 3 as described above.)
2. **What does "editing together" mean concretely?** Do clients need to *modify* task content (title, description, status), or primarily *see* live status and add comments/approvals? Which fields, if any, must support simultaneous typing?
3. **Who are clients in the account model?** Should clients be full registered users (magic-link login per AUTH-1), invited guests scoped to specific tasks/projects, or anonymous share-link viewers? What may a client never do (e.g., delete tasks, see other clients' work, see rates/billing)?
4. **The README references a `knowledge/` directory with prior decisions that is missing from this copy — does that decision history exist elsewhere?** I'd like to check whether collaboration or architecture constraints were already decided before proposing specs.
5. **What are the operational constraints?** TaskLite is positioned as "lightweight" — is there an appetite for stateful real-time infrastructure (WebSocket servers, sync engine) and a managed-service budget, or must this stay deployable as a simple app?
6. **Scale and concurrency expectations:** typically how many people would be in one task at once (2, or more)? Is offline editing with later sync in scope?
7. **Priority and deadline:** is this driven by a specific customer commitment or competitive pressure that would justify jumping straight to a more advanced phase?
