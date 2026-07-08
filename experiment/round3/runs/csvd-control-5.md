# CSV Export — Evaluation and Proposal (TaskLite)

## 1. RECOMMENDATION

Proceed, but as a spec-first change — and get a few scope decisions from a human before writing it.

Current state of the project: TaskLite is a spec-driven project. The repository at `E:\PROJEKTI\okf\example-control` currently contains only a README and a single spec (`specs/auth/spec.md`). There is no application code, no task/data-model spec, and no existing export functionality of any kind. Notably, there is not even a spec describing what a "task" is (its fields), which CSV export directly depends on — a CSV export is essentially a serialization of the task schema.

Proposed approach:

1. **Add a new spec** at `specs/export/spec.md` (following the structure and requirement-ID convention used in `specs/auth/spec.md`, e.g. `EXPORT-1`, `EXPORT-2`, ...) covering roughly:
   - **EXPORT-1 (Scope):** An authenticated user MUST be able to download their own tasks as a CSV file. Export is per-user; a user can never export another user's tasks (this follows from the auth model — magic-link sessions per AUTH-1/AUTH-2 — so the export endpoint MUST require an active session).
   - **EXPORT-2 (Columns):** The CSV MUST include a defined, ordered set of task fields with a header row. (Exact columns depend on the task data model — see Questions.)
   - **EXPORT-3 (Format):** UTF-8 encoding (with BOM, if Excel is a primary consumer), comma delimiter, RFC 4180 quoting/escaping, ISO 8601 dates (timezone handling to be decided).
   - **EXPORT-4 (Safety):** Cell values beginning with `=`, `+`, `-`, or `@` MUST be neutralized (e.g. prefixed with `'`) to prevent CSV/formula injection when the file is opened in a spreadsheet application. Task titles/notes are user-controlled free text, so this is a real risk, not a formality.
   - **EXPORT-5 (Delivery):** Synchronous download with a `Content-Disposition` attachment and a predictable filename (e.g. `tasklite-tasks-YYYY-MM-DD.csv`), unless expected data volumes justify async/emailed export (unlikely for a freelancer-scale tool — recommend keeping it synchronous).
2. **If a task data-model spec doesn't exist yet, create it first** (e.g. `specs/tasks/spec.md`) or at minimum define the exported columns explicitly in the export spec, since the export contract is meaningless without an agreed field list.
3. Keep v1 minimal: whole-account export ("all my tasks"), one flat CSV, no column picker, no XLSX. Filtered export (e.g. by project/status/date range, or "export current view") can be a follow-up requirement if the PM confirms it's needed.

Effort estimate: small. The main risk is not technical but definitional — agreeing on the column set and on whether the export reflects a filtered view or the whole account.

One housekeeping note: the README says to "browse `knowledge/` and `specs/`" and describes a Provenance Convention where every requirement links to the decision that created it, but no `knowledge/` directory exists in this project. Either the directory is missing or the README is stale; worth reconciling before adding new requirements that are supposed to carry provenance links.

## 2. PRIOR CONTEXT

The entire project contents (two files) were reviewed:

- `E:\PROJEKTI\okf\example-control\README.md` — describes TaskLite as a fictional lightweight task tracker for freelancers, used to demonstrate the "Provenance Convention"; instructs readers to browse `knowledge/` and `specs/`, with every requirement linking to a decision and every decision linking to a human answer. The referenced `knowledge/` directory does not exist in this project, so no decision/provenance records were available to consult.
- `E:\PROJEKTI\okf\example-control\specs\auth\spec.md` — the only existing spec. Defines AUTH-1 (magic-link login, single-use links, no passwords stored) and AUTH-2 (sessions expire after 30 days of inactivity). Used as: (a) the structural template for the proposed export spec (requirement-ID + MUST-style wording), and (b) the basis for the requirement that export be gated behind an authenticated session.

No prior context exists about tasks (fields/schema), export, reporting, integrations, or data formats — nothing in the project mentions CSV or export today. There is also no application code, so nothing constrains the implementation approach.

## 3. QUESTIONS

1. **What exactly is a "task" for export purposes?** There is no task data-model spec. Which fields should the CSV include, and in what order — e.g. title, status, project/client, due date, created date, completed date, notes, tags, time tracked, billable amount? (For freelancers, client/project and billable columns may be the whole point of the export.)
2. **Export scope:** should it always export all of the user's tasks, or export the currently filtered/visible view (by project, status, date range)? A v1 of "all tasks" is simplest — is that acceptable?
3. **Primary consumer:** is the target Excel (which argues for UTF-8 BOM and possibly locale-aware delimiters), Google Sheets, or downstream tooling (which argues for strict plain RFC 4180 CSV)?
4. **Date/time format:** ISO 8601 in UTC, or localized to the user's timezone? (Matters for due dates and completed-at timestamps landing on the "right" day in a spreadsheet.)
5. **Should completed/archived tasks be included** by default, excluded, or toggleable?
6. **Provenance/process:** the README's Provenance Convention says every requirement must link to the decision that created it, but this project has no `knowledge/` directory. Should I create the decision record structure (recording your answers to these questions as the justifying decisions for the EXPORT-* requirements), or is the convention out of scope here and the missing directory/stale README something you'll resolve separately?
