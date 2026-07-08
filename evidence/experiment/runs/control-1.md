# RECOMMENDATION

Adding "Sign in with Google" is feasible and low-risk from a product standpoint, but it directly touches an existing hard requirement, so I recommend treating this as a **spec change first, implementation second**:

1. **Amend AUTH-1 before writing any code.** The auth spec currently states the system *MUST* authenticate users via single-use magic links, with no passwords stored. Google OAuth SSO is a second authentication method, so AUTH-1 as written forbids it. The spec should be revised to something like "The system MUST support passwordless authentication via (a) single-use magic links and (b) Google OAuth SSO. No passwords are stored." Note that Google SSO preserves the spirit of AUTH-1 (passwordless, no credential storage on our side), which is a point in its favor.

2. **Add a new requirement for identity matching (AUTH-3).** The critical design decision is how a Google sign-in maps to an existing magic-link account. Since magic-link auth already treats a verified email address as the identity anchor, the natural rule is: match on the Google-verified email (only when Google reports `email_verified: true`), auto-linking to any existing account with that email. This should be written into the spec explicitly because silent account linking is the main security-sensitive area of this feature (account-takeover risk if an unverified email is trusted).

3. **Keep AUTH-2 unchanged.** Session lifetime (30 days of inactivity) should apply identically regardless of how the session was established. State this explicitly in the spec revision so it is not ambiguous.

4. **Implementation approach.** Use the standard OAuth 2.0 / OpenID Connect authorization-code flow with PKCE against Google. Store only the Google subject identifier (`sub`) and verified email — do not persist access/refresh tokens, since TaskLite only needs authentication, not Google API access. Add a `federated_identities` (provider, provider_subject, user_id) table/association rather than a column on the user record, so additional providers can be added later without schema churn. Scope requested: `openid email profile` only.

5. **Scope control.** Do not bundle in "remove magic links", other providers (Apple, Microsoft, GitHub), or team/workspace SSO (SAML/OIDC enterprise SSO) — those are separate decisions. This change should be additive: magic links remain the fallback for users without Google accounts.

Rough sizing: small — one external integration, one new table, one new spec requirement plus one amended requirement, login-screen UI change.

# PRIOR CONTEXT

The project is nearly empty; the context found and used:

- `E:\PROJEKTI\okf\example-control\README.md` — describes TaskLite as a lightweight task tracker for freelancers. It says to browse `knowledge/` and `specs/` and that "every requirement links to the decision that created it, and every decision links to the human answer that justified it" — however, **no `knowledge/` directory exists in this project**, and the spec below contains no links to decisions. So the provenance trail the README promises is absent; I could not recover *why* the existing auth requirements are the way they are.
- `E:\PROJEKTI\okf\example-control\specs\auth\spec.md` — the only spec. Two requirements:
  - AUTH-1: users MUST be authenticated via single-use email magic links; no passwords stored. (Directly constrains this request — see Recommendation #1.)
  - AUTH-2: sessions MUST expire after 30 days of inactivity.

No source code, no decision records, no architecture docs, and no rationale for the magic-link-only choice were found anywhere in the project.

# QUESTIONS

1. **Why was magic-link-only chosen originally?** The README implies a recorded decision exists, but the `knowledge/` directory is missing. Was there a deliberate reason to exclude social/OAuth login (e.g., privacy stance, avoiding third-party dependencies, target-user preference)? If so, that rationale may argue against — or shape — this feature, and I don't want to silently reverse a considered decision.
2. **Account linking policy:** if someone signs in with Google and an account with that email already exists (created via magic link), should we auto-link silently, or require a confirmation step (e.g., a one-time magic link to confirm ownership) before linking?
3. **Is Google SSO additive or a replacement?** I assume magic links remain available for users without Google accounts — please confirm.
4. **Is Google the only provider planned, or the first of several?** This doesn't change the recommendation much (the design accommodates more providers either way), but it affects login-screen UX and how much we invest in provider abstraction now.
5. **Any compliance/hosting constraints** (e.g., EU data-residency, users in environments where Google is blocked) that should influence whether we take on a Google dependency for a core flow?
6. **Where should the decision for this change be recorded?** The README describes a provenance convention (requirements ↔ decisions ↔ human answers), but the scaffolding for it is absent in this repo. Should I create the `knowledge/` structure as part of this change, and if so, is there a template/convention document I should follow?
