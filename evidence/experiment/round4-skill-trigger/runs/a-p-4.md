I read the knowledge base first (the `behaviors/read-first.md` file itself sits outside this session's allowed directories, but its intent — consult provenance before answering — is exactly what TaskLite's `knowledge/` wiki is built for, so I followed it there).

## 1. RECOMMENDATION

**Do not add "Sign in with Google" now.** This exact option was already evaluated and **explicitly rejected** on 2026-07-08, and nothing in the PM's request presents new evidence to overturn that decision.

The standing decision (`knowledge/decisions/magic-link-auth.md`) rejected OAuth/Google SSO for two documented reasons that still hold:
- Users are external freelancers with **no corporate identity provider** — the usual driver for SSO is absent.
- The project is **solo-maintained, a few hours/week** — each OAuth provider adds console setup, credential rotation, and 3am breakage surface the maintainer said is out of scope.

The decision left a specific re-open condition: *"Revisit if a significant user segment demands social login."* The right response to the PM is to test against that condition, not to start building. If that demand can't be shown, magic-link (AUTH-1) stays.

## 2. PRIOR CONTEXT

- `knowledge/decisions/magic-link-auth.md` — accepted decision; its **Rejected** section names "Sign in with Google" SSO specifically, with the reasons and the revisit trigger.
- `knowledge/constraints/external-users.md` — no corporate IdP (Google Workspace/Entra/Okta) to integrate with.
- `knowledge/constraints/solo-maintainer.md` — one person, few hours/week; minimize operational surface; "anything that can break at 3am is out."
- `knowledge/interviews/2026-07-08-auth-scope.md` — owner (Ivan): users are individuals not companies, ~zero auth maintenance budget, no passwords (liability).
- `specs/auth/spec.md` — AUTH-1 (magic-link login) and AUTH-2 (30-day sessions), both tracing back to that decision.

## 3. QUESTIONS

1. **What's the evidence of demand?** The decision's revisit trigger is "a significant user segment demands social login." Do we have support tickets, churn data, or signup drop-off pointing at the lack of Google login — or is this a hunch?
2. **What problem are we actually solving?** If it's signup friction, magic-link already removes passwords. Is Google login expected to convert better, and by how much — enough to justify the new surface?
3. **Who owns the ongoing cost?** Google OAuth means a Cloud console project, client secret rotation, consent-screen verification, and a new external dependency that can break. Given the solo-maintainer constraint, who maintains it when it breaks?
4. **Is this additive or a replacement?** Keep magic-link and add Google as an option (two auth paths to maintain), or migrate? Migration raises account-linking questions for existing magic-link users.
5. **Has the user base changed?** The "external freelancers, no IdP" constraint is dated 2026-07-08. If we're now targeting agencies/teams on Google Workspace, that's genuinely new evidence — and it should be captured as an interview/constraint update before the decision is reopened.

skipped: no design or code work — request was evaluate-and-propose, files untouched. Add when the PM answers Q1 with real demand data.