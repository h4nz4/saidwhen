# CSV export — evaluation and proposal

## 1. RECOMMENDATION

Proceed — CSV export is a good fit for TaskLite's users and constraints — but implement it as the smallest possible thing, and treat it spec-first, because this project currently has no implementation code and no tasks spec at all.

Proposed shape, derived directly from the recorded constraints:

- **Synchronous, on-demand download.** A single authenticated endpoint (e.g. `GET /tasks/export.csv`) that generates the CSV in-request and streams it back with `Content-Disposition: attachment`. No background jobs, no export queue, no object storage, no emailed files — anything that can fail asynchronously at 3am violates the solo-maintainer constraint (near-zero operational surface).
- **Gated by the existing magic-link session.** Auth is already decided (AUTH-1/AUTH-2); the export endpoint simply requires a valid session and returns only the requesting user's own tasks. No new auth surface.
- **Boring, interoperable format.** RFC 4180 quoting, UTF-8 with BOM (so Excel opens it correctly for freelancers double-clicking the file), comma delimiter, ISO 8601 dates, one header row.
- **CSV-injection hardening.** Prefix any cell starting with `=`, `+`, `-`, or `@` (formula-leading characters) so a task title can't execute in a spreadsheet. Cheap to do, matches the owner's "I don't want the liability" posture from the auth interview.
- **No third-party export/reporting service, no XLSX library.** Native CSV generation is a few dozen lines in any stack; a dependency or SaaS adds exactly the rotation/breakage surface the wiki says the project cannot absorb. Revisit XLSX only if users demand it.

Process, per the project's provenance convention:

1. Answer the open questions below (they are not answered anywhere in `knowledge/`).
2. Add a requirement to `specs/` (e.g. `specs/export/spec.md` — or fold into a new `specs/tasks/spec.md`, since no task data model is specified anywhere yet and the CSV columns will force that definition).
3. When the decision crystallizes, capture `knowledge/decisions/csv-export.md` (with a `## Rejected` section covering async/email export, XLSX, and third-party services), record the human's answers in `knowledge/interviews/<date>-csv-export.md`, append to `knowledge/log.md`, and link from `knowledge/index.md`.

Estimated effort once the task model is pinned down: small — one endpoint, one serializer, one UI button.

## 2. PRIOR CONTEXT

Found and used, all under `E:\PROJEKTI\okf\example\`:

- `knowledge/index.md` — entry point; TaskLite is a lightweight task tracker for freelancers, solo-maintained.
- `knowledge/constraints/solo-maintainer.md` — one person, a few hours/week; every design choice must minimize operational surface. This drives the "synchronous, no background jobs, no third-party service" recommendation.
- `knowledge/constraints/external-users.md` — users are individual freelancers, no corporate IdP. This makes spreadsheet-friendly CSV (Excel/Google Sheets double-click compatibility) the right target, and rules out enterprise-style export integrations.
- `knowledge/decisions/magic-link-auth.md` (status: accepted, 2026-07-08, evidence current) — magic-link auth, no passwords, no OAuth. Respected, not re-litigated: the export endpoint reuses the existing session mechanism. The decision's "no breach liability" spirit motivates the CSV-injection escaping.
- `knowledge/interviews/2026-07-08-auth-scope.md` — Ivan: "Anything that can break at 3am is out"; "Nothing formal" on compliance. This pre-answers questions I would otherwise ask (maintenance budget, compliance requirements), so I am not asking them.
- `specs/auth/spec.md` — AUTH-1 (magic-link login), AUTH-2 (30-day sessions); confirms the auth surface the export endpoint sits behind.
- `knowledge/log.md`, `README.md` — history and project framing; confirmed the repo is a spec/provenance example with **no implementation code and no tasks spec**, which is why the proposal is spec-first and flags the missing task data model.

Nothing in the wiki addresses export, reporting, or the task data model — so this is a fresh decision, not a revisit of an existing one.

## 3. QUESTIONS

Only questions the wiki does not answer:

1. **What is the task data model?** No `specs/tasks/spec.md` exists — nothing defines what fields a task has. Which columns should the CSV contain (e.g. title, status, due date, client/project, notes, created/completed timestamps)? Should answering this also become the missing tasks spec?
2. **Export scope:** should the download contain all of the user's tasks (including completed/archived), or respect the currently applied filters/view in the UI? (Simplest and my default: one "Export all my tasks" button, no filter plumbing — confirm that's acceptable.)
3. **Is CSV alone sufficient for v1**, or have users specifically asked for Excel (.xlsx)? I recommend CSV-only for maintenance reasons and would record XLSX under `## Rejected` with a revisit trigger — confirm no existing user demand says otherwise.

Not asking (already answered by the wiki): maintenance budget (near zero — interview), compliance requirements (none formal — interview), auth mechanism for the endpoint (magic-link session — accepted decision), SSO/enterprise delivery (no corporate IdP — constraint).
