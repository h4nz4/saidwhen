# Evaluation: Real-time collaborative editing for TaskLite

## 1. RECOMMENDATION

Do not start building real-time collaborative editing yet. Recommend a scoped discovery step first, for three reasons:

**a) The prerequisite feature is missing, and it is the bigger one.** TaskLite is described as a task tracker *for freelancers*, and the only existing spec (authentication) models a single class of user with magic-link login. There is no concept of a client as a user, no sharing model, no workspace/project membership, and no permissions. "Freelancers working live with their clients" first requires: client accounts (or guest access), an invitation/sharing flow, and a permission model (can a client edit, or only view/comment?). That is a product decision layer that must be specified before any real-time transport is chosen.

**b) "Real-time collaborative editing" is likely over-scoped for the actual need.** True concurrent co-editing (CRDT/OT, cursor presence, conflict-free merging of a shared text field) is one of the most expensive features a small product can take on — it adds a stateful sync service, offline/conflict semantics, and a large testing surface. For a *task tracker* (short structured fields: title, status, due date, description), the underlying user need is usually satisfied by much cheaper mechanisms, in escalating order:
   1. Shared visibility: client can see the task list, updates appear on refresh.
   2. Live updates: server-pushed changes (WebSocket/SSE) so both parties see edits within seconds, with last-write-wins per field + optimistic locking on the description.
   3. Presence + comments: "Ana is viewing this task", threaded comments for the actual client conversation.
   4. Full co-editing of long-form fields only (e.g., the description), if evidence shows simultaneous typing is a real pain point.
   My recommendation is to target tier 2–3 and explicitly defer tier 4 until there is demonstrated demand. Most freelancer–client collaboration is asynchronous review-and-respond, not simultaneous typing.

**c) There is no implementation to attach this to.** The repository contains only a README and one spec file — no application code, no architecture to evaluate a sync engine against. The honest deliverable at this stage is a spec + decision record (e.g., `specs/collaboration/spec.md` plus a sharing/permissions addition to `specs/auth/`), not an engineering plan for a specific technology.

**Proposed path forward:**
1. Answer the scoping questions below with the PM.
2. Write `specs/sharing/spec.md` (client identity, invitations, permissions) — this stands alone and delivers value even without real-time.
3. Write `specs/collaboration/spec.md` covering live updates + presence + comments (tier 2–3), with explicit conflict-resolution rules per field type.
4. Record the decision to defer CRDT-style co-editing, with the trigger condition that would revisit it.
5. Only then evaluate transport/tech options (managed service vs. self-hosted WebSockets) against the actual, agreed requirements.

## 2. PRIOR CONTEXT

The project is nearly empty; I found and used:

- `E:\PROJEKTI\okf\example-control\README.md` — describes TaskLite as "a fictional lightweight task tracker for freelancers" and says every requirement should link to the decision that created it and every decision to the human answer that justified it. It references `knowledge/` and `specs/` directories, but **`knowledge/` does not exist** in this copy of the project, so no prior decisions or human answers were available to consult.
- `E:\PROJEKTI\okf\example-control\specs\auth\spec.md` — the only spec. Two requirements: AUTH-1 (magic-link login, no passwords) and AUTH-2 (sessions expire after 30 days of inactivity). Relevant because it implies a single-user-class model with no client/guest concept, and because magic-link auth shapes how client invitations would naturally work (email invite → magic link is a low-friction fit).

No prior decisions, ADRs, roadmap, or code exist that mention collaboration, sharing, clients-as-users, or real-time features. Nothing in the existing material either mandates or forbids this feature — it is entirely new scope.

## 3. QUESTIONS

1. **What is the actual pain point you've observed?** Is it clients not seeing task status without asking (visibility problem), slow feedback loops (communication problem), or two people literally overwriting each other's edits (concurrency problem)? Each points to a very different — and very differently priced — solution.
2. **Do clients need to *edit* tasks, or is view + comment enough?** If clients only need to see status and leave feedback, we can skip collaborative editing entirely.
3. **Who is a "client" in the account model?** Do they get full TaskLite accounts, or lightweight guest access scoped to shared tasks/projects (e.g., via a magic link, consistent with AUTH-1)? Does a client relationship span multiple projects?
4. **What permissions should the freelancer control?** Per-task or per-project sharing? Can clients create tasks, change statuses, edit descriptions, or only comment?
5. **What does "live" mean for you — seconds-fresh updates and presence indicators, or two cursors typing in the same text field simultaneously?** The first is a moderate feature; the second is an order of magnitude more work. Would you accept tier 2–3 (live updates + presence + comments) as the first release?
6. **Are there constraints I should know about** — target release window, budget appetite for a managed real-time service (e.g., hosted sync/WebSocket provider) vs. keeping everything self-hosted, and expected concurrent-user scale?
7. **Housekeeping:** the README references a `knowledge/` directory that doesn't exist in this repository. Is the decision history stored elsewhere, and should I have access to it before writing the new specs?
