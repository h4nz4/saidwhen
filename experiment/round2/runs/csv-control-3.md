# CSV Export — Evaluation and Proposal (TaskLite)

## 1. RECOMMENDATION

Proceed, but as a **spec-first change, not code** — because there is currently nothing to attach code to.

State of the project: TaskLite (`E:\PROJEKTI\okf\example-control`) contains only a README and a single spec (`specs/auth/spec.md`). There is **no implementation code**, and — more importantly — **no spec for tasks themselves**. The task data model (fields, statuses, ownership) is undefined anywhere in the repo, so "export tasks as CSV" has no defined columns to export.

Proposed path:

1. **Define the task model first (prerequisite).** Add `specs/tasks/spec.md` establishing what a task is (e.g., title, description, status, due date, client/project, created/completed timestamps). CSV export requirements cannot be pinned down without this.
2. **Add an export spec** at `specs/export/spec.md` with requirements along these lines (numbered EXPORT-1..n, matching the existing AUTH-n convention):
   - Export MUST be available only to an authenticated user and MUST include only that user's own tasks (consistent with the magic-link auth model in AUTH-1).
   - Export MUST produce RFC 4180-compliant CSV, UTF-8 with BOM (so Excel opens it correctly), comma-delimited, with a header row.
   - Export MUST respect the user's current filter/view (or export all tasks — this is a product decision, see Questions).
   - **CSV injection protection**: any cell beginning with `=`, `+`, `-`, or `@` MUST be escaped (prefixed) so task titles like `=HYPERLINK(...)` cannot execute as formulas when opened in Excel/Sheets. This is the one genuine security concern in an otherwise low-risk feature.
   - Dates MUST be exported in ISO 8601 to avoid locale ambiguity.
   - Suggested filename convention: `tasklite-tasks-YYYY-MM-DD.csv`.
3. **Implementation** (once specs are agreed): for a tracker of this scale, a synchronous download endpoint (or client-side generation) is sufficient — no background-job/email-delivery machinery is warranted unless task counts are expected to be very large.

Effort estimate: small. The specs are an hour of work once the open questions below are answered; implementation is a day or less in any reasonable stack.

## 2. PRIOR CONTEXT

Context found and used (the entire project is three artifacts):

- `E:\PROJEKTI\okf\example-control\README.md` — describes TaskLite as a fictional lightweight task tracker **for freelancers** (informs the single-user-owns-their-tasks export scoping). It also says to "Browse `knowledge/` and `specs/`" and claims every requirement links to a decision and a human answer — however, **no `knowledge/` directory exists** in the project, and the existing spec contains no such links. So there is no decision history available to consult for prior intent about exports.
- `E:\PROJEKTI\okf\example-control\specs\auth\spec.md` — AUTH-1 (magic-link, passwordless login) and AUTH-2 (30-day inactivity session expiry). Used to require that export sits behind authentication and is scoped to the logged-in user. Also used as the formatting/numbering convention for the proposed new specs.
- **Absent context (load-bearing):** no `specs/tasks/` or any task-model definition, no application code, no prior decisions or discussions about export/reporting. Nothing in the repo indicates CSV export was previously considered, so this proposal starts from zero prior intent.

## 3. QUESTIONS

1. **What columns should the CSV contain?** There is no task spec yet — can you confirm the task fields (title, status, due date, client/project, notes, timestamps?), or should I draft `specs/tasks/spec.md` first and have you review it?
2. **Export scope:** should the export contain *all* of the user's tasks, or the *currently filtered/visible* set (e.g., only open tasks, only one client's tasks)? Or both, via an option?
3. **Delivery mechanism:** is a direct browser download from a button in the UI sufficient, or do you also want an API endpoint / emailed export? (I recommend just the download.)
4. **Excel compatibility target:** is "opens cleanly in Excel and Google Sheets" the bar (UTF-8 BOM, comma delimiter), or do we need locale-specific delimiters (semicolon for some EU locales)?
5. **Volume expectations:** roughly how many tasks might a heavy user have? If it could exceed tens of thousands, I'd spec streaming/pagination; otherwise a simple synchronous export suffices.
6. **Repo hygiene:** the README references a `knowledge/` directory that doesn't exist. Should decisions from this proposal be recorded there (creating it), per the Provenance Convention the README describes?
