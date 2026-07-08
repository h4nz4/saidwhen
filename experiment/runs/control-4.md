# TaskLite — "Sign in with Google" (OAuth SSO) Evaluation

## 1. RECOMMENDATION

Proceed, but as a **spec-level change first** — and treat it as an *addition* to the existing auth model, not a replacement.

Key points driving the recommendation:

- **The current spec conflicts with the request as written.** `specs/auth/spec.md` AUTH-1 states the system "MUST authenticate users via single-use magic links sent to their email address. No passwords are stored." A strict reading makes magic links the *only* permitted authentication method. Adding Google SSO therefore requires amending AUTH-1 (e.g., rephrase to "MUST support magic-link login" and drop the exclusivity), not just appending a new requirement. The "no passwords are stored" property is preserved by OAuth, which keeps the spirit of the original decision intact — but I could not find the rationale behind AUTH-1's exclusivity (see Prior Context), so the original intent should be confirmed with a human before weakening it.

- **Proposed spec shape:**
  - Amend **AUTH-1** to make magic links one supported method rather than the sole method, keeping the "no passwords stored" invariant as its own explicit requirement.
  - Add **AUTH-3: Google OAuth sign-in** — authenticate via OpenID Connect (Authorization Code flow with PKCE), accepting only Google identities where `email_verified` is true.
  - Add **AUTH-4: Account linking** — a Google sign-in whose verified email matches an existing magic-link account signs into that same account (single account per email), rather than creating a duplicate. This is the highest-risk design point; email-based linking is safe here only because Google verifies emails and magic links already treat email ownership as the identity root.
  - **AUTH-2 (30-day inactivity expiry) applies unchanged** to sessions created via Google SSO — session lifetime is a property of the session, not the login method.

- **Implementation notes (once specs are agreed):** standard OIDC against Google (`accounts.google.com`), store only the Google `sub` claim + email on the user record, request minimal scopes (`openid email profile`), no refresh-token/offline access needed since TaskLite manages its own sessions. Keep the door open to other IdPs by storing provider-namespaced identities (`provider` + `subject`) rather than a Google-specific column.

- **Process note:** the README says this project follows a "Provenance Convention" where every requirement links to the decision that created it. Whatever is decided here should be recorded that way — a decision record answering the questions below, linked from the amended/new AUTH requirements. However, the `knowledge/` directory the README references does not exist in the repo, so there is no prior decision trail to consult or extend (see below).

## 2. PRIOR CONTEXT

Context found and used (the project is very small — two files total, no application code):

- `E:\PROJEKTI\okf\example-control\README.md` — describes TaskLite as a fictional lightweight task tracker for freelancers, demonstrating the "Provenance Convention": requirements link to decisions, decisions link to human answers. It points to `knowledge/` and `specs/` directories.
- `E:\PROJEKTI\okf\example-control\specs\auth\spec.md` — the only spec. Contains AUTH-1 (magic-link login is *the* authentication method; no passwords stored) and AUTH-2 (sessions expire after 30 days of inactivity).

Gaps in prior context:

- The `knowledge/` directory referenced by the README **does not exist**, and `specs/auth/spec.md` contains no provenance links. So the decision and human answer that justified AUTH-1's magic-link-only stance are unavailable. I cannot determine *why* magic links were chosen exclusively (simplicity? cost? a deliberate anti-SSO stance? avoiding third-party dependencies?), which is exactly the information needed to judge whether adding Google SSO contradicts an earlier deliberate decision.
- There is no application code, so no assumptions can be made about the existing auth implementation, framework, or session storage.

## 3. QUESTIONS

Questions I would ask the human before proceeding:

1. **Why was magic-link chosen as the *only* auth method in AUTH-1?** Was excluding other methods (including SSO) a deliberate decision, and if so, what motivated it? (The provenance record the README promises is missing, so I can't check.)
2. **Should magic-link login remain available alongside Google SSO**, or is the long-term intent to migrate users to Google sign-in?
3. **Account linking policy:** if someone signs in with Google using an email that already has a magic-link account, should they land in that existing account automatically (my recommendation), or should linking require an explicit confirmation step?
4. **Scope of providers:** is this Google-only, or should the design anticipate other IdPs (Apple, Microsoft, generic OIDC) soon? This affects the data model (provider-namespaced identities) and UI.
5. **Google Workspace accounts:** any need to restrict or specially handle Workspace domains (e.g., `hd` claim restrictions), or is any Google account acceptable? (TaskLite targets freelancers, so presumably any account — confirming.)
6. **What drives this request** — user demand, sign-up conversion, partner requirement? This shapes prioritization and whether SSO should appear on the sign-up flow, the sign-in flow, or both.
7. **Where should the provenance record live?** The README references a `knowledge/` directory that doesn't exist — should I create it as part of this change and backfill the AUTH-1 decision, or is the provenance material kept elsewhere?
