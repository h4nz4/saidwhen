# RECOMMENDATION

Do not implement "Sign in with Google" right now. This exact option was evaluated and **explicitly rejected** in an accepted decision — `knowledge/decisions/magic-link-auth.md` (`status: accepted`, timestamp 2026-07-08, i.e. today). TaskLite authenticates via emailed single-use magic links; the decision's `## Rejected` section names "OAuth / 'Sign in with Google' SSO" and gives the reasons:

- Users are external freelancers with **no corporate identity provider** (`knowledge/constraints/external-users.md`).
- The project is **solo-maintained, a few hours per week**; each OAuth provider adds credential rotation, Google Cloud console setup, and 3am-breakage surface the maintainer cannot absorb (`knowledge/constraints/solo-maintainer.md`, and Ivan's own words in the interview: "Anything that can break at 3am is out").

The decision is fresh (accepted today) and its evidence is still plausible, so per project convention I respect it rather than re-litigate it. However, the decision itself carries an explicit revisit trigger: *"Revisit if a significant user segment demands social login."* A PM request may be a signal that this trigger has fired — but the request as stated gives no evidence of user demand, so the correct next step is to ask the delta question (below), not to start building.

**If the revisit trigger is confirmed** (real user demand data), my proposal would be:

1. Add Google OAuth as an *optional second* login method alongside magic links (never a replacement — magic links remain the fallback and keep the "no passwords" property intact; AUTH-1 in `specs/auth/spec.md` would be amended, not deleted).
2. Scope it to Google only (one provider = smallest possible operational surface for a solo maintainer); use the account email as the join key to existing magic-link accounts.
3. Update the decision file: supersede or amend `magic-link-auth.md` with the new evidence, record the PM's answers in a new `knowledge/interviews/` entry, append to `knowledge/log.md`, and update `knowledge/index.md`.

**If the trigger has not fired**, the request should be declined with a pointer to the existing decision, and no files change.

# PRIOR CONTEXT

Found and used, per `E:\PROJEKTI\okf\behaviors\read-first.md` (read first, as instructed):

- `E:\PROJEKTI\okf\example\knowledge\index.md` — entry point; TaskLite is a lightweight task tracker for freelancers, solo-maintained.
- `E:\PROJEKTI\okf\example\knowledge\decisions\magic-link-auth.md` — **the load-bearing document**: accepted decision for magic-link auth whose `## Rejected` section explicitly rejects OAuth/"Sign in with Google" SSO, with a revisit clause ("if a significant user segment demands social login").
- `E:\PROJEKTI\okf\example\knowledge\interviews\2026-07-08-auth-scope.md` — Ivan (owner): users are external freelancers, no corporate IdP; near-zero maintenance budget; "don't store passwords."
- `E:\PROJEKTI\okf\example\knowledge\constraints\external-users.md` — no corporate identity provider (Google Workspace, Entra, Okta) to integrate with.
- `E:\PROJEKTI\okf\example\knowledge\constraints\solo-maintainer.md` — one person, a few hours per week; every choice must minimize operational surface.
- `E:\PROJEKTI\okf\example\specs\auth\spec.md` — AUTH-1 (magic-link login MUST, no passwords stored) and AUTH-2 (30-day session expiry), both linked to the decision above.
- `E:\PROJEKTI\okf\example\knowledge\log.md` — confirms the entire auth decision chain was created 2026-07-08 (today); the evidence is current, not stale.

The wiki already answers the general questions ("do users need SSO?" — no; "how much maintenance can auth absorb?" — basically none), so I am not re-asking those.

# QUESTIONS

Only the delta question is warranted — the wiki answers everything else:

1. "OAuth/Google SSO was explicitly rejected in a decision accepted today (2026-07-08), because users are external freelancers with no corporate IdP and the solo maintainer can't absorb the operational overhead. That decision says to revisit only if a significant user segment demands social login. **What changed — is there concrete user demand (support requests, churn data, user feedback) for Google sign-in, or new information that invalidates either constraint?**"

2. (Only if the answer to 1 is "yes, demand exists") "Should Google sign-in be *additive* to magic links (my recommendation — magic links remain for users without Google accounts and as the zero-dependency fallback), or are you asking to replace magic links entirely? Replacement would contradict AUTH-1 and re-open the whole auth decision."
