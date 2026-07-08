# CSV export for TaskLite — evaluation and proposal

## 1. RECOMMENDATION

Proceed — CSV export is a good fit for TaskLite, but keep it deliberately small. Concretely:

- **Implement it as a single authenticated, synchronous endpoint** (e.g. `GET /export/tasks.csv`) that streams the current user's tasks as a CSV download. No background jobs, no export queue, no email-the-file flow, no scheduled exports, no S3/object storage. Anything that can fail asynchronously or "break at 3am" is out of scope for this project: TaskLite is solo-maintained a few hours per week and every design choice must minimize operational surface (`knowledge/constraints/solo-maintainer.md`).
- **Reuse the existing magic-link session for authorization** — the export must be gated by the same session auth defined in `specs/auth/spec.md` (AUTH-1/AUTH-2), and must only ever return the requesting user's own tasks. No new auth mechanism, no API keys for now.
- **Generate the CSV with the standard library / a minimal battle-tested CSV writer**, not a reporting framework. Include a header row, RFC 4180 quoting, UTF-8 with BOM so Excel opens it correctly (freelancers overwhelmingly mean "Excel/Google Sheets" when they say spreadsheet), and ISO 8601 dates.
- **Guard against CSV/formula injection**: task titles and notes are user-entered free text, so any cell starting with `=`, `+`, `-`, or `@` should be prefixed (e.g. with `'`) before writing. This is the one real security consideration in an otherwise trivial feature — there are no formal compliance requirements beyond that (per the 2026-07-08 interview).
- **Scope v1 to "all my tasks, one file, fixed column set"** (suggested columns: id, title, status, project/client, created date, due date, completed date, notes/tags as applicable to the actual task model). Filtered/partial exports, column pickers, XLSX format, and recurring exports are all "revisit if users ask" — same posture the project took when rejecting OAuth.
- **Process note:** the project keeps decision provenance in `knowledge/`. Once the open questions below are answered, this crystallizes into `knowledge/decisions/csv-export.md` (with a `## Rejected` section covering async export pipelines and XLSX), a new interview file for the answers, a log line, and a new spec section (e.g. `specs/export/spec.md`) whose requirements link back to the decision — mirroring how `specs/auth/spec.md` links to `magic-link-auth.md`. Note that `example/` currently contains only specs and the knowledge wiki, no application code, so "implementation" here primarily means specifying the feature; if there is a codebase elsewhere, the endpoint above is the shape it should take.

## 2. PRIOR CONTEXT

Context found in the OKF bundle at `E:\PROJEKTI\okf\example\knowledge\` (entry point `index.md`) and used above:

- `E:\PROJEKTI\okf\example\knowledge\index.md` — TaskLite is a lightweight task tracker for freelancers, solo-maintained; index of all decisions, constraints, and interviews. No existing decision touches export/reporting, so nothing is being re-litigated.
- `E:\PROJEKTI\okf\example\knowledge\constraints\solo-maintainer.md` — one person builds and operates TaskLite a few hours per week; every design choice must minimize operational surface. This is why I recommend a synchronous endpoint and reject async export infrastructure.
- `E:\PROJEKTI\okf\example\knowledge\constraints\external-users.md` — users are individual freelancers with no corporate IdP. This shapes the audience assumption (Excel/Google Sheets consumers; no enterprise export/BI integration needed).
- `E:\PROJEKTI\okf\example\knowledge\interviews\2026-07-08-auth-scope.md` — Ivan's answers: no SSO needed, near-zero maintenance budget ("Anything that can break at 3am is out"), no formal compliance requirements ("Just don't store passwords"). This already answers the questions "are there compliance constraints on exported data?" and "how much operational complexity can this feature carry?", so I am not asking them.
- `E:\PROJEKTI\okf\example\knowledge\decisions\magic-link-auth.md` (status: accepted, 2026-07-08, evidence current) — magic-link auth, no passwords, no OAuth. Respected, not re-litigated: the export endpoint rides on the existing session.
- `E:\PROJEKTI\okf\example\specs\auth\spec.md` — AUTH-1 (magic-link login) and AUTH-2 (30-day session expiry); the export endpoint must sit behind this, and the spec format here (requirement + `why` link to decision) is the template for the new export spec.
- `E:\PROJEKTI\okf\example\knowledge\log.md` and `E:\PROJEKTI\okf\example\README.md` — change history and project framing; confirm no prior export-related work exists anywhere in the bundle.

## 3. QUESTIONS

Only the questions the wiki does not already answer:

1. **Scope of the export:** should v1 export all of the user's tasks in one file, or do you want filters from day one (e.g. by status, project/client, or date range)? My proposal assumes "all tasks" with filters deferred.
2. **Columns:** which task fields must appear in the CSV? I proposed id, title, status, project/client, created/due/completed dates, and notes/tags — please confirm against the actual task model, and flag anything that should be excluded.
3. **Format:** is CSV alone sufficient, or do users concretely need `.xlsx`? (CSV opens fine in Excel/Google Sheets; XLSX adds a dependency and maintenance surface, so I'd reject it unless there's known demand.)
4. **Placement:** where should the export live in the UI — a "Download CSV" button on the task list, a settings/account page, or both? (Affects only the spec wording, not the architecture.)
