# RECOMMENDATION

Do not start implementing yet. Adding "Sign in with Google" is not a purely additive feature in this project — it directly conflicts with the existing authentication spec, and the rationale behind that spec is not recoverable from the repository. Proceed in three steps:

1. **Resolve the spec conflict first.** `specs/auth/spec.md` (AUTH-1) states the system "MUST authenticate users via single-use magic links sent to their email address. No passwords are stored." A MUST-level requirement naming a single mechanism means Google OAuth is a spec change, not just a feature addition. Before any code, AUTH-1 must be amended — either to "MUST support magic-link login and MAY/MUST support Google SSO" or to a more general "passwordless authentication" requirement with magic links and Google OAuth as permitted mechanisms. Notably, Google SSO does not violate the spirit of "no passwords are stored" (TaskLite still stores no passwords), so the two methods are likely compatible in intent — but that reading needs human confirmation because the original decision rationale is missing (see PRIOR CONTEXT).

2. **Design the identity model around email as the join key, with explicit account-linking rules.** Since magic-link auth already keys identity to a verified email address, the natural design is: on successful Google sign-in, if the Google-verified email matches an existing TaskLite account, link and sign in to that account; otherwise create a new account. Only trust emails Google reports as verified (`email_verified: true`), otherwise an attacker with an unverified Google identity could take over an existing magic-link account. Use OAuth 2.0 / OpenID Connect Authorization Code flow with PKCE; store only the Google subject identifier (`sub`) and email — no additional scopes, no offline access, since TaskLite only needs authentication, not Google API access.

3. **Keep session semantics unchanged.** AUTH-2 requires sessions to expire after 30 days of inactivity. Google sign-in should mint the same first-party session as magic-link login does — do not introduce a second session mechanism or tie session lifetime to Google token lifetime. Whichever method the user authenticates with, the resulting session is identical.

Suggested scope for a first increment, once the spec is amended and questions below are answered:
- Add a "Sign in with Google" button alongside the magic-link form.
- Implement OIDC Authorization Code + PKCE flow against Google.
- Account linking by verified email as described above.
- Update `specs/auth/spec.md` with the amended AUTH-1 and a new requirement (e.g., AUTH-3) covering SSO behavior: verified-email requirement, account-linking rule, and the "no Google data beyond sub + email" constraint.
- Record the decision and its justification per the project's Provenance Convention (the README says every requirement should link to the decision that created it and every decision to the human answer justifying it), so this change carries its provenance from day one.

Explicitly out of scope unless requested: other providers (Apple, Microsoft, GitHub), Google Workspace domain restrictions, SCIM/provisioning, and removing magic-link login.

# PRIOR CONTEXT

The project is minimal; the following is everything that exists:

- `E:\PROJEKTI\okf\example-control\README.md` — Describes TaskLite as a fictional lightweight task tracker for freelancers used to demonstrate the "Provenance Convention." It instructs readers to browse `knowledge/` and `specs/`, promising that "every requirement links to the decision that created it, and every decision links to the human answer that justified it."
- `E:\PROJEKTI\okf\example-control\specs\auth\spec.md` — The only spec file. Contains:
  - AUTH-1 (Magic-link login): the system MUST authenticate via single-use magic links sent to email; no passwords are stored. This is the requirement that Google SSO would amend.
  - AUTH-2 (Session lifetime): sessions MUST expire after 30 days of inactivity. Constrains the SSO session design (step 3 above).

**Gap found:** the `knowledge/` directory referenced by the README does not exist in this copy of the project. That means the decision record and human justification behind AUTH-1 (why magic-link-only? was SSO previously considered and rejected?) are missing. I therefore could not verify whether "no passwords" was the whole intent (in which case Google SSO is compatible) or whether there was a stronger reason to avoid third-party identity providers (e.g., privacy stance, no-third-party-dependency policy, target audience of freelancers). This unrecoverable rationale is the main reason I recommend asking before building.

# QUESTIONS

1. AUTH-1 currently mandates magic links as the only authentication method. Do you want Google SSO **in addition to** magic links, or **replacing** them? (I assume "in addition" — please confirm.)
2. The `knowledge/` directory with decision provenance is missing from this repo. Do you know the original rationale for magic-link-only auth — specifically, was avoiding third-party identity providers (like Google) a deliberate decision, or was the intent only "no passwords"? If the knowledge base exists elsewhere, can you point me to it?
3. Account linking: if a user signs in with Google and the verified Google email matches an existing magic-link account, should we automatically link and sign them into that account (my recommendation), or require an explicit confirmation step (e.g., a magic-link verification before linking)?
4. Is Google the only provider for now, or should the design anticipate more providers (Apple, Microsoft, GitHub) soon? This affects whether we build a single hardcoded integration or a small provider abstraction.
5. Should users be able to unlink Google / manage sign-in methods in settings, or is that out of scope for the first release?
6. Are there any deployment constraints I should know about — e.g., which Google Cloud project/organization owns the OAuth client, required redirect URI domains, or whether TaskLite targets any market where Google sign-in is problematic?
7. Confirm session behavior: a Google-initiated session should follow AUTH-2 exactly (30-day inactivity expiry, same first-party session as magic links), with no dependence on Google token lifetimes — correct?
