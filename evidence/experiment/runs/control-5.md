# TaskLite — "Sign in with Google" (OAuth SSO) Evaluation

## 1. RECOMMENDATION

**Proceed, but as a spec change first — not a code task — and treat it as an *addition to*, not a replacement of, magic-link login until the original rationale for AUTH-1 is clarified.**

Key points:

1. **This request conflicts with an existing normative requirement.** `specs/auth/spec.md` AUTH-1 states the system *MUST* authenticate users via single-use magic links, with no passwords stored. Adding Google SSO either (a) relaxes AUTH-1 into "magic links OR Google OAuth", or (b) replaces it. Either way, AUTH-1 must be amended before implementation — otherwise the spec and the product diverge.

2. **The rationale behind AUTH-1 is undocumented in this repo, so I cannot tell whether Google SSO violates the original intent.** Magic-link-only auth is often chosen deliberately: to avoid password storage (explicitly stated), but sometimes also to avoid third-party identity dependencies, minimize data sharing, or keep the stack simple for a freelancer audience. If the decision was "no third-party IdPs," Google SSO contradicts it; if it was merely "no passwords," Google SSO is fully compatible (it introduces no stored passwords). This distinction determines whether the change is trivial or a real product-direction reversal, and only a human who knows the original decision can resolve it.

3. **Proposed shape of the change (assuming "no passwords" was the intent):**
   - Amend AUTH-1: "The system MUST authenticate users via single-use magic links sent to their email address, OR via Google OAuth 2.0 / OpenID Connect. No passwords are stored." (The "no passwords stored" invariant is preserved.)
   - Add AUTH-3 (account identity): accounts are keyed by verified email address; a Google sign-in whose verified email matches an existing magic-link account MUST log into that same account (no duplicate accounts). Only accept Google's `email_verified: true` claim to prevent account-takeover via unverified emails.
   - Confirm AUTH-2 (30-day inactivity expiry) applies identically to sessions created via Google SSO — TaskLite issues its own session; Google is used only at sign-in time, and Google token lifetimes do not extend TaskLite sessions.
   - Implementation notes for later: use the OpenID Connect authorization-code flow with PKCE and `state` validation; store only the Google `sub` claim + email (request minimal scopes: `openid email profile`); no refresh-token storage needed since Google is only an authenticator; keep magic link as the fallback path so users without Google accounts are not locked out.

4. **Sequencing:** (1) get answers to the questions below, (2) update `specs/auth/spec.md` (and record the decision in `knowledge/`, per the convention the README describes), (3) then implement.

## 2. PRIOR CONTEXT

The project is minimal. Everything I found and used:

- `E:\PROJEKTI\okf\example-control\README.md` — Describes TaskLite as a fictional lightweight task tracker *for freelancers* (relevant to audience fit for Google SSO). It also says to "Browse `knowledge/` and `specs/`" and claims "every requirement links to the decision that created it, and every decision links to the human answer that justified it."
- `E:\PROJEKTI\okf\example-control\specs\auth\spec.md` — The only spec. Contains AUTH-1 (magic-link login MUST be used; no passwords stored) and AUTH-2 (sessions expire after 30 days of inactivity). AUTH-1 is the requirement directly affected by this request. Neither requirement contains the decision links the README promises.
- **Gap:** the `knowledge/` directory referenced by the README **does not exist** in this repository, and the spec has no links to decisions or human answers. There is also no application code. So the provenance trail for *why* magic-link-only was chosen is unavailable — which is precisely the context needed to judge whether Google SSO is compatible with the original decision. This gap is the main driver of my questions below.

## 3. QUESTIONS

1. **What was the original rationale for AUTH-1's magic-link-only decision?** Specifically: was it only "never store passwords," or also "avoid third-party identity providers" (for privacy, vendor-independence, or simplicity)? The `knowledge/` directory the README references is missing from this repo, so I can't check the recorded decision — if it exists elsewhere, please point me to it.
2. **Is Google SSO an *addition* to magic-link login or a *replacement*?** I recommend addition (magic link stays as the fallback for users without Google accounts), but please confirm.
3. **Account linking:** if a user who registered via magic link signs in with a Google account bearing the same verified email, should they land in the same account automatically (my recommendation), or should linking require an explicit confirmation step?
4. **Scope of Google accounts:** any Google account, or restricted (e.g., Google Workspace domains)? Given the freelancer audience I assume any account, but confirming.
5. **Are more providers expected soon** (Apple, Microsoft, GitHub)? If yes, we should build a generic OIDC provider abstraction now rather than hard-coding Google.
6. **Sessions:** confirm AUTH-2's 30-day inactivity expiry applies unchanged to SSO-initiated sessions (i.e., TaskLite issues its own session and Google is consulted only at sign-in).
7. **Compliance/data constraints:** are there any privacy commitments to users (e.g., "we share no data with third parties") in marketing or ToS that adding a Google dependency would breach?
