# CSV export — evaluation and proposal

## 1. RECOMMENDATION

Proceed, but keep it deliberately minimal. Recommended shape:

- **A synchronous "Export CSV" action** (a button on the task list that hits a single endpoint, or even a pure client-side download of the already-loaded tasks). No background jobs, no export queue, no email-delivery of files, no scheduled exports — TaskLite is solo-maintained a few hours per week, so anything with async infrastructure or a failure mode "at 3am" is out of scope by standing constraint.
- **CSV only, one flat file.** Do not add XLSX/Google Sheets/JSON variants speculatively. CSV opens in every spreadsheet tool the target users (individual freelancers) actually use.
- **Stream/generate on request from live data**, no stored export artifacts (nothing to retain, expire, or leak; keeps the liability posture consistent with the project's "don't store what creates liability" instinct from the auth scoping).
- **Practical details I'd bake in:** UTF-8 with BOM (so Excel renders non-ASCII correctly), RFC 4180 quoting, formula-injection hardening (prefix `=`, `+`, `-`, `@` cell values with `'`), ISO-8601 dates, filename like `tasklite-tasks-YYYY-MM-DD.csv`. Export requires an authenticated session and returns only the requesting user's own tasks.
- **Process:** once the open questions below are answered, capture the crystallized decision as `knowledge/decisions/csv-export.md` (with a `## Rejected` section covering XLSX and async/background export), record the PM/owner's answers in `knowledge/interviews/<date>-csv-export.md`, add a `specs/export/spec.md` with requirements linking back to the decision, and append to `knowledge/log.md` — per the project's read-first/capture-on-decision convention.

One caveat: the repo currently contains only `knowledge/` and `specs/` (it is the Provenance Convention example project — there is no application code yet). So "how to proceed" concretely means: answer the scoping questions, write the decision + spec with provenance links, and implement the export when/where the TaskLite codebase exists.

## 2. PRIOR CONTEXT

Context found in the OKF bundle at `E:\PROJEKTI\okf\example\knowledge\` and used above:

- `E:\PROJEKTI\okf\example\knowledge\index.md` — entry point; confirms the bundle contains one decision (auth), two constraints, one interview; nothing about export, CSV, or data formats, so no existing decision is touched or re-litigated by this task.
- `E:\PROJEKTI\okf\example\knowledge\constraints\solo-maintainer.md` — one person operates TaskLite a few hours per week; every design choice must minimize operational surface. This is the load-bearing constraint driving "synchronous, no async export infrastructure, CSV only."
- `E:\PROJEKTI\okf\example\knowledge\constraints\external-users.md` — users are individual freelancers, no corporate identity provider. Rules out enterprise-flavored asks (SharePoint/Drive integrations, admin-initiated org-wide exports) without needing to ask.
- `E:\PROJEKTI\okf\example\knowledge\interviews\2026-07-08-auth-scope.md` — owner's answers: near-zero maintenance budget ("anything that can break at 3am is out"), no formal compliance requirements, aversion to storing liability-creating data. Answers the "are there compliance requirements for exported data?" question I would otherwise have asked — there are none formal.
- `E:\PROJEKTI\okf\example\knowledge\decisions\magic-link-auth.md` and `E:\PROJEKTI\okf\example\specs\auth\spec.md` — accepted auth decision (status: accepted, evidence current as of 2026-07-08, i.e., today — not stale). Respected, not re-litigated: the export endpoint simply sits behind the existing magic-link session (AUTH-1/AUTH-2).
- `E:\PROJEKTI\okf\example\knowledge\log.md` — change history; confirms no prior export-related work.

## 3. QUESTIONS

Questions the wiki does not answer, which I would ask the human before writing the decision and spec:

1. **Scope of an export:** should it export all of the user's tasks, or respect the currently applied filter/view (e.g., only open tasks, only one project)? If both, which is the default?
2. **Columns:** which task fields belong in the CSV (title, status, due date, project/client, notes, created/completed timestamps, tags)? Anything to deliberately exclude?
3. **Is import a foreseeable follow-up?** If freelancers will later want CSV import (round-tripping), the column naming and format should be chosen now to be re-parseable; if export is one-way, we can optimize purely for spreadsheet readability.
4. **Any known target tool quirk to support?** Assume Excel + Google Sheets compatibility (UTF-8 BOM, comma delimiter) is enough — or do we know of users on locales where semicolon-delimited CSV is expected?

(Not asked, because the wiki already answers them: who the users are — external-users.md; maintenance/ops budget — solo-maintainer.md; compliance requirements — the 2026-07-08 interview: "nothing formal".)
