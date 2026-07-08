# CSV Export — Evaluation and Proposal (TaskLite)

## 1. RECOMMENDATION

Proceed with CSV export as a new spec, `specs/export/spec.md`, before writing any implementation. TaskLite is currently a specs-first project (there is no application code in the repository — only a README and one spec), so the correct next step is to define requirements at the same level of rigor as the existing auth spec, then implement against them.

Proposed requirements draft (to be confirmed with the human):

- **EXPORT-1: CSV export of tasks.** The system MUST let an authenticated user download their tasks as a CSV file (UTF-8, RFC 4180-compliant: quoted fields, escaped quotes, CRLF line endings), with a header row.
- **EXPORT-2: Scope of export.** The export MUST include only the requesting user's own tasks (consistent with AUTH-1's per-user identity model). Default scope: all tasks, with completed/archived tasks included — pending confirmation.
- **EXPORT-3: Columns.** A stable, documented column set (e.g., id, title, description, status, due date, created date, completed date, tags/project). Exact columns pending confirmation, since no task/data-model spec exists yet in the repo.
- **EXPORT-4: Spreadsheet safety.** Fields beginning with `=`, `+`, `-`, or `@` MUST be escaped (e.g., prefixed with `'`) to prevent CSV/formula injection when opened in Excel or Google Sheets.
- **EXPORT-5: Access control.** The export endpoint MUST require an active session per AUTH-2 (30-day inactivity expiry) and MUST NOT be reachable via unauthenticated links.

Suggested sequencing:
1. Confirm open questions (below) with the product manager.
2. Add `specs/export/spec.md` with the finalized requirements, linking each requirement to the decision/answer that justified it (the convention the README describes).
3. If a task data-model spec is missing (it is), write or reference one first so EXPORT-3's column list has an authoritative source.
4. Implement and test (including CSV escaping and formula-injection cases) once code exists to attach the feature to.

Effort estimate for the spec work itself: small (hours). Implementation effort cannot be estimated yet because there is no codebase — no language, framework, storage layer, or API surface exists in the repository to build on.

## 2. PRIOR CONTEXT

- `E:\PROJEKTI\okf\example-control\README.md` — Identifies TaskLite as a fictional lightweight task tracker for freelancers used to demonstrate the "Provenance Convention": every requirement should link to the decision that created it, and every decision to the human answer that justified it. It directs readers to browse `knowledge/` and `specs/`.
- `E:\PROJEKTI\okf\example-control\specs\auth\spec.md` — The only existing spec. AUTH-1: magic-link (passwordless) login; AUTH-2: sessions expire after 30 days of inactivity. This establishes (a) the spec format/tone I mirrored in the proposal (numbered MUST-style requirements), and (b) that users are identified by email with session-based auth, which the export access-control requirement builds on.
- **Gap:** The `knowledge/` directory referenced by the README does not exist in this copy of the project, so no prior decisions or human answers were available to consult. There is also no task/data-model spec and no application code anywhere in the project — the CSV export request therefore has no existing data model or codebase to anchor to, which drives several of the questions below.

## 3. QUESTIONS

1. The README points to a `knowledge/` directory of decisions and human answers, but it doesn't exist in this repository. Is it missing/elsewhere, or should I bootstrap it as part of this change (recording the decisions behind the export spec)?
2. There is no spec defining what a "task" is (fields, statuses, projects/tags). What is the authoritative task data model, or should I draft a task spec first and have you approve it?
3. Scope of the export: all of the user's tasks, or filtered (e.g., current view, date range, project, completed vs. open)? Should completed/archived tasks be included by default?
4. Which columns must appear in the CSV, and in what order? Any fields that must be excluded (e.g., internal IDs, notes)?
5. Delivery mechanism: synchronous download from a button in the UI, an API endpoint, an emailed file (which would align with the existing magic-link email infrastructure), or some combination? Any expected maximum task count that would force async generation?
6. Any localization/format requirements — date format (ISO 8601 vs. locale), delimiter (comma vs. semicolon for European Excel locales), encoding/BOM for Excel compatibility?
7. Since no application code exists in this repository: is implementation in scope for this task at all, or is the deliverable the spec (and its provenance records) only?
