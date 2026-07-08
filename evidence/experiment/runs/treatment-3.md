# Treatment 3 — "Sign in with Google" (OAuth SSO) for TaskLite

## 1. RECOMMENDATION

Do not implement Google OAuth SSO at this time. This exact option was already evaluated and explicitly rejected in an accepted, current decision: `knowledge/decisions/magic-link-auth.md` (status: accepted, 2026-07-08 — decided today, so its evidence cannot be stale). TaskLite authenticates via emailed single-use magic links, and the decision's `## Rejected` section names "OAuth / 'Sign in with Google' SSO" specifically, for two reasons that both still hold:

1. Users are external freelancers with no corporate identity provider (`knowledge/constraints/external-users.md`), so SSO solves a problem TaskLite's users do not have.
2. The project is solo-maintained on a few hours per week (`knowledge/constraints/solo-maintainer.md`), and each OAuth provider adds Google Cloud console setup, credential/secret rotation, consent-screen review, and third-party breakage surface — ongoing operational load the owner explicitly said the project cannot absorb ("Anything that can break at 3am is out", `knowledge/interviews/2026-07-08-auth-scope.md`).

The current spec (`specs/auth/spec.md`, AUTH-1) also mandates magic-link login and traces to this decision, so adding Google SSO would contradict an accepted requirement, not just add a feature.

However, the decision records its own revisit trigger: "Revisit if a significant user segment demands social login." A PM request may be a signal that this trigger has fired — or it may just be a generic feature idea. The correct next step is therefore not to build, and not to flatly refuse, but to ask the PM the single delta question below. If the answer shows genuine, significant user demand, I would reopen the decision, capture the new evidence as an interview note, and evaluate the lowest-maintenance way to satisfy it (e.g., "Sign in with Google" as an *optional convenience* layered beside magic links via a managed auth service, keeping magic links as the fallback so the no-password constraint is preserved). Otherwise the decision stands and I would simply cite it back to the PM.

## 2. PRIOR CONTEXT

Found in the project's OKF knowledge bundle and specs, all read before forming this recommendation:

- `E:\PROJEKTI\okf\example\knowledge\index.md` — entry point; lists the auth decision, both constraints, and the interview.
- `E:\PROJEKTI\okf\example\knowledge\decisions\magic-link-auth.md` — accepted Decision (2026-07-08): magic-link auth; `## Rejected` explicitly includes OAuth/"Sign in with Google" SSO with rationale and a revisit condition ("significant user segment demands social login").
- `E:\PROJEKTI\okf\example\knowledge\constraints\external-users.md` — users are individual freelancers; no corporate IdP (Google Workspace, Entra, Okta) exists to integrate with.
- `E:\PROJEKTI\okf\example\knowledge\constraints\solo-maintainer.md` — one maintainer, a few hours/week; every choice must minimize operational surface.
- `E:\PROJEKTI\okf\example\knowledge\interviews\2026-07-08-auth-scope.md` — owner (Ivan) answers: no SSO need, near-zero maintenance budget, no passwords stored.
- `E:\PROJEKTI\okf\example\knowledge\log.md` — confirms all four artifacts were created 2026-07-08 (evidence is current as of today).
- `E:\PROJEKTI\okf\example\specs\auth\spec.md` — AUTH-1 mandates magic-link login (no passwords) and AUTH-2 sets 30-day session expiry; both trace to the magic-link decision.

Questions already answered by the wiki and therefore NOT asked: "Do users need SSO?" (no — no corporate IdP, per constraint/interview), "Can we store passwords?" (no), "How much auth maintenance is acceptable?" (near zero).

## 3. QUESTIONS

Only the delta question the decision itself invites — the wiki answers everything else:

1. The magic-link decision (2026-07-08) rejected Google SSO because users are individual freelancers with no corporate IdP and the solo maintainer can't absorb OAuth's operational overhead, with an explicit revisit trigger of "a significant user segment demands social login." What prompted this request — is there concrete evidence of user demand for Google sign-in (support requests, churn feedback, numbers), or has the maintenance capacity changed? Is the decision's evidence still true?
