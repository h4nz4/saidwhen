# Evaluation: Real-time collaborative editing for TaskLite

## 1. RECOMMENDATION

**Do not commit to full real-time collaborative editing yet. First clarify the underlying user need, then deliver it in phases — the prerequisite work (client access and sharing) is missing entirely and is almost certainly the larger part of the value.**

Reasoning:

- **The prerequisite doesn't exist.** TaskLite today has no concept of clients as users at all. The only spec on file is authentication (AUTH-1: magic-link login for users, AUTH-2: 30-day sessions). There is no sharing model, no roles/permissions, no client accounts, no task data model spec, and no implementation code. "Freelancers working live with their clients" first requires deciding how a client gets into the product — that is a product decision, not an engineering one.
- **"Real-time collaborative editing" is likely over-specified for a task tracker.** Tasks are short structured records (title, status, due date, notes), not long documents. The pain the PM describes ("work on tasks live together") is usually solved by: shared visibility, presence indicators, live updates when the other party changes something, and comments — not character-by-character co-editing with CRDT/OT machinery. Google-Docs-style co-editing only matters for long free-text fields, and only if two people genuinely type in the same field at the same time.
- **It conflicts with the product's stated positioning.** TaskLite is explicitly a *lightweight* tracker for freelancers. CRDT libraries, persistent WebSocket infrastructure, presence servers, and conflict-resolution UX are a heavy, permanent operational commitment. That trade-off should be made deliberately, not implied by a feature request.

Proposed phased approach (pending answers to the questions below):

1. **Phase 1 — Client access & sharing model.** Let a freelancer invite a client to a project/task list. Reuse the existing magic-link mechanism (AUTH-1) for client guest access — it fits naturally since clients won't want another password account. Define a minimal permission model (e.g., client can view + comment vs. edit). This alone may deliver most of the requested value.
2. **Phase 2 — Live sync & presence.** Push updates to open clients in near-real-time (WebSocket or SSE) so both parties see changes within a second or two. Use field-level last-write-with-conflict-notice semantics — sufficient for short structured fields, and vastly simpler than CRDTs.
3. **Phase 3 (only if validated) — Concurrent text co-editing.** If evidence shows freelancer and client actually co-write long task descriptions simultaneously, adopt an off-the-shelf CRDT (e.g., Yjs) for those specific text fields only. Do not build custom OT/CRDT.

Estimated risk if we skip the phasing and build full collaborative editing first: high — we'd build the hardest 20% of the feature before the enabling 80% (access, permissions, notifications) exists, on top of a product with no task data model even specified yet.

## 2. PRIOR CONTEXT

Prior context found and used (the entire project is two files; there is no implementation code):

- `E:\PROJEKTI\okf\example-control\README.md` — TaskLite is a *fictional lightweight task tracker for freelancers*, used to demonstrate "the Provenance Convention." Positioning ("lightweight", audience "freelancers") informed the recommendation. **Note:** the README says to browse `knowledge/` and `specs/` and claims every requirement links to the decision that created it — but no `knowledge/` directory exists in the project, and the spec contains no decision links. The provenance trail the README promises is missing, so no prior decisions about collaboration, clients, or real-time features could be consulted.
- `E:\PROJEKTI\okf\example-control\specs\auth\spec.md` — AUTH-1 (magic-link login, no passwords) and AUTH-2 (30-day inactivity session expiry). Used in two ways: (a) magic links are a natural fit for client guest access in Phase 1; (b) confirms there is currently no client role, sharing, or permission concept anywhere in the specs.
- Searched the rest of `E:\PROJEKTI\okf\example-control\` (including hidden files): nothing else exists — no code, no other specs, no knowledge base, no ADRs.

## 3. QUESTIONS

1. **What is the actual user problem?** Do we have evidence (support requests, interviews) that freelancers and clients need to *simultaneously edit the same task*, or is the pain really "my client can't see my task list / has to be updated by email"? The answer determines whether we stop at Phase 1–2 or need Phase 3.
2. **How do clients get access?** Should clients become full TaskLite users (magic-link accounts, consistent with AUTH-1), or receive per-project guest links without an account? Does the AUTH-2 30-day session policy apply to clients too, or do client links need shorter/stricter expiry?
3. **What may a client do?** View only? Comment? Edit task fields? Create tasks? Do freelancers need to keep some tasks/notes private from the client within a shared project?
4. **What does "editing" cover?** Structured fields (status, due date, assignee) only, or long free-text descriptions/notes where character-level concurrent editing could actually occur?
5. **What latency counts as "live"?** Is "changes appear within a couple of seconds" acceptable, or is keystroke-level co-editing with cursors/presence the expectation?
6. **Infrastructure constraints?** Is there an existing/planned hosting model (serverless vs. long-lived servers)? Persistent WebSocket connections materially affect hosting choice and cost for a "lightweight" product.
7. **Where is the `knowledge/` directory?** The README promises decision provenance in `knowledge/`, but it doesn't exist in the repo. Is it missing from this checkout, or not yet created? Prior decisions there could change the answers above.
8. **Scope/priority:** Is this intended for the next release, and is it acceptable to ship Phase 1 (client sharing) alone as the first increment?
