# CSV Export — Evaluation and Proposal (TaskLite)

## 1. RECOMMENDATION

Proceed, but start by writing a spec rather than code — because there is currently nothing to attach an implementation to.

Key finding from exploring the project: TaskLite at `E:\PROJEKTI\okf\example-control` is a spec-only project. It contains a README and a single authentication spec. There is no application code, no data model, and — critically — **no spec for tasks themselves**. We cannot meaningfully specify "export tasks as CSV" before the project defines what a task is (its fields, states, and ownership).

Proposed path:

1. **Define the task model first** (blocking prerequisite). Add `specs/tasks/spec.md` capturing the task entity: fields (e.g., title, description, status, due date, client/project, created/completed timestamps, tags), statuses, and per-user ownership. Column selection for CSV export falls directly out of this.
2. **Add an export spec** at `specs/export/spec.md` following the existing spec style (requirement IDs like `EXPORT-1`, RFC-2119 MUST language, mirroring `specs/auth/spec.md`). Suggested requirements to draft:
   - EXPORT-1: An authenticated user MUST be able to download their own tasks (and only their own) as a CSV file.
   - EXPORT-2: CSV format — RFC 4180 quoting, UTF-8 with BOM (so Excel opens it correctly), header row, ISO 8601 dates, stable documented column order.
   - EXPORT-3: Formula-injection hardening — cell values beginning with `=`, `+`, `-`, `@` MUST be escaped/prefixed so the file is safe to open in Excel/Sheets ("spreadsheet" is the stated use case, so this is in scope, not gold-plating).
   - EXPORT-4: Scope of export — which tasks are included (all vs. current filter/view; include completed/archived or not) — pending answers to the questions below.
3. **Respect the auth constraints already on file**: export must run inside an authenticated session per AUTH-1/AUTH-2 (magic-link login, 30-day inactive session expiry). The export endpoint/action must not create a new unauthenticated access path (e.g., no long-lived tokenized download URLs unless separately specified).
4. **Keep it minimal**: a synchronous, on-demand download of the user's tasks. No scheduled exports, no XLSX, no email delivery — unless the PM says otherwise. For a freelancer-scale task list, streaming/pagination concerns are unnecessary.

Effort estimate once the task model is defined: the export feature itself is small (one endpoint/action + serializer + a download button), roughly a day of work including tests.

## 2. PRIOR CONTEXT

I explored the entire project. It contains exactly two files:

- `E:\PROJEKTI\okf\example-control\README.md` — describes TaskLite as "a fictional lightweight task tracker for freelancers." This anchors the product scope (single-user freelancer use, lightweight — arguing for a simple, minimal export). The README also says to "Browse `knowledge/` and `specs/`," but **no `knowledge/` directory exists in this project** — so there is no decision log or prior human answers available to consult. The only discoverable convention is the spec style itself.
- `E:\PROJEKTI\okf\example-control\specs\auth\spec.md` — AUTH-1 (magic-link login, no passwords) and AUTH-2 (30-day inactive session expiry). Used above: the export must operate within this session model, and its spec should follow this file's format (numbered requirement IDs, MUST language).

Notably absent (and load-bearing for this evaluation): no task spec, no code, no data model, no UI. That absence is the main driver of the recommendation to spec the task model before the export.

## 3. QUESTIONS

1. **What is a task?** There is no task spec or data model in the repo. What fields does a task have (title, description, status, due date, client/project, tags, timestamps, ...)? Should I draft `specs/tasks/spec.md` as part of this work, or does a task definition exist somewhere outside this repository?
2. **Export scope:** Should the CSV contain all of the user's tasks, or only the currently filtered/visible set? Should completed and/or archived tasks be included by default?
3. **Columns:** Export every field, or a curated subset? Any fields to deliberately exclude?
4. **Spreadsheet target:** Is Excel the primary consumer (freelancers commonly use it)? If so, I'll default to UTF-8 with BOM and comma delimiter — but note that users in locales where Excel expects semicolons (e.g., much of Europe) may need a delimiter option. Do we care about that now, or defer?
5. **Is CSV enough,** or is XLSX/Google Sheets export anticipated soon? (This affects whether we design a generic export layer or the simplest CSV-only path — my recommendation is CSV-only for now.)
6. **Provenance:** The README references a `knowledge/` directory that doesn't exist here. Should the decisions from your answers to these questions be recorded there per the Provenance Convention, and if so, in what format?
