**Note before the sections:** I could not read `../behaviors/read-first.md`. It sits outside this session's allowed working directories (`E:\PROJEKTI\saidwhen\example`), so both the Read tool (permission denied) and the Bash tool (blocked) refused it. I did not fabricate its contents. Instead I applied what the README states the repo is *about* — the Provenance Convention: ground every proposal in the recorded human decisions under `knowledge/`, and surface unknowns as questions rather than inventing answers. Everything below is sourced from files I could actually read. If read-first.md imposes a specific format or step I've missed, grant access to that path and I'll redo this.

---

## 1. RECOMMENDATION

Build it, and build it small. CSV export of tasks is a good fit for TaskLite and carries no provenance conflict.

- Use the Python stdlib `csv` module — no new dependency, no new infrastructure. This is the operationally-cheapest option, which is the governing constraint for this project (`solo-maintainer`).
- One read-only export path (a download endpoint or a CLI command) that sits **behind the existing magic-link session** and returns **only the authenticated user's own tasks**. Per-user scoping is not optional here — TaskLite's users are unrelated external freelancers (`external-users`), so a cross-user export would be a data leak.
- Write UTF-8 with a BOM so Excel opens it cleanly; quote fields via `csv.writer` (never hand-roll comma joining — it breaks on task titles containing commas, quotes, or newlines).

Skipped deliberately: streaming/pagination, background jobs, format options (XLSX/JSON), column config. Add when a user actually has enough tasks that a synchronous response is too large — not before (YAGNI, and it keeps the 3am-breakage surface at zero, per `solo-maintainer`).

Caveat: the task data model isn't in the knowledge base, so the exact columns are an open question (see §3), not something I should guess.

## 2. PRIOR CONTEXT (what informed this)

- `knowledge/constraints/solo-maintainer.md` — "every design choice must minimize operational surface," a few hours/week. → stdlib `csv`, no new deps, no new service, synchronous. This is the strongest driver of the "build it small" recommendation.
- `knowledge/constraints/external-users.md` — users are individual freelancers with no shared org / IdP. → export must be scoped to the requesting user; there is no tenant/org boundary to lean on, so isolation is per-user.
- `knowledge/decisions/magic-link-auth.md` + `specs/auth/spec.md` (AUTH-1, AUTH-2) — auth is magic-link sessions, 30-day expiry, no passwords. → the export endpoint reuses that existing session auth; it introduces no new credential or access path.
- `knowledge/interviews/2026-07-08-auth-scope.md` — owner: "nothing formal" on compliance, and "anything that can break at 3am is out." → no formal export-compliance bar to clear, and it reinforces the low-maintenance bias.
- `knowledge/index.md` / `log.md` — confirm the knowledge base currently covers **only auth**. There is no recorded decision, constraint, or spec about the task data model, storage, or exports. That absence is why §3 exists rather than a fuller spec.

## 3. QUESTIONS (for the PM / owner)

1. **Columns?** What fields make up a task, and which should the CSV include (id, title, status, due date, created/updated, notes)? The task data model isn't in `knowledge/`, so I won't guess it.
2. **Scope — confirm per-user.** Should export return only the authenticated user's own tasks? Given `external-users`, I'm assuming yes; I want that confirmed and recorded, since it's the security-critical decision.
3. **Delivery shape.** Download endpoint in the app, a CLI/admin command, or an emailed file? (Affects nothing about the CSV itself, everything about surface area.)
4. **Excel vs. plain CSV.** Do you need it to open cleanly in Excel (UTF-8 BOM, `,` delimiter, a specific date format), or is a plain RFC-4180 UTF-8 file fine?
5. **Any sensitivity to exporting task contents?** The auth interview said "nothing formal," but that was about auth. Is a full plaintext dump of task titles/notes acceptable, or is any field considered sensitive?
6. **Provenance step:** if this ships, should it get a `decisions/csv-export.md` entry (and the question answers logged as an interview) to keep the convention intact? I'd recommend yes.