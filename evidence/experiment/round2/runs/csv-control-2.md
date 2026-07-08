# CSV Export — Evaluation (TaskLite)

## 1. RECOMMENDATION

Proceed, but start with a spec, not code — there is currently no code to attach an implementation to.

TaskLite as it exists in this repository is a documentation/spec-only project: it contains a README and a single authentication spec (`specs/auth/spec.md`). There is no application code, no data model for tasks, no API layer, and no UI. The right next step is therefore to define the CSV export as a new requirements spec (e.g., `specs/export/spec.md`) following the existing convention, where each requirement is a numbered, testable statement (matching the AUTH-1 / AUTH-2 style).

Proposed shape of the feature, subject to answers to the questions below:

- **Scope**: a user can download all of their own tasks as a single CSV file (`EXPORT-1`). Given AUTH-1 (magic-link login, per-user accounts), export must be scoped to the authenticated user's tasks only — never other users' data (`EXPORT-2`).
- **Format**: RFC 4180-compliant CSV, UTF-8 encoded with a BOM (so Excel opens it correctly), header row included, fields quoted/escaped per the RFC (`EXPORT-3`). Note: no task schema is defined anywhere in the repo, so the column set (title, status, due date, created date, tags, etc.) cannot be derived from existing specs and must be decided.
- **Safety**: cell values beginning with `=`, `+`, `-`, or `@` must be escaped to prevent CSV/formula injection when the file is opened in a spreadsheet application (`EXPORT-4`). This is the one non-obvious requirement worth capturing explicitly.
- **Delivery**: synchronous download from a button in the task list UI is sufficient for a freelancer-scale tool (the product is described as "lightweight" and for individual freelancers, so task counts will be small — no need for background jobs, pagination of exports, or email delivery). Recommend a `GET /tasks/export.csv`-style authenticated endpoint with `Content-Disposition: attachment`.
- **Deliberately out of scope for v1** (unless the PM says otherwise): filtered/partial exports, XLSX format, scheduled/recurring exports, and import. CSV covers the stated "spreadsheet" need; XLSX adds a dependency for little gain.

Effort: small. Once the schema questions are answered, this is a one-spec, and later one-endpoint-plus-one-button, feature.

## 2. PRIOR CONTEXT

Prior context found in the project is minimal:

- `E:\PROJEKTI\okf\example-control\README.md` — describes TaskLite as "a fictional lightweight task tracker for freelancers" demonstrating the Provenance Convention, and says to browse `knowledge/` and `specs/`, where "every requirement links to the decision that created it, and every decision links to the human answer that justified it."
- `E:\PROJEKTI\okf\example-control\specs\auth\spec.md` — the only spec present. Defines AUTH-1 (magic-link login, no passwords) and AUTH-2 (30-day inactivity session expiry). Relevant to CSV export because it establishes that users are authenticated individuals, so exports must be per-user and behind auth.

Notable gaps in prior context:

- The `knowledge/` directory referenced by the README **does not exist** in this copy of the project, so there are no prior decisions or human answers to consult, and no provenance links can be followed or created against existing decision records.
- There is **no task spec** (`specs/tasks/` or similar) defining what a task is — fields, statuses, or relationships. The core entity being exported is undefined.
- There is no code, so no existing patterns (framework, endpoint conventions, download handling) constrain the implementation.

## 3. QUESTIONS

1. **Task schema**: What fields does a task have? There is no task spec in the repo. Which columns should the CSV include, and in what order (e.g., ID, title, description, status, due date, created/completed dates, tags, client/project)?
2. **Export scope**: Should the export always be "all my tasks," or should it respect the currently applied filters/view (e.g., only active tasks, only one project)? All-tasks-only is simplest for v1.
3. **Provenance/knowledge directory**: The README says every requirement must link to the decision that created it, but the `knowledge/` directory is missing here. Should I create `knowledge/` decision records for this feature (and link EXPORT-* requirements to them), or is that convention out of scope for this change?
4. **Formats**: Is CSV alone sufficient, or is Excel (.xlsx) compatibility a hard requirement beyond "opens cleanly in Excel"? (UTF-8 BOM CSV opens fine in Excel; native XLSX is extra work.)
5. **Locale/formatting**: Any requirements for date format (recommend ISO 8601), timezone (recommend the user's timezone or UTC, stated in the header), and delimiter (comma vs. semicolon for European Excel locales)?
6. **Data sensitivity**: Are there any privacy/compliance constraints on exports (e.g., audit logging of export events)? For a freelancer tool exporting the user's own data, I'd assume none, but flagging it.
