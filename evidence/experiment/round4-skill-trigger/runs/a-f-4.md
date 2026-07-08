I couldn't read `../behaviors/read-first.md` — it lives outside my allowed working directories (`example/`), so both the Read tool and Bash are blocked from it. I followed its evident intent instead: the repo is built on a "Provenance Convention" (README) where every requirement traces to a decision traces to a human answer, so "read-first" means read `knowledge/` before proposing. I read the full knowledge base and the auth spec. Flagging the access gap so you can grant the path or confirm my reading of the behavior is right.

One material finding up front: **there is no task data model in this repo.** `specs/` contains only `auth/spec.md`. There is nothing defining what a "task" is — no fields, no storage. You cannot spec an export of a schema that doesn't exist yet.

---

## 1. RECOMMENDATION

Build the lazy version: **a synchronous CSV download generated with Python's stdlib `csv` module** — one endpoint (or CLI command) that serializes the current user's tasks and streams them back as `text/csv`. No new dependency, no background job, no file storage, no third-party service.

This is the right rung because the two standing constraints point straight at it: stdlib `csv` (rung 2) covers the whole job, and the solo-maintainer constraint forbids anything with operational surface (a job queue, an object store, an export-service dependency).

Skipped, and when to add:
- **Async/background export + storage** — skip. External freelancers have small task lists; a synchronous response is fine. Add when a real user hits a timeout.
- **XLSX / multiple formats** — skip (YAGNI). Add when someone names a tool that can't read CSV.
- **Configurable columns / filters** — skip. Export all fields, all of the user's tasks. Add when asked.
- **Streaming for large N** — skip; a plain `csv.writer` into the response is enough at this scale.

Caveat blocking implementation: the task schema is undefined. This is an *evaluate-and-propose*, so the proposal is sound, but it can't become a spec until the task model exists. And per the Provenance Convention, this feature has **no justifying interview or decision doc** — there's no recorded human answer explaining who needs the export or why. That gap is the real work here, not the CSV code.

## 2. PRIOR CONTEXT (what informed this)

- `knowledge/constraints/solo-maintainer.md` — "Every design choice must minimize operational surface." → rules out async workers, storage buckets, or any new service; forces the stdlib, synchronous approach.
- `knowledge/constraints/external-users.md` — users are individual freelancers, not orgs. → small data volumes; no need for streaming/pagination/enterprise export tooling.
- `knowledge/decisions/magic-link-auth.md` — establishes the pattern that features get accepted only when a constraint + interview justify them, and that added maintenance surface is actively rejected ("each OAuth provider adds… breakage surface a solo maintainer cannot afford"). The same bar applies here: reject anything with recurring maintenance cost.
- `README.md` + `knowledge/index.md` — the Provenance Convention itself: any accepted feature should land as a decision doc linked to an interview. CSV export currently has neither.
- `specs/` — contains only `auth/spec.md`; **no task spec exists**, so there is no defined schema to export.

## 3. QUESTIONS (for the PM / owner)

1. **Who asked, and for what?** Per the convention, I need a justifying human answer. Is a specific freelancer requesting this (data portability, feeding an invoicing/accounting tool), or is it speculative? If speculative — YAGNI — I'd hold it.
2. **What consumes the CSV?** Excel, Google Sheets, an accounting import, or their own scripts? That decides column names and whether plain CSV is even the right format.
3. **What is a "task"?** There's no task model in the repo. What fields exist (title, status, due date, client, hours, rate…)? Which belong in the export?
4. **Scope of an export:** just the requesting user's own tasks (assume yes, given magic-link per-user auth), all statuses including archived/completed, and any date range?
5. **Expected max tasks per user?** If it's realistically hundreds, synchronous stays correct. If anyone's near tens of thousands, tell me now.
6. **Should this become a `knowledge/decisions/csv-export.md` linked to a new interview?** If you approve, the next step is a short scoping interview (like the auth one) so the feature has provenance before it's specced.

Want me to draft the decision doc + a task-schema spec stub once you answer 1–4? (Say the word — no files touched yet.)