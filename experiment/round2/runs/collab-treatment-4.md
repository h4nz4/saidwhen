# RECOMMENDATION

Do not build real-time collaborative editing (live cursors, CRDT/OT co-editing over WebSockets) as requested. It directly conflicts with two accepted, current constraints in the knowledge base:

1. **Solo maintainer** (`knowledge/constraints/solo-maintainer.md`): TaskLite is built and operated by one person a few hours per week, and the owner explicitly said "Anything that can break at 3am is out" (`knowledge/interviews/2026-07-08-auth-scope.md`). A real-time collaboration stack — persistent WebSocket connections, a presence/sync server, conflict-resolution logic (CRDT or OT), reconnection handling, and scaling stateful connections — is one of the highest operational-surface features a web app can take on. It is exactly the kind of thing that breaks at 3am.

2. **Users are external freelancers** (`knowledge/constraints/external-users.md`): today TaskLite's user base is individual freelancers only. "Clients" are not currently a user class at all. Making clients live collaborators means onboarding a second user population — invitations, per-task access control, and authentication for people who never signed up. Any client auth must follow the accepted magic-link decision (`knowledge/decisions/magic-link-auth.md`, status: accepted, decided today, 2026-07-08): no passwords, no OAuth. That decision is fresh and its evidence is current, so I respect it rather than re-litigating it.

**What I propose instead — a staged approach that delivers most of the client-collaboration value at a fraction of the operational cost:**

- **Stage 1 (low risk, ship first): shared task visibility.** A freelancer can share a task or project with a client. Client access is via emailed magic link (consistent with the accepted auth decision), scoped to the shared items. Clients can view status and add comments. This covers the dominant freelancer–client workflow ("can my client see progress and give feedback?") with plain request/response — no new infrastructure.
- **Stage 2 (still low risk): near-real-time freshness without WebSockets.** Lightweight polling or SSE to refresh shared views every few seconds, plus optimistic locking / last-write-wins with a visible "X updated this task just now" indicator to handle the rare concurrent edit. Tasks are short structured records (title, status, due date, notes), not long documents — true character-level co-editing has little payoff here.
- **Stage 3 (only if validated demand): managed real-time service.** If, after Stages 1–2, users demonstrably need live co-presence, adopt a fully managed sync provider (e.g., Liveblocks, PartyKit/Cloudflare, Ably, or Yjs on a managed backend) rather than self-hosting sync infrastructure, so the always-on stateful component is someone else's pager. This still adds cost and a vendor dependency, so it needs explicit owner sign-off against the solo-maintainer constraint.

I recommend committing only to Stage 1 now, and recording the decision (with the real-time rejection rationale) in `knowledge/decisions/` once the owner confirms scope.

# PRIOR CONTEXT

Found via `knowledge/index.md` (E:\PROJEKTI\okf\example\knowledge\index.md) and followed to:

- **E:\PROJEKTI\okf\example\knowledge\constraints\solo-maintainer.md** — one person builds and operates TaskLite a few hours per week; every design choice must minimize operational surface. This is the primary blocker for self-hosted real-time infrastructure.
- **E:\PROJEKTI\okf\example\knowledge\constraints\external-users.md** — users are individual freelancers; no corporate identity provider. Shapes how client access must work (no SSO to lean on; clients arrive with nothing but an email address).
- **E:\PROJEKTI\okf\example\knowledge\interviews\2026-07-08-auth-scope.md** — owner's own words: "Anything that can break at 3am is out" and "don't store passwords, I don't want the liability." Both directly constrain the collaboration design and client-auth approach.
- **E:\PROJEKTI\okf\example\knowledge\decisions\magic-link-auth.md** — accepted 2026-07-08, evidence fresh (same day). Magic links only; OAuth and passwords rejected. Respected, not re-litigated: client access in my proposal reuses magic links.
- **E:\PROJEKTI\okf\example\specs\auth\spec.md** — AUTH-1 (magic-link login, no passwords) and AUTH-2 (30-day session expiry). Any client-facing sessions must conform; the 30-day inactivity expiry likely needs a shorter variant for client share links (question below).
- **E:\PROJEKTI\okf\example\knowledge\log.md** — confirms all of the above were created today (2026-07-08), i.e., none of the evidence is stale, so no delta questions about staleness are warranted.

The wiki already answers "do clients need SSO?" (no — no corporate IdP exists) and "how much operational load can we absorb?" (essentially none), so I am not asking those.

# QUESTIONS

1. **What is the actual job to be done?** When you say freelancers "work on tasks live together with their clients," do clients need to *edit* tasks concurrently (change titles, statuses, descriptions at the same moment), or is the real need that clients can *see current status and comment* without emailing back and forth? Stage 1 covers the latter; only genuine concurrent editing justifies anything beyond it.

2. **Do clients become accounts?** Should a client be a first-class TaskLite user (magic-link login, sees all tasks shared with them across freelancers), or is per-share, link-scoped guest access enough? This determines the size of the auth and data-model change.

3. **What may clients change?** Comments only? Task status? Full edit rights on shared tasks? (This sets the permission model and how much conflict handling we need at all.)

4. **Session length for clients:** AUTH-2 mandates 30-day inactivity expiry for users. Are shorter-lived client share sessions (e.g., 7 days, re-request via email) acceptable, or should clients get the same 30 days?

5. **If Stage 3 ever happens:** is a paid managed real-time service (vendor dependency, monthly cost, data flowing through a third party) acceptable in principle, given the solo-maintainer constraint rules out self-hosting sync infrastructure? A "no" here caps the roadmap at Stage 2, which is worth knowing before we design.
