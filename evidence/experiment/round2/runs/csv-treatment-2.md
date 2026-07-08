# CSV Export — Evaluation and Proposal (TaskLite)

## 1. RECOMMENDATION

Proceed — CSV export is a good fit for TaskLite, but keep it deliberately minimal, shaped by the two accepted constraints in the knowledge base.

Proposed approach:

- **Synchronous, on-demand download.** A single authenticated endpoint (e.g. `GET /tasks/export.csv`) that streams the requesting user's own tasks as a CSV response with `Content-Disposition: attachment`. No background jobs, no export queue, no emailed files, no stored artifacts. Rationale: the [solo-maintainer constraint](../../example/knowledge/constraints/solo-maintainer.md) requires minimizing operational surface — anything that can break at 3am is out, and async export pipelines are exactly that kind of surface. A freelancer's task list is small enough that streaming it synchronously is safe.
- **Per-user scope only.** Export returns only the authenticated user's tasks, gated behind the existing magic-link session (AUTH-1/AUTH-2 in `example/specs/auth/spec.md`). Users are individual external freelancers ([external-users constraint](../../example/knowledge/constraints/external-users.md)), so there is no team/org/admin export concept to design for.
- **Boring, standards-compliant CSV.** RFC 4180 quoting/escaping, UTF-8 with BOM (so Excel opens it correctly since "spreadsheet" is the stated user goal), comma delimiter, ISO 8601 dates, header row. Use the standard library's CSV writer — no new dependency.
- **No format ambitions beyond CSV.** No XLSX, no scheduled exports, no import — YAGNI until a user asks. Revisit only on demand.
- **Process note:** once the open questions below are answered, the outcome should be captured as `knowledge/decisions/csv-export.md` (with a `## Rejected` section covering async/emailed export and XLSX), the answers recorded as an interview file, a line appended to `knowledge/log.md`, and a `specs/export/spec.md` requirement added with a `why` link — per the project's read-first/capture-on-decision convention. (Not done now: this run is read-only by instruction, and the decision has not yet crystallized because the questions below are unanswered.)

Estimated effort: small — one endpoint, one serializer, one UI button, a handful of escaping/encoding tests.

## 2. PRIOR CONTEXT

Context found and used (all paths absolute):

- `E:\PROJEKTI\okf\behaviors\read-first.md` — the governing behavior: read the knowledge bundle first, never ask what it already answers, cite accepted decisions, capture new decisions when they crystallize.
- `E:\PROJEKTI\okf\example\knowledge\index.md` — entry point; TaskLite is a lightweight task tracker for freelancers, solo-maintained. Lists all decisions/constraints/interviews. **No existing decision, constraint, or interview touches export, CSV, reporting, or the task data model** — this is a genuinely new decision area, so nothing is being re-litigated.
- `E:\PROJEKTI\okf\example\knowledge\constraints\solo-maintainer.md` — one person, a few hours/week; every design choice must minimize operational surface. Directly drives the "synchronous, no background jobs" recommendation.
- `E:\PROJEKTI\okf\example\knowledge\constraints\external-users.md` — users are individual freelancers, no corporate IdP/org structure. Drives the "per-user export only, no team/admin export" scoping.
- `E:\PROJEKTI\okf\example\knowledge\interviews\2026-07-08-auth-scope.md` — Ivan's answers: near-zero maintenance tolerance, no formal compliance requirements, no password liability. Confirms low-maintenance bias and that there is no compliance regime constraining data export.
- `E:\PROJEKTI\okf\example\knowledge\decisions\magic-link-auth.md` — accepted 2026-07-08, evidence current (same day). Respected and cited, not re-litigated: the export endpoint sits behind the existing magic-link session.
- `E:\PROJEKTI\okf\example\specs\auth\spec.md` — AUTH-1 (magic-link login) and AUTH-2 (30-day session expiry); the only spec in the project. Notably, **there is no task spec** — the task data model (fields/columns) is not documented anywhere, which is why Question 1 below must go to the human.
- `E:\PROJEKTI\okf\example\knowledge\log.md` — confirms the bundle's full history is the 2026-07-08 auth work; nothing export-related has ever been decided.

Per the read-first rule, I am NOT asking about: maintenance budget, user population, SSO/org concerns, or compliance — the wiki already answers all of these.

## 3. QUESTIONS

1. There is no task data model documented in `knowledge/` or `specs/` — what fields does a task have, and which of them should appear as CSV columns (e.g. title, status, due date, created date, notes, client/project tags)?
2. Should the export cover all of the user's tasks, or respect the currently applied filter/view in the UI (e.g. "export what I'm looking at")?
3. Is plain CSV sufficient for the "spreadsheet" goal, or do users specifically expect an Excel (.xlsx) file? I recommend CSV-only (UTF-8 with BOM opens cleanly in Excel) to avoid a new dependency, but want to confirm before locking the decision.
