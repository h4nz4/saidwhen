# CSV export — evaluation and proposal

## 1. RECOMMENDATION

Proceed with CSV export — it is a good fit for TaskLite, but keep it deliberately minimal so it respects the project's standing constraints.

Proposed shape of the feature:

- **On-demand, synchronous download only.** A single "Export CSV" action that streams the logged-in user's tasks as a `text/csv` attachment in the same request. No background jobs, no scheduled exports, no emailed reports, no export history/storage. This is not arbitrary minimalism: TaskLite is solo-maintained with a few hours per week of capacity, and every design choice must minimize operational surface (`knowledge/constraints/solo-maintainer.md`). Async pipelines and schedulers are exactly the kind of "can break at 3am" machinery the owner ruled out in the auth interview (`knowledge/interviews/2026-07-08-auth-scope.md`).
- **Auth-gated per session, own tasks only.** The export endpoint sits behind the existing magic-link session (AUTH-1/AUTH-2 in `specs/auth/spec.md`); a user can export only their own tasks. No new auth mechanism is needed — the accepted magic-link decision (`knowledge/decisions/magic-link-auth.md`, status: accepted, decided today 2026-07-08, evidence current) is respected as-is and covers this feature.
- **Format:** RFC 4180 quoting, UTF-8 with BOM (so Excel opens it correctly without an import wizard — the audience is individual freelancers, not IT-supported employees, per `knowledge/constraints/external-users.md`), comma delimiter, ISO 8601 dates, header row. Include formula-injection hardening (prefix leading `=`, `+`, `-`, `@` in text cells) since the file is destined for spreadsheet apps.
- **Scope of rows/columns:** default to all of the user's tasks with one column per task field — but the task data model is not documented anywhere in the bundle, so the exact column set is an open question (below).
- **Process note:** the repository currently contains no application code, only `knowledge/` and `specs/`. So the concrete next step is a spec, not code: add `specs/export/spec.md` with EXPORT-1 (on-demand CSV of own tasks) and EXPORT-2 (format requirements), each linking to a new `knowledge/decisions/csv-export.md` (with a `## Rejected` section covering scheduled/emailed exports and XLSX). Per the capture-on-decision behavior, I would write that decision file, record any new answers in `knowledge/interviews/2026-07-08-csv-export.md`, append to `knowledge/log.md`, and add the entry to `knowledge/index.md` — once the questions below are answered and the decision crystallizes.

Rejected alternatives I would record in the decision:
- **Scheduled / emailed exports** — recurring infrastructure a solo maintainer cannot afford; violates the minimize-operational-surface constraint.
- **XLSX or Google Sheets integration** — extra dependencies and (for Sheets) an OAuth/API console to maintain; the same reasoning that rejected OAuth for auth applies. CSV opens in every spreadsheet app anyway.
- **Async export job with notification** — unjustified at TaskLite's scale (individual freelancers' personal task lists are small); synchronous streaming suffices.

## 2. PRIOR CONTEXT

Context found in the OKF bundle at `E:\PROJEKTI\okf\example\knowledge\` and used above:

- `E:\PROJEKTI\okf\example\knowledge\index.md` — entry point; TaskLite is a lightweight task tracker for freelancers, solo-maintained. No existing decision, constraint, or interview mentions export/CSV/reporting, so this is a genuinely new decision area.
- `E:\PROJEKTI\okf\example\knowledge\constraints\solo-maintainer.md` — one person, a few hours/week; every design choice must minimize operational surface. Drives the "synchronous on-demand only, no jobs/scheduling" recommendation.
- `E:\PROJEKTI\okf\example\knowledge\constraints\external-users.md` — users are individual freelancers with no corporate identity provider. Drives the Excel-friendly formatting choice and rules out enterprise-flavored delivery (SFTP drops, BI connectors).
- `E:\PROJEKTI\okf\example\knowledge\interviews\2026-07-08-auth-scope.md` — owner's own words: "Anything that can break at 3am is out"; no formal compliance requirements. Already answers the maintenance-budget and compliance questions, so I am not re-asking them.
- `E:\PROJEKTI\okf\example\knowledge\decisions\magic-link-auth.md` — accepted 2026-07-08 (today), evidence fresh and plausible. Respected, not re-litigated: the export endpoint simply lives behind the existing magic-link session.
- `E:\PROJEKTI\okf\example\specs\auth\spec.md` — AUTH-1 (magic-link login) and AUTH-2 (30-day session expiry) define the session the export action will be gated by.
- `E:\PROJEKTI\okf\example\knowledge\log.md` — confirms the bundle history contains only the auth work; nothing export-related was decided and later dropped.

## 3. QUESTIONS

Only the deltas the wiki does not answer (maintenance budget, user identity, and compliance are already answered by the interview and constraints, so I am not asking those):

1. **Which columns?** The task data model isn't documented in `knowledge/` or `specs/`. What fields does a task have (e.g., title, status, due date, client/project, notes, created/completed timestamps), and should the CSV include all of them or a curated subset?
2. **Which rows?** Should "Export CSV" always export all of the user's tasks, or export the currently visible/filtered view (e.g., only open tasks, only one client's tasks)? All-tasks is simpler; filtered-view is more useful if freelancers use exports for per-client invoicing.
3. **Is invoicing the driver?** If the main use case is sending task/time summaries to clients for billing, that may argue for a per-client filter and a stable column order — worth knowing before the spec is written, and worth capturing in the interview file either way.
