# TaskLite — "Sign in with Google" (OAuth SSO) Evaluation

## 1. RECOMMENDATION

Proceed with caution: adding Google SSO is technically straightforward, but it directly conflicts with an existing spec requirement, so the first step is a spec decision, not code.

- **Conflict to resolve first.** `specs/auth/spec.md` AUTH-1 states the system "MUST authenticate users via single-use magic links sent to their email address. No passwords are stored." Adding Google OAuth changes the authentication model from "magic links only" to "magic links OR Google SSO" (or replaces magic links entirely — unclear from the request). AUTH-1 must be amended before implementation, and the amendment depends on the original rationale for magic-link-only, which I could not find in this repo (the README references a `knowledge/` directory of decisions, but it does not exist here).
- **Compatibility note in our favor.** Google SSO is philosophically consistent with the spirit of AUTH-1: no passwords are stored either way. So if the original decision was driven by "avoid password storage/management," Google SSO does not violate that intent — it only violates the letter of the requirement.
- **Proposed approach (pending answers to the questions below):**
  1. Amend AUTH-1 to: "The system MUST authenticate users without storing passwords. Supported methods: (a) single-use magic links, (b) Google OAuth 2.0 / OpenID Connect sign-in." Record the decision and its justification (per the Provenance Convention the README describes).
  2. Implement Google sign-in using OpenID Connect (Authorization Code flow with PKCE), verifying the ID token and using the verified `email` claim as the identity key.
  3. **Account linking:** treat a Google sign-in whose verified email matches an existing magic-link account as the same account (safe here because Google verifies email ownership, same as a magic link does). New emails create new accounts.
  4. Preserve AUTH-2 unchanged: sessions created via Google SSO get the same 30-day inactivity expiry. Do not rely on Google token lifetimes for session management — issue our own session exactly as magic-link login does.
  5. Store only the minimum: Google subject ID (`sub`) and email per user. No refresh tokens needed unless we later want Google API access (out of scope for sign-in).
- **Effort estimate:** small. One OAuth callback route, one button on the login screen, a `google_sub` column/field on the user record, plus spec/decision updates. TaskLite targets freelancers, who overwhelmingly have Google accounts, so product fit is good; magic links should remain as the fallback for non-Google users unless the PM decides otherwise.

## 2. PRIOR CONTEXT

- `E:\PROJEKTI\okf\example-control\specs\auth\spec.md` — the authentication spec. AUTH-1 (magic-link login, MUST, no passwords stored) is the requirement this feature collides with; AUTH-2 (30-day inactivity session expiry) applies to any new sign-in method.
- `E:\PROJEKTI\okf\example-control\README.md` — describes TaskLite as a lightweight task tracker for freelancers and says the repo follows a "Provenance Convention": every requirement should link to the decision that created it, and every decision to the human answer that justified it. It points to `knowledge/` and `specs/` directories.
- **Gap found:** the `knowledge/` directory referenced by the README does not exist in this repo, and `spec.md` contains no links to decisions. So the rationale behind "magic links only" (AUTH-1) is unavailable — I cannot tell whether OAuth/social login was previously considered and deliberately rejected, or simply never discussed. This gap is the main reason for the questions below.
- No application code exists in the repo (only README and the spec), so there is no existing auth implementation to evaluate for integration effort.

## 3. QUESTIONS

1. AUTH-1 currently mandates magic links as the only authentication method. Was "magic-link only" a deliberate decision (e.g., simplicity, avoiding OAuth vendor lock-in, privacy stance toward Google), or just the initial choice? Is there a decision record for it outside this repo — the `knowledge/` directory the README references is missing?
2. Should Google SSO be **added alongside** magic links, or **replace** them? (My recommendation is alongside, keeping magic links as the fallback for users without Google accounts.)
3. Account linking: when someone signs in with Google using an email that already has a magic-link account, should we automatically treat it as the same account (my recommendation, since both methods verify email ownership), or keep them separate / require explicit linking?
4. Is Google the only identity provider planned, or should the design anticipate others (Apple, Microsoft, GitHub)? This affects whether we hard-code Google or build a small provider abstraction now.
5. Do we need anything from Google beyond sign-in (e.g., Calendar/Gmail integration for tasks)? That determines requested OAuth scopes and whether we must store refresh tokens — otherwise I'd request only `openid email profile` and store no Google tokens.
6. Any constraints on data residency/privacy for the target users (e.g., EU freelancers) that should be recorded alongside the decision — such as noting that sign-in metadata will flow through Google?
