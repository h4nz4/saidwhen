Read-first done — the knowledge base is small and fully absorbed. Here's the proposal.

## 1. RECOMMENDATION

Build the smallest thing that works: a single authenticated endpoint that streams the current user's own tasks as CSV, generated with the language's **standard-library CSV writer** (Python `csv`, Node `csv-stringify` only if already present — otherwise hand-write, it's ~10 lines). No new dependency, no background job, no file storage, no async "export job" queue.

Shape:
- `GET /tasks/export.csv` — session-authenticated (reuses existing magic-link session; no new auth surface).
- Streams rows for the logged-in user **only** — scoped by the same user filter every other task query already uses.
- `Content-Type: text/csv`, `Content-Disposition: attachment; filename="tasks.csv"`.
- Columns = the task fields that already exist. Don't invent a reporting schema.

Skipped: async export jobs, S3/file storage, scheduled/emailed exports, XLSX, column pickers, date-range filters. Add when a user actually asks and the task count makes a synchronous response too slow (thousands+). For a solo-maintained freelancer tool, that day is far off — a freelancer's own task list is small enough to serialize in one request.

Why this fits the project, not just "why it's less code": the binding constraint here is **[solo-maintainer](example/knowledge/constraints/solo-maintainer.md)** — "anything that can break at 3am is out." An export-job queue, a storage bucket, or a new dependency each add exactly the kind of 3am surface that got OAuth and passwords rejected. A synchronous stdlib endpoint has near-zero operational surface, which is the same test that shaped every existing decision.

## 2. PRIOR CONTEXT (what informed this)

- **`example/knowledge/constraints/solo-maintainer.md`** — one maintainer, a few hours/week; every choice must minimize operational surface. This is why I reject the async-job / storage / new-dependency version by default.
- **`example/knowledge/constraints/external-users.md`** + **`example/knowledge/decisions/magic-link-auth.md`** — users are external freelancers, each authenticated individually via magic-link sessions. Directly implies export must be **per-user scoped** (a freelancer exports *their* tasks) and must reuse the existing session, not a new auth path.
- **`example/specs/auth/spec.md`** (AUTH-1, AUTH-2) — export inherits the existing session model (30-day expiry, single-use link). The endpoint is just another authenticated route; no auth spec change needed.
- **`example/knowledge/interviews/2026-07-08-auth-scope.md`** — "nothing formal" on compliance, but "don't store passwords, I don't want the liability." The liability-aversion pattern argues against **storing generated export files** anywhere; stream and forget.
- Provenance note: there is currently **no `tasks` spec or decision** in `knowledge/` — the base only covers auth. So the actual task/field schema this CSV serializes is undocumented; see Questions.

## 3. QUESTIONS (for the PM / owner)

1. **Scope of data** — export only the requesting freelancer's own tasks, correct? (Everything in the knowledge base says single-user; confirming there's no shared/team view I'm missing.)
2. **What is a "task"?** — there's no task spec in `knowledge/` yet. Which fields exist and which should the CSV include (e.g. title, status, due date, created-at, notes)? This decision should get written down as the first `specs/tasks/` entry regardless of export.
3. **Trigger** — is a "Download CSV" button in the existing UI enough, or do you want it emailed/scheduled? (Default assumption: button. Scheduled/emailed adds a mail path and a scheduler — real 3am surface — so I'd want an explicit ask.)
4. **Volume** — roughly how many tasks does a heavy user accumulate? If it's realistically bounded (hundreds), synchronous streaming is safe forever; if some users could hit tens of thousands, we'd revisit.
5. **Provenance** — should I capture this as a proper `decisions/csv-export.md` + a short interview once you answer the above, to keep the convention intact? (I did **not** modify any files this pass, per instruction.)

*Note: the `../behaviors/read-first.md` file you pointed me to sits outside this session's allowed working directories, so I couldn't open it directly — I followed its evident intent (read the full `knowledge/` base before proposing). If you want me to read the actual file, grant access to `E:\PROJEKTI\saidwhen\behaviors\` or run from the repo root.*