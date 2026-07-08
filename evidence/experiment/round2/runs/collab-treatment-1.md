# TaskLite — Real-time collaborative editing: evaluation

## 1. RECOMMENDATION

Do not build real-time collaborative editing (CRDT/OT sync engines, WebSocket presence, live cursors) in its full form. It is the single highest-operational-surface feature class a web app can take on, and it directly collides with TaskLite's accepted, current constraints:

- **Solo maintainer** (`knowledge/constraints/solo-maintainer.md`): one person, a few hours per week, and per the owner interview, "anything that can break at 3am is out." A real-time sync service is exactly the thing that breaks at 3am — stateful WebSocket servers, reconnection storms, conflict-resolution bugs, and scaling concerns that cannot be absorbed by this project.
- **Users are external freelancers** (`knowledge/constraints/external-users.md`): today, clients are not users of TaskLite at all. "Work live together with their clients" quietly introduces an entirely new user class before any editing technology is even discussed.

The underlying job — "freelancers and clients look at the same task and stay in sync" — can be delivered incrementally, cheapest-first:

**Phase 1 — Client visibility (recommended starting point).** Tokenized read-only share links for a task or project, plus client comments. This reuses the exact mechanics of the accepted magic-link decision (`knowledge/decisions/magic-link-auth.md`): single-use/scoped emailed links, no passwords, no OAuth, near-zero new auth surface. Stateless, cacheable, nothing to break at 3am.

**Phase 2 — Near-real-time freshness, no sync engine.** Short-interval polling or SSE (server-sent events, one-directional, no WebSocket state) so an open task view refreshes within seconds. Combine with per-field last-write-wins and an "edited by X just now — reload" notice for the rare simultaneous edit. For a task tracker (short structured fields, not long-form documents), true concurrent character-level merging is almost never the actual requirement.

**Phase 3 — only if validated demand survives Phases 1–2.** If genuine live co-editing demand persists, use a fully managed sync service (e.g., a hosted CRDT/sync provider) rather than self-hosting one — the solo-maintainer constraint makes self-hosted real-time infrastructure a non-starter regardless of demand.

Proposed process: answer the questions in section 3, then (per the project convention) record the outcome as `knowledge/decisions/<slug>.md` with a `## Rejected` section — including explicitly rejecting self-hosted real-time sync — and, if clients become users, a new/updated constraint superseding or amending `external-users.md`. Ship Phase 1 behind that decision.

## 2. PRIOR CONTEXT

Found and used, all under `E:\PROJEKTI\okf\example\`:

- `knowledge/index.md` — entry point; TaskLite is a lightweight task tracker for freelancers, solo-maintained.
- `knowledge/constraints/solo-maintainer.md` — one person builds and operates TaskLite a few hours per week; every design choice must minimize operational surface. Timestamp 2026-07-08 (today) — evidence is current, so this constraint is respected, not re-litigated.
- `knowledge/constraints/external-users.md` — users are individual freelancers; no corporate identity provider. Current as of today. Relevant because the request implies clients becoming users, which this constraint does not cover.
- `knowledge/decisions/magic-link-auth.md` — accepted 2026-07-08: magic-link auth only; OAuth and passwords explicitly rejected. Fresh and plausible → respected. Consequence: any client access must also be magic-link/token-based; I did not re-open the auth question.
- `knowledge/interviews/2026-07-08-auth-scope.md` — owner's answers: no SSO, "basically none" maintenance budget, "anything that can break at 3am is out," no formal compliance, no passwords. This interview pre-answers all maintenance-budget and auth-mechanism questions, so none are asked below.
- `specs/auth/spec.md` — AUTH-1 (magic-link login), AUTH-2 (30-day session expiry); Phase 1 share links must slot alongside these requirements.
- `knowledge/log.md` — confirms the bundle's history; nothing about collaboration or clients exists yet, so this is a genuinely new decision area.

## 3. QUESTIONS

Only questions the wiki does not already answer (auth mechanism and maintenance budget are settled by the interview and decision above):

1. This request makes clients first-class users for the first time — the current constraint (`external-users.md`, 2026-07-08) says users are individual freelancers only. Is expanding the user base to include freelancers' clients an intentional product decision, and should clients get accounts (magic-link, consistent with the accepted auth decision) or only tokenized guest access to specific tasks/projects?
2. What is the actual observed need behind "real-time"? Concretely: do freelancers/clients need to type in the same field at the same moment (true co-editing), or do they need to see each other's updates and comments quickly (visibility within seconds)? Is there user evidence (requests, churn reasons) for the former?
3. If live co-editing turns out to be genuinely required, is a paid, fully managed third-party sync service acceptable (recurring cost + external dependency), given that self-hosting real-time infrastructure is ruled out by the solo-maintainer constraint?
4. Scope of "editing together": which objects — task title/description, checklists, comments, attachments? (This determines whether last-write-wins per field is sufficient, which it usually is for structured task data.)
