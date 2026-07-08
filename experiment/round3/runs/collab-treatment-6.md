# RECOMMENDATION

Do not build real-time collaborative editing (live multi-cursor editing, presence, OT/CRDT sync) as requested. It conflicts directly with the project's accepted operating constraint: TaskLite is built and run by one person a few hours per week, and every design choice must minimize operational surface (`knowledge/constraints/solo-maintainer.md`, sourced from Ivan's own words: "Anything that can break at 3am is out"). Real-time collaboration is one of the highest-operational-surface features that exists — it requires persistent WebSocket infrastructure, a conflict-resolution engine (CRDT or OT), presence/awareness state, reconnection and offline handling, and a new class of hard-to-reproduce sync bugs. That is precisely the "can break at 3am" category the project has already ruled out.

The underlying need — "freelancers work on tasks together with their clients" — is legitimate and worth serving, but it can almost certainly be met with a drastically cheaper shape. I recommend proposing this ladder to the PM, in order of increasing cost:

1. **Shared read-only task views** (signed link a freelancer sends a client; no client account needed). Near-zero new surface; reuses nothing stateful.
2. **Client accounts + comments/status updates on tasks**, using the existing magic-link auth (`knowledge/decisions/magic-link-auth.md` — it extends naturally to clients, who as external individuals also have no corporate IdP). Asynchronous collaboration, plain request/response, no realtime stack.
3. **Cheap freshness, not realtime**: short-interval polling or a "this task was updated — refresh" banner, plus optimistic-concurrency conflict detection (reject stale writes via an `updated_at` check). This gives 90% of the perceived "live" experience with none of the sync machinery.

Only if evidence later shows simultaneous same-field editing is a real, frequent need (and the solo-maintainer constraint has changed — e.g., a team or a managed service budget exists) should true realtime editing be reconsidered. If we proceed with the lighter shape, the outcome should be captured as a new `knowledge/decisions/` entry with the full realtime version documented under `## Rejected`, linked to the solo-maintainer constraint, plus a new interview file for the PM's answers to the questions below.

Note: the magic-link auth decision (`status: accepted`, 2026-07-08 — today) is fresh and is respected, not re-litigated; option 2 builds on it rather than around it.

# PRIOR CONTEXT

Found and used, per `E:\PROJEKTI\okf\behaviors\read-first.md`:

- `E:\PROJEKTI\okf\example\knowledge\index.md` — entry point; TaskLite is a lightweight task tracker for freelancers, solo-maintained.
- `E:\PROJEKTI\okf\example\knowledge\constraints\solo-maintainer.md` — one maintainer, a few hours/week; every design choice must minimize operational surface. This is the controlling constraint for this request.
- `E:\PROJEKTI\okf\example\knowledge\constraints\external-users.md` — users are individual external freelancers; no corporate identity provider. Relevant because "clients" would be a *new* user class this constraint does not yet cover.
- `E:\PROJEKTI\okf\example\knowledge\decisions\magic-link-auth.md` — accepted 2026-07-08; magic links, no passwords, no OAuth; rejected alternatives recorded. Fresh evidence → respected and reused for client access, not reopened.
- `E:\PROJEKTI\okf\example\knowledge\interviews\2026-07-08-auth-scope.md` — Ivan: "Basically none [maintenance]... Anything that can break at 3am is out"; "don't store passwords." Answers the maintenance-budget question, so I do not ask it again.
- `E:\PROJEKTI\okf\example\knowledge\log.md` — change history; confirms the bundle is current (all entries dated today).
- `E:\PROJEKTI\okf\example\specs\auth\spec.md` — AUTH-1 (magic-link login) and AUTH-2 (30-day sessions); client accounts and shared views would extend this spec, and AUTH-2's session policy may need a variant for client-facing share links.

Questions the wiki already answers (therefore NOT asked): how much operational/maintenance burden is acceptable (none — solo-maintainer constraint); whether SSO/OAuth is needed for new users (no — external-users constraint + magic-link decision); whether passwords are acceptable for client accounts (no — interview).

# QUESTIONS

1. What is the actual observed problem behind "work on tasks live together"? Is it (a) clients can't see task status at all today, (b) feedback happens over email and gets lost, or (c) two people genuinely need to edit the same task description at the same moment? The right rung on the ladder above depends entirely on this.
2. Clients are a new user class — the current constraint says users are individual freelancers. Should clients get full accounts (they'd log in via the existing magic-link flow), or is per-task/per-project link-based access enough? Do clients ever need to *edit* tasks, or only comment and change status?
3. The solo-maintainer constraint was recorded today (2026-07-08) because you work on this alone a few hours per week — I'm treating it as current and binding. Confirming: is that still true, i.e., there is no plan to add maintainers or an ops budget that would change what "acceptable operational surface" means for this feature?
4. Is there any expectation of simultaneous editing of the same field by freelancer and client at the same time, or is "within a few seconds of each other, with a refresh" acceptable? (If the latter, polling + stale-write rejection covers it and no realtime stack is needed.)
