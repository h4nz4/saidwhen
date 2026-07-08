# CSV Export for TaskLite — Evaluation and Proposal

## 1. RECOMMENDATION

Proceed, but as a **spec-first change**, because there is no application code in this repository to modify. TaskLite (`E:\PROJEKTI\okf\example-control`) currently consists of only a README and one spec file (`specs/auth/spec.md`). The project's stated convention is that every requirement is captured as a spec linked to the decision that created it, so CSV export should enter the project the same way.

Concretely, I propose:

1. **Add a new capability spec** at `specs/export/spec.md` (parallel to `specs/auth/spec.md`), following the existing style — numbered requirement IDs with RFC-2119 keywords. Draft requirements:
   - **EXPORT-1: CSV download** — The system MUST let an authenticated user download their tasks as a CSV file, generated on demand.
   - **EXPORT-2: Scope** — The export MUST include only tasks belonging to (or visible to) the requesting user, and SHOULD respect any filters active at the time of export (pending answers to the questions below).
   - **EXPORT-3: Format** — The file MUST be RFC 4180-compliant CSV, UTF-8 encoded with a BOM (for Excel compatibility), comma-delimited, with a header row. Fields containing commas, quotes, or newlines MUST be quoted; cells beginning with `=`, `+`, `-`, or `@` MUST be escaped to prevent CSV/formula injection when opened in spreadsheet software.
   - **EXPORT-4: Columns** — A defined, stable column set (e.g., id, title, description, status, priority, due date, created/completed timestamps, tags) — exact set to be confirmed.
   - **EXPORT-5: Dates** — Timestamps MUST be exported in ISO 8601 (or a confirmed alternative), in a documented timezone.
   - **EXPORT-6: Auth** — Export MUST require an authenticated session per AUTH-1/AUTH-2; the endpoint must not be accessible via unauthenticated links.
2. **Record the decision** in the project's provenance structure. The README references a `knowledge/` directory that does not yet exist; the decision entry justifying EXPORT-* should create it (or the README should be corrected — see Questions).
3. **Defer implementation details** (endpoint vs. client-side generation, streaming for large exports, rate limiting) until the spec is approved, since there is no codebase yet to anchor those choices.

Effort estimate for the spec work itself: small (one spec file + one decision record). Implementation effort cannot be estimated until an actual codebase exists or is identified.

## 2. PRIOR CONTEXT

The repository is minimal; I found and used:

- `E:\PROJEKTI\okf\example-control\README.md` — Describes TaskLite as a fictional lightweight task tracker for freelancers demonstrating the "Provenance Convention": every requirement links to the decision that created it, and every decision links to the human answer that justified it. It directs readers to `knowledge/` and `specs/`.
- `E:\PROJEKTI\okf\example-control\specs\auth\spec.md` — The only existing spec. Establishes the house style (H1 capability name, `## Requirements`, `### AUTH-n: Title` headings, MUST-style requirement sentences). Relevant content: AUTH-1 (magic-link login, no passwords stored) and AUTH-2 (30-day inactivity session expiry) — these constrain how the export endpoint must be authenticated.
- **Notable absence:** the `knowledge/` directory referenced by the README does not exist, and there is no application code, no data model or task schema, no API definition, and no existing spec for tasks themselves. This means (a) there is no defined "task" field list to export, and (b) the provenance chain the README promises has no anchor yet for the export decision.

## 3. QUESTIONS

1. **Task schema:** There is no spec defining what a "task" is. What fields does a task have (title, description, status, priority, due date, tags, project/client, time tracked, etc.), and which of them should appear in the CSV? Should a `specs/tasks/spec.md` be written first?
2. **Export scope:** Should the export always include all of the user's tasks, or the currently filtered/visible view (e.g., only open tasks, a date range, a specific client)? Should archived/completed tasks be included by default?
3. **Delivery mechanism:** Is this a synchronous download from the UI (button → file), an API endpoint, an emailed file, or some combination? (Freelancer-scale data suggests synchronous download is enough, but I'd like that confirmed.)
4. **Spreadsheet compatibility target:** Is Excel the primary consumer (which argues for UTF-8 with BOM and possibly locale-aware delimiters), or is plain RFC 4180 CSV sufficient? Any need for XLSX instead of/in addition to CSV?
5. **Provenance bookkeeping:** The README points to a `knowledge/` directory that doesn't exist. Should I create it as part of this change to record the decision behind the export spec (per the Provenance Convention), or is that structure maintained elsewhere?
6. **Codebase location:** This repository contains no implementation. Is the actual TaskLite code elsewhere, or is this change intended to remain spec-only for now?
