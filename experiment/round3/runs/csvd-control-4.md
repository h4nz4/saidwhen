# CSV Export — Evaluation and Proposal

## 1. RECOMMENDATION

Proceed, but as a **spec-first change, not a code change** — this project currently contains no application code at all. TaskLite is a documentation/specification project (a README plus `specs/auth/spec.md`), so "adding CSV export" here means authoring a new requirements spec, e.g. `specs/export/spec.md`, in the same style as the existing auth spec (numbered, RFC-2119 "MUST" requirements).

Proposed spec skeleton (draft requirements to confirm with the PM):

- **EXPORT-1: CSV download** — The system MUST let an authenticated user download their tasks as a CSV file (`text/csv; charset=utf-8`, RFC 4180: comma-delimited, CRLF line endings, quoted fields containing commas/quotes/newlines, header row).
- **EXPORT-2: Scope of data** — The export MUST include only the requesting user's own tasks (TaskLite is a tracker for freelancers, so per-user scoping is the natural boundary). Column set to be defined once a task data model spec exists — notably, there is no `specs/tasks/spec.md` today, which is a gap this feature exposes.
- **EXPORT-3: Authentication** — Export MUST be available only within a valid session per AUTH-1/AUTH-2 (magic-link auth, 30-day inactivity expiry). No unauthenticated or long-lived export URLs, since those would bypass the passwordless session model.
- **EXPORT-4: Spreadsheet-injection safety** — Cell values beginning with `=`, `+`, `-`, or `@` MUST be escaped (e.g. prefixed with `'`) so user-entered task titles/notes cannot execute as formulas when opened in Excel/Sheets.
- **EXPORT-5 (optional): Excel friendliness** — Emit a UTF-8 BOM and ISO-8601 dates, pending PM confirmation of the primary consumer (Excel vs. Google Sheets vs. programmatic use).

Sizing: small. One new spec file plus a decision record if the project's Provenance Convention is followed (see caveat below). I recommend not writing the spec until the questions in section 3 are answered, since the column set and delivery mechanism depend on them.

## 2. PRIOR CONTEXT

Context found and used (the entire project is two files):

- `E:\PROJEKTI\okf\example-control\README.md` — TaskLite is a fictional lightweight task tracker for freelancers demonstrating the "Provenance Convention": every requirement should link to the decision that created it, and every decision to the human answer that justified it. It tells readers to browse `knowledge/` and `specs/`.
  - **Caveat found:** the `knowledge/` directory the README references does not exist in this checkout. There are no decision records, no prior decisions about exports, reporting, or data formats, and no convention file showing how requirement→decision links are formatted. I therefore cannot follow the provenance-linking convention concretely, and there is no prior context suggesting CSV export was previously considered or rejected.
- `E:\PROJEKTI\okf\example-control\specs\auth\spec.md` — the only existing spec. Establishes the house style (H1 domain, `## Requirements`, `### PREFIX-N: Title`, MUST-language) that the new export spec should mirror, and two requirements the export feature must respect: AUTH-1 (single-use magic-link login, no passwords) and AUTH-2 (sessions expire after 30 days of inactivity).

Not found (relevant absences): no task data model spec (task fields are undefined anywhere), no API or UI specs, no application code, no `knowledge/` decision log.

## 3. QUESTIONS

1. This repo is spec-only — do you want me to (a) author a requirements spec for CSV export in `specs/export/spec.md`, (b) actually implement export code somewhere I haven't found, or (c) both? If there is application code in another location, where?
2. The README says every requirement must link to the decision that created it via `knowledge/`, but no `knowledge/` directory exists here. Should I create the decision record for this feature (and if so, is there a template or example of the expected format), or skip provenance links for now?
3. There is no spec defining what a "task" is. What fields does a task have, and which should appear as CSV columns (e.g. title, status, due date, project/client, created/completed timestamps, notes)?
4. Should the export cover all of the user's tasks, or respect the user's current view (filters such as status, date range, project/client)?
5. How is the file delivered — direct browser download from a button, or emailed (which would align with the existing magic-link email infrastructure)? Any size expectations that would argue for async generation?
6. Who is the primary consumer of the file — Excel, Google Sheets, or programmatic tools? This decides UTF-8 BOM, date formatting, and whether we also want a locale-specific delimiter option.
7. Any privacy/compliance constraints on exports (e.g. audit-logging that an export happened), given tasks may contain client-confidential notes?
