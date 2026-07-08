# RECOMMENDATION

Do not implement "Sign in with Google" now. This exact option was evaluated and **explicitly rejected** in an accepted decision made today (2026-07-08): `knowledge/decisions/magic-link-auth.md` chose emailed single-use magic links and lists "OAuth / 'Sign in with Google' SSO" in its Rejected section, for two evidence-backed reasons:

1. **Users have no corporate IdP** — TaskLite's users are individual external freelancers, not employees of an organization (`knowledge/constraints/external-users.md`).
2. **Solo-maintainer operational budget** — each OAuth provider adds Google Cloud console setup, credential rotation, and breakage surface that a one-person, few-hours-a-week operation cannot absorb (`knowledge/constraints/solo-maintainer.md`; Ivan: "Anything that can break at 3am is out").

The decision's evidence is dated today, so it is current, not stale — there is no basis to silently override it. However, the decision itself names its own revisit trigger: *"Revisit if a significant user segment demands social login."* The PM's request may be a signal that this trigger has fired, so the correct next step is not to build, and not to flatly refuse, but to ask the single delta question below.

If the revisit trigger has genuinely fired (real, quantified user demand for Google sign-in), the proposed path would be:
- Add Google OAuth as a **secondary** login method alongside magic links (not a replacement — magic links remain the fallback and keep the no-password guarantee from AUTH-1 in `specs/auth/spec.md`).
- Account linking by verified email, so an existing magic-link user who signs in with Google lands in the same account.
- Scope to Google only (no generic multi-provider SSO framework), keeping the solo-maintainer surface minimal.
- Update the decision record: supersede or amend `knowledge/decisions/magic-link-auth.md`, record the new interview answers in `knowledge/interviews/`, update `specs/auth/spec.md`, and append to `knowledge/log.md`.

If the trigger has not fired (the request is speculative "nice to have"), recommend keeping the accepted decision as-is and recording the PM inquiry in the log for future reference.

# PRIOR CONTEXT

- `E:\PROJEKTI\okf\example\knowledge\index.md` — entry point; TaskLite is a lightweight task tracker for freelancers, solo-maintained.
- `E:\PROJEKTI\okf\example\knowledge\decisions\magic-link-auth.md` — accepted 2026-07-08; magic-link auth chosen; OAuth/Google SSO and passwords explicitly rejected; includes the revisit condition ("significant user segment demands social login").
- `E:\PROJEKTI\okf\example\knowledge\constraints\external-users.md` — users are individual freelancers; no corporate identity provider (Google Workspace, Entra, Okta) to integrate with.
- `E:\PROJEKTI\okf\example\knowledge\constraints\solo-maintainer.md` — one person operates TaskLite a few hours per week; every choice must minimize operational surface.
- `E:\PROJEKTI\okf\example\knowledge\interviews\2026-07-08-auth-scope.md` — Ivan's answers: no SSO need, near-zero maintenance budget, no passwords (liability).
- `E:\PROJEKTI\okf\example\specs\auth\spec.md` — AUTH-1 (magic-link login MUST, no passwords stored) and AUTH-2 (30-day session expiry), both linked to the magic-link decision.
- `E:\PROJEKTI\okf\example\knowledge\log.md` — confirms all auth artifacts were created 2026-07-08.

Questions already answered by the wiki, and therefore **not** asked: who the users are and whether they need corporate SSO (no — external-users.md), how much auth maintenance is acceptable (near zero — solo-maintainer.md), and whether there are compliance requirements (none formal; no password storage — the interview).

# QUESTIONS

1. (Delta question) OAuth/Google SSO was rejected today, 2026-07-08, because users are external freelancers with no corporate IdP and the project is solo-maintained with a near-zero auth-maintenance budget. The decision says to revisit only if a significant user segment demands social login. Has that changed — i.e., is this request backed by concrete user demand for Google sign-in (how many users / what share), or has the user base or maintenance capacity changed since the decision?
2. If the demand is real: should Google sign-in be added as a secondary method alongside magic links (preserving the no-password rule in AUTH-1), or is a change to the primary auth model intended?
