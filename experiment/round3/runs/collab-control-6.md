# RECOMMENDATION

Do not commit to "real-time collaborative editing" as scoped — the request as phrased implies the heaviest possible interpretation (Google-Docs-style concurrent text editing with CRDT/OT machinery, WebSocket infrastructure, presence indicators), and nothing in the project as it stands justifies or even supports that yet. I recommend proceeding in deliberately smaller steps:

1. **Clarify the underlying need first.** "Work on tasks live together" is usually satisfied by something far simpler than character-level co-editing. In practice, freelancer↔client collaboration on a task tracker most often means: (a) both parties see task changes reflected without refreshing, (b) both can comment/discuss on a task, and (c) conflicting edits don't silently destroy each other. That is live sync, not collaborative editing, and it is roughly an order of magnitude cheaper to build and maintain.

2. **Resolve the prerequisite gap: clients are not currently users.** The only existing spec (`specs/auth/spec.md`) defines magic-link login and 30-day session expiry for users generally; there is no concept of a client role, task sharing, invitations, or per-task permissions anywhere in the specs. Before any real-time work, we need a sharing/authorization spec: how a client gets access to a freelancer's tasks (magic-link account? guest share link?), and what they may see and edit. Real-time transport is pointless until two parties can legitimately look at the same task.

3. **Propose a phased plan, gated on the answers to the questions below:**
   - **Phase 0 — Sharing & permissions spec** (new `specs/sharing/spec.md`): client invitation via the existing magic-link mechanism (keeps AUTH-1 intact, no passwords introduced), role-based access (owner vs. client), field-level edit rights.
   - **Phase 1 — Live sync**: server-pushed updates (WebSocket or SSE) so both parties see task state changes in near real time; optimistic UI with per-field last-write-wins plus edit-conflict surfacing ("Client updated this while you were editing"); presence indicator ("client is viewing this task"). This delivers most of the perceived "live together" value.
   - **Phase 2 (only if validated)** — true concurrent editing of long-form task descriptions using an off-the-shelf CRDT library (e.g., Yjs) rather than a homegrown OT implementation. Scope it to the description field only, not the whole task object.

4. **Follow the project's own convention.** The README states this project demonstrates the Provenance Convention: every requirement links to the decision that created it, and every decision links to the human answer justifying it. So the correct next step is not code — it is getting the PM's answers to the questions below recorded, deriving decisions from them, and writing the spec deltas with those links before implementation. Note that the referenced `knowledge/` directory does not exist in this working copy, which itself needs resolving (see Questions).

5. **Flag the cost honestly.** Real-time infrastructure changes the operational profile of a "lightweight" tracker: persistent connections, stateful servers or a pub/sub layer, harder debugging, and ongoing hosting cost. If TaskLite's positioning is "lightweight for freelancers," Phase 2 may be permanently out of scope, and that would be a fine outcome.

# PRIOR CONTEXT

The project is nearly empty — it contains exactly two files and no source code:

- `E:\PROJEKTI\okf\example-control\README.md` — describes TaskLite as "a fictional lightweight task tracker for freelancers" used to demonstrate the Provenance Convention, and says to browse `knowledge/` and `specs/` where "every requirement links to the decision that created it, and every decision links to the human answer that justified it."
- `E:\PROJEKTI\okf\example-control\specs\auth\spec.md` — the only spec. Two requirements: **AUTH-1** (magic-link login, single-use links, no passwords stored) and **AUTH-2** (sessions expire after 30 days of inactivity). It contains no provenance links despite the README's claim.

Notable absences that shaped the recommendation:

- The `knowledge/` directory referenced by the README **does not exist**, so no decision history or prior human answers were available to consult. I could not find any prior decision about collaboration, sharing, clients, or real-time features.
- There are no specs for tasks themselves, sharing, permissions, or client access — so "clients" have no defined existence in the system yet.
- There is no implementation code, so no technology stack constrains (or informs) the real-time architecture choice.

# QUESTIONS

1. When you say freelancers and clients "work on tasks live together," what does that concretely look like? Is it (a) both seeing task changes appear instantly without refreshing, (b) commenting/chatting on a task in real time, or (c) literally typing in the same text field simultaneously like Google Docs? Which of these is the actual user need you've heard?
2. Clients don't exist in the product today. How should a client get access — a full magic-link account (per AUTH-1), or a lighter-weight guest share link per task/project? And do share links change our "no passwords, single-use magic links" security posture?
3. What may a client do once they have access — view only, comment only, edit specific fields (e.g., status, description), or full edit rights equal to the freelancer?
4. What concurrency scale are we designing for — is this 1 freelancer + 1 client per task (the common case), or do we need to support larger groups?
5. What are the conflict expectations? If both parties edit the same task while one is offline or on a flaky connection, is "last write wins with a visible warning" acceptable, or must no keystroke ever be lost?
6. Is there an existing implementation/stack elsewhere (this repo has specs only, no code)? Any hosting or budget constraints that would rule out persistent WebSocket infrastructure?
7. What's the priority/deadline driving this — a specific customer request, a competitive gap, or exploratory? That determines whether we stop at Phase 1 (live sync) or plan for Phase 2 (CRDT co-editing).
8. Housekeeping: the README points to a `knowledge/` directory that doesn't exist in this working copy, and the auth spec has no provenance links. Is that directory missing by accident, and should decisions from this initiative seed it?
