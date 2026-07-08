# Real-time collaborative editing — evaluation

## 1. RECOMMENDATION

**Do not build true real-time collaborative editing (live cursors, simultaneous character-level co-editing, CRDT/OT sync) now.** It directly conflicts with the project's accepted operating constraint: TaskLite is built and run by one person a few hours per week, and every design choice must minimize operational surface. Real-time collab is one of the highest operational-surface features that exists — persistent WebSocket infrastructure, conflict-resolution logic (CRDT or OT), presence tracking, reconnection handling, and a whole new class of "breaks at 3am" failure modes. The owner explicitly ruled that class of thing out ("Anything that can break at 3am is out").

Instead, I recommend a phased approach that captures most of the user value at a fraction of the operational cost:

**Phase 1 — Client access via shared task links (low risk, reuses existing decisions).**
Let a freelancer share a task (or project) with a client. Clients authenticate the same way freelancers do — single-use magic links emailed to them — which extends the accepted magic-link auth decision naturally, since clients are also external individuals with no corporate IdP. Scope client permissions narrowly at first (view + comment, or view + edit specific fields). This introduces the *collaboration* concept without any real-time machinery.

**Phase 2 — Asynchronous co-editing with conflict safety.**
Task-level edits from either party, protected by optimistic concurrency (version stamp per task; on conflict, show "this task changed since you loaded it" and let the user reconcile). Add lightweight change history / activity feed per task so each side can see what the other did. This is plain request/response CRUD — nothing stateful to operate.

**Phase 3 — "Live-feeling" updates without WebSockets.**
Short-interval polling or SSE to refresh a task view while it's open, plus a soft "X is viewing/editing this task" indicator. This delivers ~90% of the perceived "working live together" experience with essentially zero new operational surface.

**Only if validated demand emerges** for genuine simultaneous text co-editing (e.g., on task descriptions), consider a fully managed real-time service (e.g., a hosted sync/CRDT SaaS) rather than self-hosting anything — and treat that as a new Decision with its own evidence, because it partially trades against the solo-maintainer constraint (vendor dependency and cost instead of ops burden).

I would not start any implementation until the questions in section 3 are answered, because the request as phrased assumes clients become users — a concept that does not exist anywhere in the current knowledge base or specs.

## 2. PRIOR CONTEXT

Found via `E:\PROJEKTI\okf\example\knowledge\index.md` (per the read-first behavior in `E:\PROJEKTI\okf\behaviors\read-first.md`):

- **`E:\PROJEKTI\okf\example\knowledge\constraints\solo-maintainer.md`** — one person builds and operates TaskLite a few hours per week; every design choice must minimize operational surface. This is the load-bearing constraint that rules out self-hosted real-time infrastructure.
- **`E:\PROJEKTI\okf\example\knowledge\constraints\external-users.md`** — users are individual freelancers with no corporate identity provider. Clients invited by freelancers will be the same kind of external individual, so the existing auth approach extends to them.
- **`E:\PROJEKTI\okf\example\knowledge\decisions\magic-link-auth.md`** — accepted 2026-07-08 (today; evidence fresh and plausible): auth is emailed single-use magic links; passwords and OAuth explicitly rejected. I respect this decision and built Phase 1 on top of it rather than re-litigating — client access should use magic links too, not a new auth mechanism.
- **`E:\PROJEKTI\okf\example\knowledge\interviews\2026-07-08-auth-scope.md`** — Ivan's answers: no SSO needed; "basically none" maintenance capacity; "anything that can break at 3am is out"; no formal compliance requirements, just no password storage. This interview already answers "how much operational complexity can this feature carry?" — near zero — so I did not re-ask it.
- **`E:\PROJEKTI\okf\example\specs\auth\spec.md`** — AUTH-1 (magic-link login, no passwords) and AUTH-2 (30-day inactivity session expiry). Client sessions would inherit these requirements unless deliberately changed.
- **`E:\PROJEKTI\okf\example\knowledge\log.md`** — confirms the auth decision chain is the entire current history; there is no prior decision about collaboration, sharing, multi-user access, or real-time features. This is greenfield territory, so a new Decision (with a Rejected section) must be captured once scoping questions are answered.

## 3. QUESTIONS

The wiki answers the maintenance-budget and auth-mechanism questions, so I am not asking those. What it does not answer:

1. **What is the underlying problem?** When you say freelancers should "work on tasks live together with their clients" — is the actual pain (a) clients can't see or update tasks at all today, (b) feedback loops are slow/async and people want faster visibility, or (c) people genuinely need to type in the same text field at the same moment, Google-Docs style? The answer determines whether Phase 1, Phase 3, or the managed-CRDT endgame is the real target.
2. **Do clients become first-class accounts?** Should a client have a persistent TaskLite identity (email + magic link, sessions, their own task list across freelancers), or is per-share, per-task guest access enough? This shapes the data model far more than the real-time question does.
3. **What may clients do to a task?** View only? Comment? Edit status/due dates? Edit descriptions? Create tasks? The minimal viable permission set determines Phase 1 scope.
4. **Is there demand evidence?** Has any user asked for this, or is it a hypothesis? Given the solo-maintainer constraint, I'd want at least a few concrete user requests before investing beyond Phase 1.
5. **If real-time ever becomes necessary: is a paid managed service acceptable?** The magic-link decision rejected third-party OAuth partly for vendor/console overhead. A hosted real-time sync service is a similar trade (vendor dependency + recurring cost in exchange for near-zero ops). Is that trade acceptable in principle, or is "no critical third-party runtime dependencies" the standing rule? (This is the one delta-style question, since the existing decision's reasoning gestures at it without settling it.)
