# CSV export — evaluation

## 1. RECOMMENDATION

Proceed — CSV export is a good fit for TaskLite and nothing in the knowledge base argues against it. But keep it deliberately small, because the project's binding constraint is operational surface, not features.

Proposed approach:

- **Scope**: a single authenticated "Export tasks as CSV" action that exports the logged-in user's own tasks only. Sits behind the existing magic-link session (AUTH-1/AUTH-2 in `specs/auth/spec.md`), so no new auth work.
- **Implementation shape**: one synchronous endpoint (e.g. `GET /tasks/export.csv`) that streams the user's tasks as an RFC 4180 CSV, generated on request. No background jobs, no export queue, no stored export files, no email delivery — all of those add exactly the kind of "can break at 3am" machinery the solo-maintainer constraint rules out. A freelancer's task list is small enough that synchronous generation is trivially fast.
- **Format details**: UTF-8 with BOM (so Excel opens it correctly), header row, ISO 8601 dates, and formula-injection hardening (prefix cell values starting with `=`, `+`, `-`, `@` per OWASP CSV-injection guidance) since the file will be opened in spreadsheet apps.
- **No XLSX, no Google Sheets integration** for v1. "Spreadsheet" is satisfied by CSV, which every spreadsheet app imports; XLSX would add a dependency and maintenance weight for marginal gain. Revisit only if users demand it.
- **Process**: per the project's Provenance Convention, once the open questions below are answered I would record the answers in `knowledge/interviews/<date>-csv-export.md`, write `knowledge/decisions/csv-export.md` (with the Rejected section covering background-job export, XLSX, and third-party integrations), add a `specs/export/spec.md` with requirements linking to that decision, and append to `knowledge/log.md`. Note: the example project currently contains no application code (only `knowledge/` and `specs/`), so the concrete deliverable at this stage is the spec + decision, ready to guide implementation.

## 2. PRIOR CONTEXT

Context found in the OKF bundle at `E:\PROJEKTI\okf\example\knowledge\` and used above:

- `E:\PROJEKTI\okf\example\knowledge\index.md` — entry point; TaskLite is a lightweight task tracker for freelancers, solo-maintained.
- `E:\PROJEKTI\okf\example\knowledge\constraints\solo-maintainer.md` — one person, a few hours/week; every design choice must minimize operational surface. This is why I propose a synchronous endpoint and reject job queues, stored exports, and XLSX libraries.
- `E:\PROJEKTI\okf\example\knowledge\constraints\external-users.md` — users are individual freelancers, no corporate IdP. Confirms exports are per-user personal data (own tasks only), and there is no "admin exports the whole org" requirement to design for.
- `E:\PROJEKTI\okf\example\knowledge\decisions\magic-link-auth.md` (status: accepted, 2026-07-08, evidence current) — auth is magic-link sessions. The export endpoint simply lives behind the existing session; this decision is respected, not re-litigated.
- `E:\PROJEKTI\okf\example\knowledge\interviews\2026-07-08-auth-scope.md` — Ivan: "Anything that can break at 3am is out" and no formal compliance requirements. This pre-answers questions I would otherwise ask about maintenance tolerance and data-export compliance (e.g. GDPR tooling), so I am not asking them.
- `E:\PROJEKTI\okf\example\specs\auth\spec.md` — AUTH-1 (magic-link login) and AUTH-2 (30-day sessions) define the session the export endpoint reuses.

No existing decision, constraint, or interview touches export/reporting, so this is a fresh decision rather than a delta question on a stale one.

## 3. QUESTIONS

Only questions the wiki does not already answer:

1. **What should one CSV row be, and which columns?** I'd default to one row per task with: title, description, status, due date, created date, completed date, tags/project. Is anything missing or unwanted (e.g. time tracked, client name — do those fields even exist in TaskLite's task model)?
2. **Export scope**: always all of the user's tasks, or should the export respect the currently applied filter/view (e.g. "only open tasks for client X")? Filter-respecting is more useful but slightly more work.
3. **Does "download as a spreadsheet" strictly mean a CSV file download is acceptable**, or do you have reason to believe users specifically expect a native .xlsx file? (I recommend CSV; asking only to confirm I'm not misreading the request.)
