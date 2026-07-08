# TaskLite — "Sign in with Google" (OAuth SSO) evaluation

## 1. RECOMMENDATION

**Do not proceed with Google OAuth SSO as requested — it directly contradicts an accepted, currently-valid project decision.**

TaskLite's authentication approach was explicitly decided in `knowledge/decisions/magic-link-auth.md` (`status: accepted`, 2026-07-08 — today): the product authenticates via emailed single-use magic links, and **OAuth / "Sign in with Google" SSO was specifically evaluated and rejected** in that decision's `## Rejected` section. The rejection rationale is grounded in two documented constraints:

1. **Users are external freelancers with no corporate identity provider** (`knowledge/constraints/external-users.md`) — there is no Google Workspace / Entra / Okta tenant to integrate with, so SSO delivers little of its usual value.
2. **Solo maintainer, near-zero maintenance budget** (`knowledge/constraints/solo-maintainer.md`) — each OAuth provider adds Google Cloud console setup, client-secret/credential rotation, consent-screen verification, and third-party breakage surface that a one-person, few-hours-per-week operation cannot absorb. The owner said in the scoping interview: "Anything that can break at 3am is out."

The decision's evidence is dated today and remains plausible, so per project convention I respect it rather than re-litigate it. The spec already encodes it as requirement AUTH-1 (`specs/auth/spec.md`), which mandates magic-link login.

**However, the decision includes an explicit revisit trigger:** *"Revisit if a significant user segment demands social login."* The PM's request may be exactly that trigger firing — but the request as stated doesn't say why. So the correct next step is not implementation and not a flat refusal; it is to ask the PM the delta question (see QUESTIONS below).

**If the revisit trigger is real** (documented user demand for social login), my proposal would be:
- Add "Sign in with Google" as an **additional** login option alongside magic links, not a replacement — magic links stay as the universal fallback, preserving the no-passwords position.
- Use a managed auth library/provider pattern that minimizes operational surface (single OAuth provider, no token refresh against Google APIs beyond sign-in, account linking keyed on verified email), to stay as compatible as possible with the solo-maintainer constraint.
- Update the knowledge bundle: supersede/amend `decisions/magic-link-auth.md`, record the new evidence in a new interview file, update `specs/auth/spec.md`, and append to `knowledge/log.md`.

**If the trigger is not real** (no documented user demand — e.g. the request is a generic "everyone has Google login" impulse), I recommend keeping magic-link-only auth and citing the existing decision.

## 2. PRIOR CONTEXT

Prior context found in the project's OKF knowledge bundle and specs (all paths absolute):

- `E:\PROJEKTI\okf\example\knowledge\index.md` — entry point; lists the auth decision, both constraints, and the scoping interview.
- `E:\PROJEKTI\okf\example\knowledge\decisions\magic-link-auth.md` — **the controlling decision**: `type: Decision`, `status: accepted`, 2026-07-08. Magic-link auth chosen; OAuth/Google SSO and passwords explicitly rejected; contains the revisit clause "Revisit if a significant user segment demands social login."
- `E:\PROJEKTI\okf\example\knowledge\constraints\external-users.md` — users are individual freelancers; no corporate IdP exists to integrate with.
- `E:\PROJEKTI\okf\example\knowledge\constraints\solo-maintainer.md` — one person, a few hours/week; every choice must minimize operational surface.
- `E:\PROJEKTI\okf\example\knowledge\interviews\2026-07-08-auth-scope.md` — the owner's (Ivan's) primary-source answers: no SSO need, essentially zero auth-maintenance budget, no formal compliance, "don't store passwords."
- `E:\PROJEKTI\okf\example\specs\auth\spec.md` — AUTH-1 (magic-link login MUST, no passwords) and AUTH-2 (30-day session expiry), both linking back to the magic-link decision as their "why."
- `E:\PROJEKTI\okf\example\knowledge\log.md` — confirms the whole auth decision chain was created 2026-07-08 (evidence is fresh, not stale).

This context fully answers the questions I would otherwise have asked (who the users are, whether a corporate IdP exists, how much maintenance is acceptable, compliance posture) — so I am not asking those.

## 3. QUESTIONS

Only the delta question warranted by the revisit clause:

1. "OAuth/Google SSO was explicitly rejected in the accepted decision `knowledge/decisions/magic-link-auth.md` (2026-07-08), because users are external freelancers with no corporate IdP and the project is solo-maintained with a near-zero auth-maintenance budget. That decision says to revisit only if a significant user segment demands social login. **Has that changed — do we now have concrete evidence (support requests, churn feedback, sign-up drop-off) that a significant user segment is demanding 'Sign in with Google'?** If yes, what is that evidence, so it can be recorded as the basis for superseding the decision?"

If the answer is no, I will not implement Google SSO and will cite the existing decision. If the answer is yes, one follow-up before implementation:

2. "Given the solo-maintainer constraint still holds, do you agree Google sign-in should be an *additional* option alongside magic links (magic links remain the fallback), rather than a replacement?"
