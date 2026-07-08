# Real-time collaborative editing for TaskLite — evaluation

## 1. RECOMMENDATION

Do not commit to full real-time collaborative editing yet. Clarify the underlying problem first, then deliver collaboration value in stages, reserving true concurrent co-editing (CRDT/OT) as a last, demand-validated step.

Reasoning:

- **The project is at spec stage only.** TaskLite currently consists of a README and a single auth spec — there is no implementation, no data model, no sharing/permissions concept, and no collaboration spec. "Real-time collaborative editing" is among the most expensive features in software (conflict resolution, presence, WebSocket infrastructure, offline/reconnect handling, permission enforcement on every sync message). Building it before the basics exist would invert the dependency order.
- **A prerequisite is missing: client access.** Freelancers' clients are external parties. Before anyone can "work on tasks live together," clients need an identity and a permission model. Note this interacts directly with the existing auth spec (AUTH-1: magic-link login, no passwords; AUTH-2: 30-day sessions) — magic links actually extend naturally to inviting clients, but that has to be specified.
- **Most of the perceived value is likely cheaper than co-editing.** In task trackers, "working live together" usually means: seeing changes without refreshing, not overwriting each other, and discussing work in context. Those are solvable with (in order of cost): server-pushed live updates, optimistic-concurrency conflict detection, presence indicators/soft locks, and comments — none of which require CRDTs.

Proposed staged path (each stage independently shippable and validating demand for the next):

1. **Sharing & permissions** — invite a client to a project/task via magic link; define roles (view / comment / edit). Prerequisite for everything else.
2. **Live-updating views** — broadcast task changes over SSE or WebSocket so all viewers see current state within ~1s. Writes remain whole-field, last-write-wins with version checks (reject/merge on stale write, surface "X updated this task" instead of silently clobbering).
3. **Presence & soft locking** — show who is viewing/editing a task; warn or soft-lock when two people open the same field. This eliminates most real-world conflicts at a tiny fraction of CRDT cost.
4. **True concurrent text co-editing** — only if stages 1–3 show users actually editing the same text simultaneously (rather than just wanting freshness). Scope it to the task description/notes field only, using an off-the-shelf CRDT library (e.g., Yjs + y-websocket) rather than building sync from scratch.

Whatever is decided should be captured as a spec (e.g., `specs/collaboration/spec.md`) with the decision rationale recorded, consistent with the provenance convention the README describes, before implementation starts.

## 2. PRIOR CONTEXT

The project contains only two files; both were read and used:

- `E:\PROJEKTI\okf\example-control\README.md` — TaskLite is a fictional lightweight task tracker for freelancers, used to demonstrate the "Provenance Convention" (every requirement links to the decision that created it, every decision to the human answer justifying it). It refers to `knowledge/` and `specs/` directories.
- `E:\PROJEKTI\okf\example-control\specs\auth\spec.md` — the only spec: AUTH-1 (magic-link login, single-use, no passwords stored) and AUTH-2 (sessions expire after 30 days of inactivity). Relevant because client-facing collaboration requires extending this identity model to external clients.

Gaps found:

- The `knowledge/` directory referenced by the README **does not exist** in the repo, so no prior decisions or human answers were available to consult.
- There is no application code, no data model, and no existing spec covering tasks, sharing, permissions, or collaboration. This proposal would be the first feature decision beyond auth.

## 3. QUESTIONS

1. What specific problem prompted this request — clients seeing stale task state, edits overwriting each other, or clients wanting to discuss/annotate work? Do we have user evidence (support requests, interviews) pointing at one of these?
2. What does "editing together" mean concretely: simultaneous character-level editing of the same text field (Google-Docs style), or seeing each other's changes to task status/fields/comments in real time? Would stage 2–3 (live updates + presence + conflict warnings) satisfy the need?
3. How do clients get access — full accounts via the existing magic-link flow, or anonymous per-task/per-project share links? What can a client be allowed to do (view, comment, edit, create tasks)?
4. What is the expected concurrency — typically one freelancer plus one client on a task, or larger groups? (This heavily affects the sync architecture.)
5. Are there offline or flaky-network requirements (e.g., edits made offline must merge later), or is "online-only, live when connected" acceptable?
6. What is the appetite/timeline — is a staged rollout over several releases acceptable, or is this pitched as a single headline feature?
7. The README says every requirement should link to a decision in `knowledge/`, but that directory is missing. Does the decision history live elsewhere, and where should the record of this decision be written?
