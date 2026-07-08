# CSV Export — Evaluation and Proposal

## 1. RECOMMENDATION

Proceed with the feature, but as a **spec-first task, not a coding task** — and only after resolving a few blocking gaps.

What I found: the TaskLite project at `E:\PROJEKTI\okf\example-control` is currently a documentation-only repository. It contains exactly two files: a README and one auth spec. There is **no application code, no data model spec for tasks, and no existing export functionality** to extend. The README describes the repo as a demonstration of a "Provenance Convention" where every requirement links to the decision that created it, and every decision links to the human answer that justified it.

Given that, my proposal is:

1. **Do not write any implementation code yet.** There is nothing to attach it to — no backend, no task schema, not even a spec describing what a "task" is (fields, statuses, ownership).
2. **Author a new spec** at `specs/export/spec.md` (or `specs/tasks/spec.md` first, if the task model itself is undefined) following the same convention as `specs/auth/spec.md` — numbered, testable MUST-requirements. A reasonable starting shape:
   - EXPORT-1: Authenticated users MUST be able to download their own tasks as a CSV file (scoped to the requesting user only — consistent with the freelancer, single-user framing).
   - EXPORT-2: The CSV MUST include a defined column set (to be confirmed — see Questions).
   - EXPORT-3: The export MUST be safe to open in spreadsheet applications: UTF-8 with BOM for Excel compatibility, RFC 4180 quoting, and CSV-injection mitigation (prefix cell values beginning with `=`, `+`, `-`, `@` to prevent formula execution).
   - EXPORT-4: Export MUST respect the current session rules already defined in AUTH-1/AUTH-2 (no unauthenticated export endpoints, no long-lived signed URLs beyond session policy — to be confirmed).
3. **Follow the provenance convention**: the README states every requirement must link to the decision that created it and the human answer justifying it. The repo's `knowledge/` directory (where decisions apparently live) is referenced by the README but **does not exist in this copy**, so I cannot follow the existing decision format. Before writing the spec, either that directory needs to be restored/created, or the PM should confirm the decision-record format to use. The answers to the questions below would become the linked "human answers."
4. Keep scope minimal for v1: synchronous download of the user's own tasks, one flat CSV, no scheduling, no email delivery, no XLSX. Those can be follow-ups if demand appears.

Estimated effort once questions are answered: small — one spec file plus one decision record; implementation sizing is impossible to estimate until an actual codebase exists.

## 2. PRIOR CONTEXT

The entire project contents (verified by full directory listing — 2 files total):

- `E:\PROJEKTI\okf\example-control\README.md` — Describes TaskLite as a fictional lightweight task tracker for freelancers used to demonstrate the "Provenance Convention": every requirement links to the decision that created it, and every decision links to the human answer that justified it. It tells readers to browse `knowledge/` and `specs/`.
- `E:\PROJEKTI\okf\example-control\specs\auth\spec.md` — The only spec. Two requirements: AUTH-1 (magic-link login, single-use links via email, no passwords stored) and AUTH-2 (sessions expire after 30 days of inactivity). This is relevant to CSV export because any export endpoint must sit behind this auth model.

Notable gaps found while exploring:

- The `knowledge/` directory referenced by the README **does not exist**, so there are no prior decisions or human answers to link to, and no example of the decision-record format to imitate.
- There is **no spec for tasks themselves** — no defined fields, statuses, or ownership model — which makes it impossible to define CSV columns authoritatively.
- There is no application code anywhere in the project (no source files, no package manifest, no build config), so "add CSV export" cannot currently mean a code change.

## 3. QUESTIONS

1. **Is this repo intended to stay spec-only?** Should I deliver CSV export as a spec + decision record (matching the Provenance Convention), or is there an actual TaskLite codebase elsewhere that this request targets?
2. **The `knowledge/` directory referenced in the README is missing.** What is the expected format/location for decision records, so the new EXPORT requirements can link to their provenance as the convention demands? (Or should I create `knowledge/` and establish the format?)
3. **What is the task data model?** There is no tasks spec. What fields does a task have (e.g., title, description, status, due date, project/client, created/completed timestamps, time tracked, billing rate)? This determines the CSV columns.
4. **Export scope:** should the export always be "all of the user's tasks," or should it respect the user's current filters/view (e.g., only open tasks, a date range, a specific client/project)?
5. **Spreadsheet-compatibility details:** any known user base constraints — e.g., must open cleanly in Excel (UTF-8 BOM, possibly semicolon delimiters for some locales) vs. Google Sheets only? And what date/time format and timezone should exported timestamps use?
6. **Delivery mechanism:** synchronous browser download from an authenticated endpoint (my default recommendation), or email/link delivery? If a link, what expiry — and does that interact with the 30-day session policy in AUTH-2?
7. **Privacy/retention:** tasks for freelancers may contain client-identifying or billing data. Are there any constraints on including such fields in exports, or any audit-logging requirement when a user exports their data?
