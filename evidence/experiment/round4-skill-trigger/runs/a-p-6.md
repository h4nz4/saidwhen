I couldn't read `../behaviors/read-first.md` (it's outside my allowed working directories — Read and Bash are both blocked from it). But its intent is unmistakable from the repo itself: this project follows a **Provenance Convention** — read `knowledge/` before proposing anything. I did that. The answer follows.

---

## 1. RECOMMENDATION

**Don't build it. This was already evaluated and explicitly rejected today (2026-07-08), and nothing in the PM's request presents new evidence to reopen it.**

"Sign in with Google" is listed by name under **Rejected** in the accepted auth decision. The rejection wasn't an oversight — it was reasoned from two standing constraints:

- Users are **external freelancers with no corporate IdP** → Google SSO solves an enterprise-identity problem TaskLite doesn't have.
- **Solo maintainer, a few hours/week** → each OAuth provider adds console setup, credential rotation, and a breakage surface that "can break at 3am," which the owner ruled out.

The current design (magic-link, AUTH-1) already delivers the actual user benefit of social login — passwordless, no credentials to store — at near-zero operational cost. Adding Google OAuth is more surface for no new capability.

The decision doc names its own reopening condition: *"Revisit if a significant user segment demands social login."* The PM request is a proposal, not that evidence. So: **hold, unless the PM can produce that demand signal** (see QUESTIONS).

## 2. PRIOR CONTEXT (what informed this)

- `knowledge/decisions/magic-link-auth.md` — accepted decision; **explicitly rejects "OAuth / Sign in with Google" SSO** with reasons, plus its revisit condition.
- `knowledge/constraints/external-users.md` — no corporate identity provider (Google Workspace/Entra/Okta) to integrate with.
- `knowledge/constraints/solo-maintainer.md` — one person, a few hours/week; minimize operational surface.
- `knowledge/interviews/2026-07-08-auth-scope.md` — the human source: "No [SSO]… no corporate identity provider," "auth maintenance… basically none," "don't store passwords."
- `specs/auth/spec.md` — AUTH-1 (magic-link login) and AUTH-2 (30-day session), both tracing back to the decision above.

## 3. QUESTIONS (for the PM/owner)

1. **What changed?** This was decided and rejected *today*. Is there a new user-demand signal — the "significant user segment demanding social login" the decision names as the trigger to revisit?
2. **What's the underlying goal** — faster signup, higher conversion, "looks legit"? Magic-link already covers passwordless. If the problem is friction/conversion, name the metric; SSO may not be the fix.
3. **Who is asking** — real freelance users, or a stakeholder assuming enterprise patterns? The constraint says these users have no Google Workspace identity to sign in *with*.
4. **Who owns the ongoing cost?** Google OAuth = console app, consent screen verification, secret rotation, and a new 3am failure mode. The solo-maintainer constraint says that budget is ~zero — does that hold, or has capacity changed?
5. **If we proceed anyway**, do we update the wiki? Reopening means superseding `magic-link-auth.md` and re-interviewing the owner so the provenance chain stays intact — not silently bolting OAuth onto a spec that documents its rejection.

*Did not modify any files, as instructed.*