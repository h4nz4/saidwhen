# RECOMMENDATION

Do not implement "Sign in with Google" at this time.

This exact option was already evaluated and explicitly rejected in an accepted decision made today (2026-07-08): `knowledge/decisions/magic-link-auth.md` (`type: Decision`, `status: accepted`). TaskLite authenticates via emailed single-use magic links, and its `## Rejected` section names **OAuth / "Sign in with Google" SSO** specifically, for two evidence-backed reasons:

1. Users are external freelancers with no corporate identity provider (`knowledge/constraints/external-users.md`).
2. The project is solo-maintained on a few hours per week; each OAuth provider adds Google Cloud console setup, credential/secret rotation, and breakage surface the maintainer cannot absorb (`knowledge/constraints/solo-maintainer.md`). The owner stated in the scoping interview: "Anything that can break at 3am is out."

The decision's evidence is dated today and there is no indication circumstances have changed, so per project convention I respect it rather than re-litigate it. The decision itself defines the only documented reopening condition: "Revisit if a significant user segment demands social login."

Proposed path forward:

- **Default: decline the request**, citing `knowledge/decisions/magic-link-auth.md`, unless the PM can point to new evidence that satisfies the revisit clause (e.g., measurable user demand for social login, sign-up funnel drop-off attributable to magic-link friction).
- **If such evidence exists**, the correct process is to reopen the decision — not to quietly ship OAuth: hold a short scoping session with the owner (Ivan), record answers in `knowledge/interviews/<date>-oauth-revisit.md`, and either supersede or reaffirm the magic-link decision, updating `specs/auth/spec.md` (AUTH-1 currently mandates magic links with no passwords stored) accordingly.
- **If it were ever approved**, the implementation should honor the standing constraints: OAuth as an *additional* login method alongside magic links (not a replacement), one provider only (Google), no password storage, and minimal operational surface — but this is contingent on the decision being formally revisited first.

# PRIOR CONTEXT

Prior context found and used, all under `E:\PROJEKTI\okf\example\`:

- `knowledge/index.md` — entry point; lists the auth decision, constraints, and interview.
- `knowledge/decisions/magic-link-auth.md` — accepted 2026-07-08; chooses magic-link auth and explicitly rejects OAuth/"Sign in with Google" SSO and passwords, with a revisit condition ("significant user segment demands social login").
- `knowledge/constraints/external-users.md` — users are individual freelancers; no corporate IdP (Google Workspace, Entra, Okta) to integrate with.
- `knowledge/constraints/solo-maintainer.md` — one person, a few hours/week; every design choice must minimize operational surface.
- `knowledge/interviews/2026-07-08-auth-scope.md` — owner's answers: no SSO need, near-zero maintenance budget, no passwords (liability).
- `specs/auth/spec.md` — AUTH-1 (magic-link login MUST, no passwords) and AUTH-2 (30-day session expiry), both linked to the magic-link decision.
- `knowledge/log.md` — confirms all of the above were created 2026-07-08 (evidence is current, not stale).

The wiki already answers the baseline questions I would otherwise ask (who the users are, maintenance budget, compliance posture), so I am not re-asking those.

# QUESTIONS

Only the delta question is warranted — the wiki answers everything else:

1. "Adding Google OAuth was explicitly rejected in an accepted decision made today (2026-07-08), because users have no corporate IdP and the solo maintainer can't absorb OAuth's operational overhead (`knowledge/decisions/magic-link-auth.md`). That decision says to revisit only if a significant user segment demands social login. Has that changed — do you have concrete evidence of user demand for 'Sign in with Google' (support requests, sign-up drop-off data, user feedback) that should reopen this decision?"

2. (Only if the answer to 1 is yes) "Is the intent for Google sign-in to *replace* magic links or to be offered *alongside* them? Note the standing constraints still apply: no password storage, and the maintenance budget is near zero, so I'd propose a single provider added alongside magic links, with the decision file superseded and the interview recorded."
