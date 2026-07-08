# Treatment 4 — "Sign in with Google" (OAuth SSO) for TaskLite

## 1. RECOMMENDATION

Do not implement Google OAuth SSO at this time.

This exact option was evaluated and **explicitly rejected** in an accepted decision recorded today (2026-07-08): `knowledge/decisions/magic-link-auth.md` (`type: Decision`, `status: accepted`). TaskLite authenticates via emailed single-use magic links, and the decision's `## Rejected` section names "OAuth / 'Sign in with Google' SSO" specifically, for two evidenced reasons:

1. **Users have no corporate IdP** — TaskLite's users are individual external freelancers, not employees of organizations with Google Workspace/Entra/Okta (`knowledge/constraints/external-users.md`).
2. **Operational surface** — each OAuth provider adds credential rotation, Google Cloud console setup, and breakage surface that a solo maintainer working a few hours per week cannot absorb (`knowledge/constraints/solo-maintainer.md`; Ivan in the interview: "Anything that can break at 3am is out").

The decision's evidence is dated today, so it is not stale — the circumstances it rests on are current. Per project policy, an accepted decision with plausible evidence is respected, not re-litigated.

However, the decision itself defines a revisit trigger: *"Revisit if a significant user segment demands social login."* The PM's request may be a signal that this trigger has fired — but the request as stated provides no evidence of that. So the correct path is:

- **If the PM has evidence of user demand** (support requests, churn attributed to login friction, onboarding drop-off data): reopen the decision on that new evidence. If reopened and accepted, the scoped approach would be: Google as an *additional* login method alongside magic links (never replacing them — magic links remain the fallback and the passwordless guarantee holds, since "Sign in with Google" stores no passwords), using a well-maintained off-the-shelf library/hosted flow rather than hand-rolled OAuth, to keep the solo-maintainer operational cost as low as possible. This would also require updating `specs/auth/spec.md` (AUTH-1 currently mandates magic links as *the* authentication method) and recording a superseding decision with the new evidence.
- **If there is no such evidence**: the accepted decision stands, and no work should be done.

Recommended action now: ask the PM the delta question below before writing any code or specs.

## 2. PRIOR CONTEXT

Found and used, all under `E:\PROJEKTI\okf\example\`:

- `knowledge/index.md` — entry point; project is a lightweight task tracker for freelancers, solo-maintained; links to all items below.
- `knowledge/decisions/magic-link-auth.md` — **accepted decision (2026-07-08)**: magic-link auth; OAuth/"Sign in with Google" explicitly listed under `## Rejected`, with a revisit condition ("if a significant user segment demands social login"). This is the decision the PM's request directly touches.
- `knowledge/constraints/external-users.md` — users are individual freelancers; no corporate identity provider exists to integrate with.
- `knowledge/constraints/solo-maintainer.md` — one maintainer, a few hours/week; every choice must minimize operational surface.
- `knowledge/interviews/2026-07-08-auth-scope.md` — Ivan's answers grounding both constraints: no SSO need, near-zero maintenance budget, no passwords (liability).
- `specs/auth/spec.md` — AUTH-1 mandates magic-link login (no passwords stored); AUTH-2 mandates 30-day inactivity session expiry. Both cite the magic-link decision as their "why". Adding Google SSO would require amending AUTH-1.
- `knowledge/log.md` — confirms all auth provenance artifacts were created 2026-07-08 (evidence is current, not stale).

Questions already answered by the wiki (and therefore **not** asked): who the users are, whether they have a corporate IdP, the maintenance budget, and compliance/password requirements — all answered in the 2026-07-08 interview and constraints.

## 3. QUESTIONS

1. "OAuth/'Sign in with Google' was explicitly rejected in an accepted decision made today (2026-07-08), because users are external freelancers with no corporate IdP and the project is solo-maintained with a near-zero auth-maintenance budget. The decision says to revisit only if a significant user segment demands social login. Has that changed — do you have evidence of user demand for Google sign-in (support requests, onboarding drop-off, churn feedback) that should reopen this decision?"

2. (Only if the answer to Q1 is yes:) "Is Google SSO intended as an additional login option alongside magic links, or a replacement? The no-passwords constraint and the solo-maintainer constraint both favor 'additional, with magic links kept as the universal fallback' — is that acceptable?"
