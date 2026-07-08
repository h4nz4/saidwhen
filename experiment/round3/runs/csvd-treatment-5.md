# CSV export for TaskLite — evaluation and proposal

## 1. RECOMMENDATION

Proceed — CSV export is a good fit for TaskLite, and the existing constraints point clearly at the simplest possible shape:

- **Synchronous, on-demand generation.** A single authenticated endpoint (e.g. `GET /export/tasks.csv`) that streams the current user's tasks as a CSV download. No background jobs, no export queue, no emailed files, no stored artifacts to clean up. TaskLite is solo-maintained with a near-zero operational budget, so anything with async moving parts or a third-party export service is out of scope.
- **No new dependencies if avoidable.** CSV generation is simple enough to do with the standard library of whatever stack TaskLite runs on; avoid pulling in a spreadsheet library (XLSX etc.) unless the human explicitly wants Excel-native format.
- **Scope to the requesting user's own tasks only.** Users are individual external freelancers; there is no team/org dimension, so no admin/bulk-export surface is needed.
- **Practical format defaults** (pending confirmation): UTF-8 with BOM so Excel detects encoding correctly, comma delimiter, RFC 4180 quoting, ISO 8601 dates, header row. Escape any cell beginning with `=`, `+`, `-`, or `@` (CSV/formula-injection hardening) since task titles are user-supplied text.
- **Auth is already settled** — the export endpoint sits behind the existing magic-link session (AUTH-1/AUTH-2 in `specs/auth/spec.md`); nothing about this feature requires touching authentication, and the accepted magic-link decision is respected as-is.
- **Process note:** the repository currently contains specs and the knowledge bundle but no application code, so "proceed" concretely means: (a) get answers to the questions below, (b) add a `specs/export/spec.md` with requirements linked to a new `knowledge/decisions/csv-export.md` (with evidence and a Rejected section covering async export, XLSX, and third-party export services), and (c) implement. Since this evaluation run is not allowed to modify project files, the decision/interview capture is deferred until the human answers.

Estimated size: small — one endpoint, one menu/button in the UI, a handful of tests around quoting/escaping.

## 2. PRIOR CONTEXT

Prior context found in the OKF bundle at `E:\PROJEKTI\okf\example\knowledge\` and used above:

- `E:\PROJEKTI\okf\example\knowledge\index.md` — entry point; TaskLite is a lightweight task tracker for freelancers, solo-maintained.
- `E:\PROJEKTI\okf\example\knowledge\constraints\solo-maintainer.md` — one person, a few hours per week; every design choice must minimize operational surface. This is what rules out async export pipelines, stored export artifacts, and third-party export services.
- `E:\PROJEKTI\okf\example\knowledge\constraints\external-users.md` — users are individual freelancers, no corporate identity provider. This is why export scope is per-user with no org/admin export, and why the likely consumers are Excel/Google Sheets rather than a corporate BI pipeline.
- `E:\PROJEKTI\okf\example\knowledge\interviews\2026-07-08-auth-scope.md` — Ivan: "Anything that can break at 3am is out" and "don't store passwords, I don't want the liability." Reinforces minimal-ops design and general liability-averse posture (hence formula-injection escaping by default rather than as an afterthought).
- `E:\PROJEKTI\okf\example\knowledge\decisions\magic-link-auth.md` — accepted 2026-07-08, evidence still current (same-day). Respected, not re-litigated: the export endpoint simply reuses the existing session.
- `E:\PROJEKTI\okf\example\specs\auth\spec.md` — AUTH-1 (magic-link login) and AUTH-2 (30-day session expiry); the export feature inherits these.
- `E:\PROJEKTI\okf\example\knowledge\log.md` — confirms the bundle history contains no prior export/reporting decision, so this is a genuinely new decision area with nothing to conflict with.

No existing decision touches export, reporting, or data formats, so nothing needs a "is this still true?" delta question.

## 3. QUESTIONS

The wiki answers who the users are and how much maintenance the project can absorb, so I am not asking about those. What it does not answer:

1. **Columns and scope:** Should the export include every task field (including internal ones like IDs and timestamps), or a curated set (title, status, due date, created, completed, notes)? And should it export all of the user's tasks, or respect the currently applied filter/view (e.g. only open tasks)?
2. **Excel locale handling:** Many European Excel installs (including Croatian) expect semicolon-delimited CSV and will jam a comma-delimited file into one column. Is plain comma-delimited UTF-8 CSV acceptable, or do you want either (a) a delimiter choice in the UI, or (b) `sep=,` / BOM tricks tuned for Excel? (This determines whether "opens cleanly in my Excel" is a launch requirement or a documented caveat.)
3. **Is CSV enough?** Confirming you don't want native `.xlsx` — CSV keeps us dependency-free and zero-maintenance, XLSX would add a library. If any user demand mentioned "spreadsheet" meaning Excel specifically, say so now and I'll record the trade-off in the decision either way.
