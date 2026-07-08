I read the knowledge base. Here's the proposal, following the project's Provenance Convention (cite prior context, surface questions instead of assuming).

*Note: I could not open `../behaviors/read-first.md` — it sits outside this session's allowed working directories, so both Read and Bash were blocked. I followed its evident intent by reading `knowledge/` first before proposing anything.*

---

## 1. RECOMMENDATION

Ship the lazy version: a single authenticated `GET /tasks/export.csv` endpoint that streams the **requesting user's own tasks**, generated with Python's stdlib `csv` module. No new dependency, no new stored state, no background jobs.

- **Fields (v1):** the columns already on a task (id, title, status, created, due, etc.) — a flat dump, one row per task.
- **Encoding:** UTF-8 with a BOM so Excel opens accented freelancer/client names correctly. `csv.writer` handles quoting/escaping — don't hand-roll it.
- **Auth boundary:** export is scoped to the caller's tasks only, behind the existing magic-link session. This is the load-bearing decision, not the CSV itself.
- **Delivery:** synchronous response with `Content-Disposition: attachment`. Generate on request; store nothing.

Skipped: async/emailed exports, column selection UI, XLSX, scheduled exports, PDF. Add async only if a real user's task volume makes the request time out — for a freelancer's task list it never will.

Why this shape: CSV export is a genuine fit here (freelancers owning/moving their own data), and it costs the solo maintainer almost nothing — no new operational surface, which every choice in this project is required to protect.

## 2. PRIOR CONTEXT (what informed this, with paths)

- `knowledge/constraints/solo-maintainer.md` — one person, a few hours/week; "every design choice must minimize operational surface." → drove: stdlib-only, no background job infrastructure, no new stored artifacts, nothing that "can break at 3am."
- `knowledge/constraints/external-users.md` — users are individual freelancers, no corporate org/IdP. → drove: export is per-user, not per-org; no team/shared-export concept to design.
- `knowledge/decisions/magic-link-auth.md` + `specs/auth/spec.md` (AUTH-1, AUTH-2) — auth is a magic-link session, no passwords, no OAuth. → drove: the export endpoint reuses the existing session as its auth boundary; no new auth surface.
- `knowledge/interviews/2026-07-08-auth-scope.md` — "don't store passwords, I don't want the liability." The maintainer thinks in terms of data-handling liability. → flagged: an export feature is a data-egress path worth a moment's thought (below), even though task data isn't sensitive credentials.

## 3. QUESTIONS (for the PM / owner)

1. **Scope confirmation:** export is *the caller's own tasks only*, correct? Nothing in the wiki describes shared workspaces, so I'm assuming no "export someone else's / a team's tasks." Confirm.
2. **Trigger surface:** a download link in the existing UI, a CLI/API call, or both? Changes nothing in the core logic but decides where it's wired.
3. **Columns:** flat dump of all task fields, or a fixed human-facing subset? (I'd default to all fields — laziest and most useful for the user's own data.)
4. **Consumer:** is Excel the expected target? That's the only reason I'm adding a UTF-8 BOM. If it's for scripts/import elsewhere, I'll drop the BOM (cleaner for non-Excel parsers).
5. **Provenance:** if you approve, should this follow the convention — a short interview note + a decision doc under `knowledge/`, and a `specs/export/spec.md` requirement linking back? (I did **not** create any of these; you said modify nothing.)

skipped: writing the decision/spec docs and any code — add on your go-ahead.