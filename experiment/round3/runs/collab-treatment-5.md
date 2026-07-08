# Real-time collaborative editing — evaluation

## 1. RECOMMENDATION

Do not build true real-time collaborative editing (live multi-cursor, OT/CRDT-based co-editing) at this time. Recommend a scoping conversation first, and steer toward a low-operational-surface alternative.

Reasoning:

- **It collides head-on with the solo-maintainer constraint.** TaskLite is built and operated by one person, a few hours per week, and the owner's own words in the auth interview were "anything that can break at 3am is out." Real-time collaboration is exactly the class of feature that breaks at 3am: it requires a persistent stateful layer (WebSockets or similar), presence tracking, conflict resolution (CRDT/OT), reconnection handling, and horizontal-scaling concerns. This is among the highest-operational-surface features a web app can take on. A managed service (e.g., a hosted sync backend) reduces but does not remove this surface, and adds cost and vendor dependency — a trade-off the knowledge base has no answer for yet.

- **"Clients" are a new, undecided user class.** The accepted constraint says users are individual freelancers; nothing in the knowledge base covers client accounts, permissions, or sharing. Before any collaboration feature, the project needs decisions on: do clients get accounts, what can they see/do, and how is a task shared. That groundwork is a prerequisite regardless of whether editing is "real-time."

- **Auth for clients is already decided and should be reused, not re-litigated.** The accepted magic-link decision (no passwords, no OAuth) applies cleanly to clients too — they are also external individuals with no corporate IdP. If clients get access, they log in via magic links. No new auth work or discussion needed.

- **Most of the PM's stated goal is achievable without real-time infrastructure.** "Freelancers working on tasks live together with their clients" is usually satisfied by a much cheaper ladder:
  1. **Shared task access + comments/activity feed** (plain request/response, no new infra).
  2. **Freshness without sockets**: short-interval polling or ETag-based refresh so both parties see recent changes within seconds.
  3. **Conflict safety**: optimistic locking with a "this task was updated by X — reload?" prompt, so concurrent edits never silently clobber each other.
  This delivers ~80% of the perceived value at ~10% of the operational cost, and each rung is independently shippable. True character-level co-editing should only be considered if user evidence shows the ladder is insufficient — and even then, only via a fully managed service with an explicit revisit of the solo-maintainer constraint.

Proposed next step: run a short scoping session with the PM/owner (questions below), then record the outcome as a new `knowledge/decisions/` entry (e.g., `client-collaboration.md`) with the rejected real-time option and its evidence, per the project's provenance convention.

## 2. PRIOR CONTEXT

Context found in the OKF bundle at `E:\PROJEKTI\okf\example\knowledge\` and used above:

- `E:\PROJEKTI\okf\example\knowledge\index.md` — entry point; TaskLite is a lightweight task tracker for freelancers, solo-maintained.
- `E:\PROJEKTI\okf\example\knowledge\constraints\solo-maintainer.md` — one person builds and operates TaskLite a few hours per week; every design choice must minimize operational surface. This is the binding constraint against real-time infrastructure.
- `E:\PROJEKTI\okf\example\knowledge\constraints\external-users.md` — users are individual freelancers, no corporate identity provider. Extends naturally to clients, so client access needs no SSO.
- `E:\PROJEKTI\okf\example\knowledge\decisions\magic-link-auth.md` — accepted 2026-07-08: magic-link auth, no passwords, no OAuth; rejected SSO and passwords. Evidence is dated today and remains plausible, so I respect it without re-litigating: client logins would also use magic links.
- `E:\PROJEKTI\okf\example\knowledge\interviews\2026-07-08-auth-scope.md` — Ivan: "I'm the only maintainer... Anything that can break at 3am is out" and "don't store passwords." Directly answers maintenance-capacity and auth questions, so I do not ask them again.
- `E:\PROJEKTI\okf\example\specs\auth\spec.md` — AUTH-1 (magic-link login) and AUTH-2 (30-day session expiry); any client-access feature must conform to these.
- `E:\PROJEKTI\okf\example\knowledge\log.md` — confirms all knowledge entries date from 2026-07-08 (today), i.e., evidence is fresh, no staleness delta-questions required.

No existing decision, constraint, or interview covers collaboration, sharing, or client accounts — that gap is what the questions below target.

## 3. QUESTIONS

Questions the wiki does not answer (auth approach and maintenance capacity are already answered by the wiki and are deliberately not asked):

1. What does "work live together" concretely mean to you and the users? Simultaneous character-by-character editing of the same field, or "we both see each other's changes within a few seconds and never overwrite each other"? Would presence indicators + fast refresh + conflict prompts satisfy the need?
2. Who are the "clients" as users: do they get their own TaskLite accounts, and what should they be able to do on a shared task — view only, comment, or edit fields? Should a freelancer be able to share individual tasks, whole projects, or both?
3. What is the evidence of demand — have users asked for this, and how many? Is there a specific workflow (e.g., scoping a task on a call together) we can validate with the cheapest rung first?
4. If, after shipping the cheaper ladder, true real-time co-editing still proves necessary: is there budget and appetite for a fully managed third-party sync service (recurring cost, vendor dependency, data flowing through a third party), given that self-hosting real-time infrastructure is ruled out by the solo-maintainer constraint?
