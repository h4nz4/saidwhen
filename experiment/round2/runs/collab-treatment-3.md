# RECOMMENDATION

Do not build real-time collaborative editing (CRDTs/OT, WebSockets, presence, live cursors) as requested. It directly conflicts with an active, freshly-evidenced project constraint, and the underlying need it serves is not yet established.

Reasoning:

1. **Operational surface conflict.** TaskLite is built and operated by one person, a few hours per week, and "every design choice must minimize operational surface" (`knowledge/constraints/solo-maintainer.md`). The owner's own words in the scoping interview: "Anything that can break at 3am is out" (`knowledge/interviews/2026-07-08-auth-scope.md`). Real-time collaborative editing is close to the maximum-operational-surface feature a web app can have: a persistent stateful WebSocket layer, conflict-resolution machinery (CRDT or OT), presence/awareness state, reconnection and offline-merge edge cases, and horizontal-scaling complications. It is precisely the class of thing that breaks at 3am. The constraint is dated today (2026-07-08), so its evidence is current — per project convention I respect it and cite it rather than re-litigate it.

2. **The premise smuggles in a new user class.** The request assumes clients are TaskLite users. The knowledge base says users are individual freelancers (`knowledge/constraints/external-users.md`); clients-as-users appears nowhere in decisions, constraints, or interviews. Whether clients get accounts at all is a bigger product decision than the editing mechanism, and it should be decided (and captured as a Decision) first. Positive note: if clients do become users, the accepted magic-link auth decision (`knowledge/decisions/magic-link-auth.md`) extends to them cleanly — clients are also external individuals with no corporate IdP — so auth would not need re-litigating.

3. **Propose the cheap 80% instead.** Most "work on tasks live together with clients" value can be delivered with near-zero new operational surface, in escalating order:
   - **Level 0 — Read-only share links:** a client views a task/board via a tokenized link (mechanically similar to the existing magic-link flow). No accounts, no realtime infra.
   - **Level 1 — Client accounts + comments:** clients log in via the same magic-link auth and can comment on shared tasks. Async collaboration; plain CRUD.
   - **Level 2 — Freshness without realtime:** short-interval polling or SSE to refresh task state, plus optimistic concurrency (version check on save with a "this task changed, reload" prompt). Feels live for task-tracker granularity; no conflict-resolution machinery, since tasks are small structured records, not documents.
   - **Level 3 (only if evidence demands it) — true concurrent editing** via a managed realtime service (e.g., Liveblocks/Ably/PartyKit) rather than self-hosted infra, to keep the 3am surface on someone else's pager. This still adds cost, a vendor dependency, and client-side complexity, so it needs demonstrated user demand first.

   My concrete proposal: pursue Levels 0–1 now (pending answers to the questions below), design saves to be conflict-safe (Level 2's version check is a few lines), and defer Level 3 until a real user asks for simultaneous editing. If accepted, capture this as `knowledge/decisions/client-collaboration.md` with the realtime option in the `## Rejected` section, record the PM/owner answers as an interview file, and update `log.md` and `index.md`.

# PRIOR CONTEXT

Found and used, all under `E:\PROJEKTI\okf\example\knowledge\` (entry point per the read-first behavior):

- `E:\PROJEKTI\okf\example\knowledge\index.md` — knowledge base entry point; TaskLite is a lightweight task tracker for freelancers, solo-maintained.
- `E:\PROJEKTI\okf\example\knowledge\constraints\solo-maintainer.md` — one person builds and operates TaskLite a few hours per week; every design choice must minimize operational surface. Directly governs this request.
- `E:\PROJEKTI\okf\example\knowledge\constraints\external-users.md` — users are individual freelancers, no corporate identity provider. Relevant because the request introduces clients as a possible new user class.
- `E:\PROJEKTI\okf\example\knowledge\interviews\2026-07-08-auth-scope.md` — owner (Ivan) interview: "I'm the only maintainer... Anything that can break at 3am is out." Primary evidence for the operational-surface argument; also answers, in advance, any question about SSO for client accounts.
- `E:\PROJEKTI\okf\example\knowledge\decisions\magic-link-auth.md` — accepted 2026-07-08: magic-link auth, no passwords, no OAuth. Fresh and plausible; respected, not re-litigated. Reused as the auth mechanism for any new client-facing sharing/accounts.
- `E:\PROJEKTI\okf\example\knowledge\log.md` — change history; confirms all decisions/constraints were created today, i.e., evidence is current, not stale.
- `E:\PROJEKTI\okf\example\specs\auth\spec.md` — AUTH-1 (magic-link login) and AUTH-2 (30-day session expiry); any client access mechanism must fit these requirements.
- `E:\PROJEKTI\okf\example\README.md` — project overview (provenance convention demo).

Deliberately NOT asked because the wiki already answers them: "Should client accounts use SSO/social login?" (no — external individuals, no corporate IdP, OAuth explicitly rejected in `decisions/magic-link-auth.md`) and "How much operational complexity can we absorb?" (near zero — `constraints/solo-maintainer.md`).

# QUESTIONS

1. What user evidence is behind this request — did specific freelancers ask to work on tasks *simultaneously* with clients, or is the underlying need just "my client can't see/update task status without emailing me"? The answer decides between Level 0/1 (sharing + comments) and anything realtime.
2. Are clients meant to become first-class TaskLite users with their own accounts, or should they only access individual tasks/boards a freelancer explicitly shares? (This is a new user class not covered by `constraints/external-users.md` and needs its own decision.)
3. If some live experience is truly required: is "sees updates within a few seconds and never silently overwrites" acceptable (polling/SSE + version checks), or is character-by-character co-editing with live cursors the actual bar? Note the second option conflicts with the solo-maintainer constraint recorded on 2026-07-08 ("anything that can break at 3am is out") unless we buy it as a managed service — is there budget and appetite for a paid realtime vendor dependency?
