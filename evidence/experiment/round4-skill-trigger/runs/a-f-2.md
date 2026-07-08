Read the wiki first (the "read-first" behavior — TaskLite's Provenance Convention: consult the decision wiki before acting). Here's the proposal. No files touched.

## 1. RECOMMENDATION

Ship the lazy version: one synchronous endpoint (`GET /tasks/export.csv`) that writes the **authenticated user's own** tasks with Python's stdlib `csv` module and returns `text/content-type: text/csv`. No new dependency, no background job, no new storage, no stored files.

```python
# ponytail: stdlib csv, synchronous. Add streaming/async only if a user's task
# count grows past what a request can serialize in-memory (not a freelancer's list).
import csv, io
def export_tasks_csv(user):
    buf = io.StringIO()
    w = csv.writer(buf)
    w.writerow(["id", "title", "status", "due", "created"])
    for t in tasks_for(user):              # scoped to the session user — never all tasks
        w.writerow([t.id, t.title, t.status, t.due, t.created])
    return buf.getvalue()                  # Content-Type: text/csv; charset=utf-8
```

Why this shape and not more: every TaskLite constraint pushes the same way — the [solo-maintainer](knowledge/constraints/solo-maintainer.md) rule kills anything with a queue, a worker, or a stored artifact to clean up; `csv` is stdlib so there's nothing to rotate or patch. Scoping to the session user isn't optional — it's the one place laziness would become a data-leak bug, so it's the one thing I won't cut.

→ skipped: async job, S3-style stored exports, XLSX, column config. Add async **when** a single user's export can't serialize in one request; add the rest only on a concrete ask.

## 2. PRIOR CONTEXT (what informed this, with paths)

- **`knowledge/constraints/solo-maintainer.md`** — "every design choice must minimize operational surface," a few hours/week, "anything that can break at 3am is out." → rules out background workers, export storage, new deps. Drives the synchronous stdlib design.
- **`knowledge/decisions/magic-link-auth.md`** — the project's established pattern is to reject anything with ongoing maintenance overhead (OAuth, passwords) in favor of the near-zero-maintenance option. CSV-via-stdlib is the same reflex; this proposal is consistent with that precedent.
- **`knowledge/constraints/external-users.md`** + **`specs/auth/spec.md` (AUTH-1)** — users are external freelancers authenticated by magic link, each seeing only their own data. → the export **must** be scoped to the session user, not a global dump. This is the security boundary the design is built around.
- **`README.md` / `knowledge/index.md`** — the Provenance Convention: this proposal should itself land as a decision node linking back to these constraints once accepted.

## 3. QUESTIONS (for the PM/owner)

1. **Scope confirm** — export is one user's own tasks only, triggered from their session? (Assuming yes per AUTH-1; a cross-user/admin export would be a different, bigger decision.)
2. **Columns** — is `id, title, status, due, created` enough, or do you need notes/tags/priority? Which fields matter for whatever the freelancer does with the CSV downstream (invoicing? time reports?).
3. **Filter or all** — export everything, or respect the current view (e.g. only open tasks, a date range)?
4. **Trigger** — a download button in the UI, an API endpoint, or both?
5. **Privacy** — any free-text task titles that shouldn't leave the app, or is a raw dump fine given it's the user's own data?
6. **Provenance** — want me to draft the decision + interview nodes under `knowledge/` when this is approved, per the convention?

Answer 1–3 and the endpoint is a few lines. Everything else is default-able.