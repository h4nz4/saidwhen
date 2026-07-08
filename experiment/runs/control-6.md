# TaskLite — "Sign in with Google" (OAuth SSO) Evaluation

## 1. RECOMMENDATION

Proceed, but as an **additive** auth method — not a replacement — and only after confirming why the current passwordless design was chosen.

Key points:

- **Compatibility with the existing spec.** The auth spec (AUTH-1) mandates magic-link login and explicitly states "No passwords are stored." Google OAuth is philosophically compatible with this (still no passwords stored by TaskLite), but AUTH-1 is written as "The system MUST authenticate users via single-use magic links," which reads as exclusive. Adding Google requires a spec change, not just an implementation change — either relaxing AUTH-1 or adding a new requirement (e.g., AUTH-3: Google OAuth sign-in) and rewording AUTH-1 to "MUST support" rather than implying it is the sole method.
- **Fit for the audience.** TaskLite targets freelancers, who overwhelmingly have Google accounts (Gmail/Workspace). Google SSO reduces the friction of the magic-link round-trip (open email, click link), so the feature is plausibly valuable.
- **Proposed approach (spec-level, since this repo is specs/docs only — there is no implementation code here):**
  1. Add AUTH-3: users MAY authenticate via Google OAuth (OpenID Connect, authorization-code flow with PKCE); TaskLite stores only the Google subject identifier and verified email — no passwords, no tokens beyond what session management needs.
  2. Account identity remains keyed on verified email: a Google sign-in with `email_verified: true` for an address that already has a magic-link account resolves to the same account (auto-link), so users can't accidentally split their data. If Google reports the email unverified, fall back to a magic-link confirmation before linking.
  3. AUTH-2 (30-day inactivity expiry) applies unchanged to sessions created via Google — session lifetime is a property of the session, not the sign-in method.
  4. Keep magic links as the universal fallback (Google outage, users without Google accounts, de-Googling users).
- **Risks to flag:** dependency on a third-party IdP for a product whose current auth is fully self-contained; Google Cloud project/consent-screen setup and verification; and the possibility that "magic-link only" was a deliberate prior decision (privacy positioning, simplicity, avoiding third-party trackers) whose rationale I could not find in this repo — see QUESTIONS.

## 2. PRIOR CONTEXT

- `E:\PROJEKTI\okf\example-control\specs\auth\spec.md` — the existing auth requirements:
  - AUTH-1: Magic-link login — "The system MUST authenticate users via single-use magic links sent to their email address. No passwords are stored."
  - AUTH-2: Session lifetime — "Sessions MUST expire after 30 days of inactivity."
- `E:\PROJEKTI\okf\example-control\README.md` — describes TaskLite as a fictional lightweight task tracker for freelancers, and says the project demonstrates a "Provenance Convention" where every requirement links to the decision that created it and every decision links to the human answer justifying it. **However, the referenced `knowledge/` directory does not exist in this copy of the project** — the only files present are the README and the auth spec. So the decision rationale behind AUTH-1/AUTH-2 (why magic links were chosen, whether other auth methods were considered and rejected) is not available to me. My recommendation is therefore made without knowing whether "no OAuth/SSO" was previously an explicit decision.

## 3. QUESTIONS

1. Was magic-link-only auth a deliberate decision that excluded OAuth/social login (e.g., for privacy positioning, simplicity, or avoiding third-party dependencies)? If so, what was the rationale, and has it changed? The README implies this rationale should exist in `knowledge/`, but that directory is missing from the repo I can see.
2. Is Google sign-in intended to be **in addition to** magic links, or to **replace** them? (My recommendation assumes additive.)
3. Account linking policy: if a user signs in with Google using an email that already has a magic-link account, should we auto-link on Google's `email_verified` claim, or require an explicit confirmation step?
4. Does the 30-day inactivity session expiry (AUTH-2) apply unchanged to Google-authenticated sessions, or do you want a different policy for SSO sessions?
5. Scope: Google only for now, or should the spec be written generically for OIDC providers so Apple/Microsoft can be added later without another spec change?
6. Are there privacy or data-handling constraints for the freelancer audience (e.g., GDPR positioning, "we don't share data with Google" marketing claims) that this feature would touch?
