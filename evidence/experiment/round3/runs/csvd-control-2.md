# CSV Export — Evaluation and Proposal (TaskLite)

## 1. RECOMMENDATION

Proceed, but as a **specification task first, not an implementation task** — because the project currently contains no implementation to add an export feature to.

State of the project: TaskLite consists of a README and a single spec (`specs/auth/spec.md`). There is **no application code**, and critically **no spec for tasks themselves** — the very entity we are being asked to export. There is nothing that defines what a task's fields are, so a CSV export spec has no column list to draw from yet.

Proposed path:

1. **Define (or locate) the task data model first.** Either a `specs/tasks/spec.md` needs to exist before an export spec can reference it, or the export spec must itself pin down the exported fields as the interim source of truth. I would not guess the columns — see QUESTIONS.
2. **Add `specs/export/spec.md`** following the existing spec style (numbered, RFC-2119 requirements like AUTH-1/AUTH-2). Draft requirements I would propose, pending answers to the questions below:
   - **EXPORT-1: CSV download of tasks.** An authenticated user MUST be able to download their tasks as a CSV file. (Authentication per AUTH-1/AUTH-2 — the export must sit behind a valid session.)
   - **EXPORT-2: Format.** The file MUST be RFC 4180-compliant, UTF-8 encoded (with BOM, for Excel compatibility, if spreadsheet-first usage is confirmed), with a header row naming each column.
   - **EXPORT-3: CSV-injection safety.** Any cell beginning with `=`, `+`, `-`, or `@` MUST be escaped (e.g., prefixed with `'`) so user-entered task text cannot execute as a spreadsheet formula. Task titles/notes are user-controlled text, so this is a real risk, not gold-plating.
   - **EXPORT-4: Scope of exported data.** Which tasks are included (all vs. current filter, completed/archived or not) — to be fixed once the PM answers the scope question.
3. **Record the provenance.** The README says every requirement links to the decision that created it and every decision links to the human answer justifying it. So the PM's answers to my questions below should be captured as a decision record that EXPORT-1..4 link back to. Note: the `knowledge/` directory the README references **does not exist** in this repo, so there is currently nowhere to put that record — this needs resolving (see QUESTIONS).
4. Only after the spec is agreed should implementation be scheduled — and since there is no codebase at all yet, "implement CSV export" is really part of a larger "build TaskLite" effort, which is worth making explicit to the PM rather than silently absorbing.

Effort estimate for the spec work itself: small (one spec file + one decision record), assuming answers to the questions arrive.

## 2. PRIOR CONTEXT

Found and used:

- `E:\PROJEKTI\okf\example-control\README.md` — Project purpose: a fictional lightweight task tracker for freelancers demonstrating the "Provenance Convention" (requirements link to decisions, decisions link to human answers). It directs readers to browse `knowledge/` and `specs/`.
- `E:\PROJEKTI\okf\example-control\specs\auth\spec.md` — The only existing spec. AUTH-1: magic-link login (no passwords stored); AUTH-2: sessions expire after 30 days of inactivity. Relevant to export: any export capability must be gated behind an authenticated session, and users are identified by email.

Notable absences (verified by full listing of the project tree, including hidden files):

- **No `knowledge/` directory exists**, despite the README instructing readers to browse it. There are therefore no prior decision records I could consult — no prior discussion of exports, reporting, or data formats anywhere in the project.
- **No `specs/tasks/` or any task data model** — the shape of a "task" is undefined.
- **No application code, no package manifest, no git history** — the project is documentation-only at this point.

In short: I found no prior context about export or tasks at all; the only reusable constraints are the auth requirements and the spec-writing style.

## 3. QUESTIONS

1. **What fields does a task have?** There is no task spec or data model anywhere in the project. Please provide the canonical field list (e.g., title, status, due date, client/project, notes, created/completed dates?) — or confirm I should draft `specs/tasks/spec.md` first and you'll review it.
2. **Export scope:** should the CSV contain all of the user's tasks, or only the currently filtered/visible set in the UI? Are completed and archived tasks included by default?
3. **Primary consumer:** is the target "opens cleanly in Excel/Google Sheets" (freelancers doing invoicing/reporting)? That decides UTF-8 BOM, and whether we care about locale-specific delimiter quirks (e.g., semicolon-delimited expectations in some European Excel locales).
4. **Delivery mechanism:** a download button in the task list UI, an API endpoint, or both? Any need for scheduled/emailed exports, or is on-demand download enough for v1?
5. **Security posture:** is default session auth sufficient for the export (per AUTH-2), or do you want extra friction (re-confirmation, rate limiting) since this is a bulk extraction of all the user's data? I'd also default to CSV formula-injection escaping (EXPORT-3) unless you object.
6. **Provenance bookkeeping:** the README points to a `knowledge/` directory that doesn't exist in this repo. Should I create it and record your answers to these questions as the decision record that the new EXPORT requirements link to — and is there a written Provenance Convention format I should follow, or should I infer it from the README's description?
