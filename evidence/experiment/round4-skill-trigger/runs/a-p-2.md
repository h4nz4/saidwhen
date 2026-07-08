Note: `../behaviors/read-first.md` is outside this session's allowed working directory, so I couldn't open it directly (Read and `cat` both blocked). I followed its evident intent — read TaskLite's `knowledge/` provenance wiki before proposing anything. That wiki answered the question outright.

## 1. RECOMMENDATION

**Don't build it. "Sign in with Google" was already evaluated and explicitly rejected today (2026-07-08), with documented reasons that still hold.** This isn't a new evaluation — it's a re-open of a closed decision, and nothing in the PM request supplies the one condition the decision named for revisiting it.

The accepted approach is magic-link auth. OAuth SSO was rejected for two reasons tied to standing constraints:
- Users are external freelancers with **no corporate IdP** — the population SSO exists to serve isn't there.
- The project is **solo-maintained, a few hours/week** — each OAuth provider adds console setup, credential rotation, and breakage surface ("anything that can break at 3am is out").

The decision left an explicit reopen trigger: *"Revisit if a significant user segment demands social login."* The PM request doesn't cite that demand. So the correct action is to point back at the existing decision and ask for the evidence that would justify overturning it — not to write a proposal.

## 2. PRIOR CONTEXT (what informed this)

- `knowledge/decisions/magic-link-auth.md` — **accepted**; its "Rejected" section names *"OAuth / 'Sign in with Google' SSO"* verbatim, with reasons and a revisit condition.
- `knowledge/constraints/external-users.md` — no corporate identity provider (Google Workspace / Entra / Okta) to integrate.
- `knowledge/constraints/solo-maintainer.md` — one person, a few hours/week; minimize operational surface.
- `knowledge/interviews/2026-07-08-auth-scope.md` — owner (Ivan): "No [SSO]… no corporate identity provider," "Basically none [maintenance]… anything that can break at 3am is out," "don't store passwords."
- `specs/auth/spec.md` — AUTH-1 mandates magic-link login, linked back to the decision above.

## 3. QUESTIONS (for the PM/owner)

1. Are you aware this exact option was rejected earlier today? What changed since — or is this a request to reopen the decision?
2. Is there a **significant user segment demanding social login** (the documented revisit trigger)? How many, and what's the evidence — the constraint says users have no corporate IdP.
3. Who absorbs the ongoing maintenance (Google Cloud console app, OAuth consent screen, credential rotation, breakage) given the solo-maintainer, few-hours-a-week constraint?
4. Magic-link already gives passwordless login with near-zero ops. What does Google SSO add that magic-link doesn't — faster login, or a specific user ask?
5. If we proceed, do you want it to *replace* or *sit alongside* magic-link (AUTH-1)? Adding a second auth path roughly doubles the auth surface to maintain.

skipped: any design/effort proposal for the OAuth flow — YAGNI until the reopen trigger (proven user demand) is met. add when Q2 comes back with a real segment.