I read the project's knowledge base first (per the read-first behavior — read decision provenance before acting). This request has already been evaluated. Here is the proposal.

## 1. RECOMMENDATION

**Don't build it — not yet.** "Sign in with Google" was already evaluated and **explicitly rejected today (2026-07-08)** in the accepted auth decision. Nothing in the PM request cites new evidence that would overturn that decision.

The existing decision even names the one condition that reopens it: *"Revisit if a significant user segment demands social login."* The PM request asserts a feature, not that condition. So the lazy-but-correct move is to point back at the recorded decision and ask for the missing evidence, rather than spec-ing an integration that contradicts two standing constraints.

If that evidence exists, OAuth becomes a legitimate *addition alongside* magic links (not a replacement) — but that's a new decision, and it should be recorded as one, superseding the "rejected" note with its justification.

## 2. PRIOR CONTEXT (what informed this)

- `knowledge/decisions/magic-link-auth.md` — **accepted 2026-07-08.** Explicitly lists *"OAuth / 'Sign in with Google' SSO"* under **Rejected**, because users have no corporate IdP and each provider adds credential rotation, console setup, and breakage surface. Also defines the revisit trigger.
- `knowledge/constraints/external-users.md` — users are individual freelancers with **no corporate identity provider** (no Google Workspace/Entra/Okta). Google SSO's usual justification (org-managed identity) doesn't apply here.
- `knowledge/constraints/solo-maintainer.md` — one maintainer, a few hours/week; every choice must minimize operational surface.
- `knowledge/interviews/2026-07-08-auth-scope.md` — the human source: *"Anything that can break at 3am is out"* and *"just don't store passwords."* (OAuth doesn't store passwords — a point in its favor — but it does add a 3am-breakage surface, the console/secret it depends on.)
- `specs/auth/spec.md` — AUTH-1 mandates magic-link login as the authentication method; AUTH-2 sets 30-day sessions. Both trace back to the decision above.

## 3. QUESTIONS (for the PM / owner)

1. **What changed since this morning?** The rejection was recorded today. Is there new evidence, or did the decision record not reach you?
2. **Is there a "significant user segment demanding social login"** — the documented revisit trigger? How many users, and are they asking for Google specifically, or just "fewer emailed links"? (If it's the latter, that's a magic-link UX problem, not an OAuth need.)
3. **Add or replace?** Google SSO *alongside* magic links, or instead of them? (Replacing breaks AUTH-1 and abandons non-Google users.)
4. **Who owns the 3am surface** — the Google Cloud console project, OAuth consent screen, and client-secret rotation — given the solo-maintainer constraint?
5. **If we proceed, may I record it as a new decision** that supersedes the rejection note (with the demand evidence as its justification), so the provenance stays intact?

---
Skipped: writing any spec/decision file — you said don't modify, and the decision to build isn't made yet. Add the decision record + `specs/auth` OAuth requirement once Q2/Q3 are answered.