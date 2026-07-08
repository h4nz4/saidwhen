# CSV Export — evaluation and proposal (TaskLite)

## 1. RECOMMENDATION

Proceed with CSV export — it fits TaskLite's profile well — but scope it to the smallest possible operational surface, and record it through the project's provenance workflow before writing code.

Proposed approach:

- **Synchronous, on-demand download.** A single authenticated endpoint (e.g. `GET /tasks/export.csv`) that streams the current user's tasks as `text/csv` with a `Content-Disposition: attachment` header. No background jobs, no export queue, no emailed files, no stored artifacts. TaskLite is solo-maintained a few hours per week, so anything with async moving parts or scheduled cleanup is out of budget (see constraints below).
- **No new dependencies.** CSV generation is simple enough for the standard library of whatever stack TaskLite uses; a spreadsheet-library dependency (e.g. for .xlsx) adds maintenance surface the project explicitly cannot absorb. CSV opens fine in Excel, Google Sheets, and Numbers, which covers freelancer users who have no corporate tooling.
- **Scope: the requesting user's own tasks only**, reusing the existing magic-link session for authorization. No admin/all-users export, no public share links.
- **Safety details baked in from the start:** UTF-8 with BOM (so Excel renders non-ASCII correctly), RFC 4180 quoting, and CSV-injection hardening (prefix cells starting with `=`, `+`, `-`, `@` — task titles are user-supplied free text landing in spreadsheets).
- **Process:** this project keeps decision provenance in `knowledge/`. Once the open questions below are answered, the work should produce: `knowledge/decisions/csv-export.md` (type: Decision, with a `## Rejected` section covering async export, xlsx, and third-party export services), `knowledge/interviews/<date>-csv-export-scope.md` capturing the answers, a new `specs/export/spec.md` with requirements linking to the decision (matching the `specs/auth/spec.md` pattern), a line in `knowledge/log.md`, and an index entry. Note there is currently no application code in the repo — only specs and the knowledge bundle — so the concrete deliverable of this feature at this stage is the spec + decision, not an implementation diff.

Rough size: one endpoint, one serializer function, a link/button in the UI. Small, low-risk, aligned with existing constraints. Nothing in the existing decisions conflicts with it (the only accepted decision is about auth, which this feature simply reuses).

## 2. PRIOR CONTEXT

Context found in the OKF bundle at `E:\PROJEKTI\okf\example\knowledge\` (entry point `index.md`), plus specs:

- `E:\PROJEKTI\okf\example\knowledge\index.md` — knowledge-base entry point; TaskLite is a lightweight task tracker for freelancers, solo-maintained.
- `E:\PROJEKTI\okf\example\knowledge\constraints\solo-maintainer.md` — one person builds and operates TaskLite a few hours per week; every design choice must minimize operational surface. This is the constraint that drives the "synchronous download, no async pipeline, no new dependencies" shape of the recommendation.
- `E:\PROJEKTI\okf\example\knowledge\constraints\external-users.md` — users are individual freelancers with no corporate identity provider. This rules out "export to Google Workspace / SharePoint integration"-style features and answers who the spreadsheet consumers are (individuals using consumer spreadsheet tools).
- `E:\PROJEKTI\okf\example\knowledge\decisions\magic-link-auth.md` — status: accepted, 2026-07-08, evidence still current (same-day). Respected, not re-litigated: the export endpoint authenticates via the existing magic-link session; no per-feature auth questions need asking.
- `E:\PROJEKTI\okf\example\knowledge\interviews\2026-07-08-auth-scope.md` — Ivan: "Basically none [maintenance]. I'm the only maintainer... Anything that can break at 3am is out." and "Nothing formal [compliance]." These pre-answer two questions I would otherwise ask (maintenance budget for an export pipeline; compliance/data-handling requirements for exported data), so I am not asking them.
- `E:\PROJEKTI\okf\example\specs\auth\spec.md` — the requirement-with-provenance-link format (`([why](...))`) the new `specs/export/spec.md` should follow.
- `E:\PROJEKTI\okf\example\knowledge\log.md` — change-history format for the log entry this decision will append.

No existing decision, interview, or constraint mentions export, CSV, reporting, or data formats — this is a genuinely new decision area, so a decision record must be created rather than an old one cited.

## 3. QUESTIONS

Only the deltas the wiki does not answer:

1. **Columns and scope:** Which task fields should the CSV include (e.g. title, status, due date, created date, notes/description, project/client tag)? And should the export be "all my tasks" only, or respect the currently applied filter/view (e.g. export just completed tasks or one client's tasks)?
2. **Is plain CSV sufficient, or do users expect a native Excel (.xlsx) file?** I recommend CSV-only (zero dependencies, opens in every spreadsheet app); confirming so the Decision's Rejected section can record xlsx as considered-and-rejected with your answer as evidence.
3. **Locale/delimiter expectations:** Are a meaningful share of your freelancer users in locales where Excel expects semicolon-delimited CSV (much of Europe)? If yes, I'd add a `sep=,` hint line or a delimiter option; if unknown/no, I'll ship plain comma-delimited UTF-8-BOM and revisit on complaint.

(Not asking about maintenance budget, compliance, or auth for the endpoint — the interview of 2026-07-08 and the accepted magic-link decision already answer those.)
