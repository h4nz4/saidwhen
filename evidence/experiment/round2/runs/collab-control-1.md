# Evaluation: Real-time collaborative editing for TaskLite

## 1. RECOMMENDATION

Do not start building yet. Recommend a scoped discovery step first, and if the feature proceeds, start with the smallest useful slice rather than full live co-editing.

Reasoning:

- **The project is at a very early stage.** TaskLite currently consists of a README and a single spec (authentication, 2 requirements). There is no task model, no data-layer spec, no UI spec, and no code. "Real-time collaborative editing" presupposes a task-editing feature that is not yet specified anywhere. Sequencing matters: the core single-user task CRUD experience must be specified (and presumably built) before a collaborative layer on top of it can be designed.
- **Real-time co-editing is one of the most expensive features to build and operate.** It implies presence, conflict resolution (OT/CRDT or last-write-wins with locking), WebSocket or similar persistent-connection infrastructure, and a permission model for non-owner participants ("clients") — none of which exists today.
- **The stated user need may be satisfiable far more cheaply.** "Freelancers working on tasks live together with their clients" often reduces to: shared visibility of a task list, comments, and near-real-time updates. Options in ascending cost:
  1. Client read-only share links + polling/refresh (days of work).
  2. Comments + live-updating task status via server-sent events (small weeks).
  3. Field-level "someone else is editing" locking with auto-refresh (moderate).
  4. True character-level co-editing of task descriptions, CRDT-based (large, ongoing operational cost).
  My recommendation is to validate whether option 1 or 2 solves the client-collaboration need before committing to 3 or 4.
- **The client-access question interacts with the existing auth spec.** AUTH-1 mandates magic-link login with no passwords, and AUTH-2 sets a 30-day session lifetime. Clients are a new user class: do they get full magic-link accounts, or lighter-weight guest/share-token access? A 30-day session for an external client on a shared device may also be too long. Any collaboration feature will need either an extension of the auth spec or an explicit guest-access requirement, recorded as a new decision.

Proposed path forward:

1. Answer the discovery questions below with the PM.
2. Write a `specs/collaboration/spec.md` (and any auth spec deltas) capturing the agreed scope, linking requirements to the decisions and human answers per the project's Provenance Convention.
3. Implement the smallest slice that delivers client visibility; measure usage before investing in live co-editing.

## 2. PRIOR CONTEXT

The project is nearly empty; I found and used the following:

- `E:\PROJEKTI\okf\example-control\README.md` — describes TaskLite as a lightweight task tracker for freelancers and states the Provenance Convention: every requirement links to the decision that created it, and every decision links to the human answer that justified it. It also references `knowledge/` and `specs/` directories.
- `E:\PROJEKTI\okf\example-control\specs\auth\spec.md` — the only spec. AUTH-1: magic-link login, no passwords stored. AUTH-2: sessions expire after 30 days of inactivity. Relevant because client collaborators are a new user class whose access model must be reconciled with this spec.
- **Gap:** the `knowledge/` directory referenced by the README does not exist in the repo, so there are no recorded decisions or human answers to consult. No prior decisions about collaboration, sharing, client access, or real-time infrastructure exist. Any provenance chain for this feature would start from scratch — which strengthens the case for asking the questions below and recording the answers before writing requirements.

## 3. QUESTIONS

1. What specific problem have freelancers/clients reported? Is the pain "my client can't see task status without me emailing them," or genuinely "two people need to type in the same task at the same time"? Can you share the underlying request(s)?
2. What is the minimum that would count as success — shared read-only visibility, commenting, live status updates, or true simultaneous editing of task text?
3. What do clients need to be able to do: view only, comment, edit task fields, create tasks? And should their access be scoped to specific tasks/projects or the freelancer's whole workspace?
4. How should clients authenticate? Full magic-link accounts under the existing AUTH-1 flow, or lightweight share links/guest tokens? Does the 30-day session lifetime (AUTH-2) apply to clients too?
5. What scale should we design for (typical concurrent editors per task — is it ever more than 2)? This determines whether we need CRDT-grade conflict resolution or simple locking/last-write-wins.
6. Are there budget/timeline constraints or an appetite ceiling for this? Persistent-connection infrastructure has ongoing operational cost that may not fit a "lightweight" product positioning.
7. Where is the `knowledge/` directory the README promises? Should I create it as part of recording the decisions for this feature, or does it live elsewhere?
