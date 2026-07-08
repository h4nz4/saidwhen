Read-first done — I've grounded this in TaskLite's knowledge base (`knowledge/`) and specs. Here's the evaluation.

---

## 1. RECOMMENDATION

Ship the **laziest version that satisfies the constraints**: a single authenticated, on-demand endpoint that streams the **current user's own tasks** as CSV, built on Python's stdlib `csv` module. No new dependency, no background job, no export-history table, no scheduling.

Why this shape and not more:
- **Solo-maintainer constraint** dictates minimum operational surface. A synchronous "click → download" endpoint has nothing that can page you at 3am. Background workers, an export queue, or emailed exports all add moving parts this project has explicitly ruled out for auth and should rule out here too.
- **External-freelancer + magic-link model** means the natural scope is *per-user, their own data only* — reusing the existing session (AUTH-1/AUTH-2) as the authorization boundary. CSV export doubles as data-portability for individual users, which fits the audience.
- **stdlib covers it.** `csv.writer` over an HTTP streaming response is a few lines. No pandas, no CSV library.

What I'd deliberately skip, and when to add it:
- **Async/background export** — skip; add only if a real user hits a task count large enough to time out a request (unlikely for a solo freelancer's task list).
- **Emailed/scheduled exports** — skip; the mailer exists (magic links) so it's tempting, but it's new surface with no stated need.
- **Column config / field selection** — skip; ship a fixed sensible column set, revisit if asked.

One caution that isn't laziness: **the CSV must be scoped and field-filtered at a trust boundary** — only the authenticated user's rows, and no session tokens, magic-link tokens, or other users' data in any column. That's non-negotiable given the "don't want the liability" posture in the auth interview.

## 2. PRIOR CONTEXT (what informed this, with paths)

- `knowledge/constraints/solo-maintainer.md` — "Every design choice must minimize operational surface… Anything that can break at 3am is out." → rules out background jobs, queues, scheduled exports.
- `knowledge/constraints/external-users.md` — individual freelancers, no corporate IdP. → export is inherently per-user; also frames it as personal data portability.
- `knowledge/decisions/magic-link-auth.md` + `specs/auth/spec.md` (AUTH-1, AUTH-2) — the only auth boundary is the emailed magic-link session. → the export endpoint authorizes off that same session; scope = "tasks owned by the session's user."
- `knowledge/interviews/2026-07-08-auth-scope.md` — owner: "just don't store passwords, I don't want the liability." → sensitive-field exclusion in the CSV is a hard requirement, not a nicety.
- `README.md` / `knowledge/index.md` — the **Provenance Convention**: every spec requirement links to a decision, every decision to a human answer. → this feature currently has *no* decision or interview backing it, which drives my questions below.

## 3. QUESTIONS (for the PM / owner)

1. **Scope confirmation.** Export = only the authenticated user's own tasks, correct? Is there any admin/all-users export need? (Everything in the knowledge base points to per-user; I want to confirm before it becomes a spec.)
2. **Columns.** Which fields belong in the CSV, and — given the liability stance — which must be *excluded*? I'll default to a fixed set (e.g. title, status, due date, created/updated) and no internal IDs/tokens unless you say otherwise.
3. **Volume.** Rough ceiling on tasks per user? This is the one thing that decides whether synchronous streaming is safe (it is for anything short of very large). Under ~tens of thousands, sync is fine.
4. **Trigger.** On-demand download button only, or do you also want scheduled/emailed exports? (I recommend download-only; emailed export reuses the mailer but adds the kind of surface the solo-maintainer constraint pushes back on.)
5. **Provenance.** This feature has no decision or interview yet. Per the convention, want me to run a short scoping interview (like the auth one) so the resulting `EXPORT-*` requirement can link back to a human answer — before I write any spec?

*Note: I could not open `../behaviors/read-first.md` — it sits outside this session's permitted working directory (`example/`) and the read was denied. I followed the read-first intent via the README's explicit instruction (browse `knowledge/` + `specs/`). No files were modified.*