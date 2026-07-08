# CSV export — evaluation (TaskLite)

## 1. RECOMMENDATION

Proceed — CSV export is a good fit for TaskLite, but keep it deliberately minimal.

Proposed shape, derived from the project's recorded constraints:

- **Synchronous, on-demand download.** A single authenticated endpoint (e.g. `GET /tasks/export.csv`) that streams the current user's tasks as CSV in the request/response cycle. No background job queue, no scheduled exports, no emailed files, no export-history storage. Rationale: TaskLite is solo-maintained a few hours per week and every design choice must minimize operational surface (`knowledge/constraints/solo-maintainer.md`) — async export pipelines are exactly the kind of "can break at 3am" machinery the owner ruled out.
- **Per-user scope only.** Users are individual external freelancers, not organizations (`knowledge/constraints/external-users.md`), so there is no need for team/workspace/admin bulk export. Export = "my tasks."
- **Excel-friendly output.** UTF-8 with BOM, comma-delimited, RFC 4180 quoting, ISO 8601 dates — freelancers will overwhelmingly open this in Excel/Google Sheets, and this combination avoids the classic mojibake/date-mangling complaints with zero ongoing maintenance.
- **Reuse existing auth.** The endpoint sits behind the existing magic-link session (AUTH-1/AUTH-2 in `specs/auth/spec.md`); no new auth surface, no signed public download links (those add token lifecycle to maintain).
- **Explicitly reject (record in the Decision's `## Rejected` section):** scheduled/emailed exports, XLSX generation (library dependency + formatting surface for marginal gain over CSV), a generic multi-format export framework, and third-party integrations (Zapier etc.) — all violate the solo-maintainer constraint; revisit only on demonstrated user demand.

Process: this is a new capability with no existing Decision, so per the provenance convention the crystallized outcome should be captured as `knowledge/decisions/csv-export.md` (with evidence links and the Rejected section), the human's answers as `knowledge/interviews/<date>-csv-export.md`, a new `specs/export/spec.md` with `([why](...))` links, plus a `log.md` line and an `index.md` entry. I have not written any of these because (a) this task is read-only and (b) the decision has not crystallized yet — three scoping questions below are genuinely unanswered by the wiki.

## 2. PRIOR CONTEXT

Found and used, all under `E:\PROJEKTI\okf\example\`:

- `knowledge/index.md` — entry point; confirms TaskLite is a lightweight task tracker for freelancers, solo-maintained, and lists all decisions/constraints/interviews (none about export — this is a genuinely new decision area).
- `knowledge/constraints/solo-maintainer.md` — one person, a few hours per week; every design choice must minimize operational surface. Drives the "synchronous, no pipeline, no new dependencies" recommendation.
- `knowledge/constraints/external-users.md` — users are individual freelancers with no corporate IdP. Drives "per-user export only, no team/admin export."
- `knowledge/interviews/2026-07-08-auth-scope.md` — owner's own words: "Anything that can break at 3am is out"; no formal compliance requirements. Pre-answers questions I would otherwise ask about compliance-driven export formats and about maintenance appetite — I am not asking those.
- `knowledge/decisions/magic-link-auth.md` (status: accepted, 2026-07-08, evidence current) — respected, not re-litigated: the export endpoint reuses the existing magic-link session rather than introducing any new auth mechanism (e.g. API keys for export tooling).
- `specs/auth/spec.md` — AUTH-1 (magic-link login) and AUTH-2 (30-day session expiry) constrain how the download endpoint is protected.
- `knowledge/log.md` — change history; confirms no prior export-related work.

Note: the example project contains only `knowledge/` and `specs/` (no application source code), so "how to proceed" is necessarily spec-and-decision-first rather than pointing at code touchpoints.

## 3. QUESTIONS

The wiki answers who the users are, the maintenance budget, and the compliance posture, so I am not asking about those. What it does not answer:

1. **Column set and task scope:** Which task fields should the CSV include (e.g. title, status, due date, project/client, notes, created/completed timestamps)? And should the export cover all of a user's tasks including completed/archived ones, or respect the currently applied filter/view in the UI?
2. **Trigger point:** Is a simple "Export CSV" button on the task list (direct browser download) sufficient, or do you envision anything beyond that (e.g. choosing a date range before download)?
3. **Scale sanity check:** Roughly how many tasks can a heavy user accumulate (hundreds? tens of thousands?)? This only matters for deciding whether plain in-memory generation is fine or the response should be streamed — either way it stays a synchronous endpoint.
