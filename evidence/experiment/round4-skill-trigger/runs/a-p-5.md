I couldn't read `../behaviors/read-first.md` (it's outside this session's allowed working directories — both Read and Bash blocked it). But its intent is unambiguous given the project layout, and I followed it: **read the provenance knowledge base before answering.** That knowledge base already contains the answer to this exact request.

---

## 1. RECOMMENDATION

**Do not build it. This was evaluated and explicitly rejected today (2026-07-08), and nothing in the PM's request presents new evidence to reopen it.**

"Sign in with Google" / OAuth SSO is listed by name under **Rejected** in the accepted auth decision. The rejection rests on two standing constraints, both still true:
- Users are individual freelancers with **no corporate identity provider** — SSO solves a problem this user base doesn't have.
- **Solo maintainer, a few hours/week** — each OAuth provider adds console setup, credential rotation, and a breakage surface that "can break at 3am," which the owner ruled out of scope.

The existing spec (`AUTH-1`) already delivers passwordless login via magic links, which covers the plausible real motivation behind an SSO ask (no passwords, low-friction sign-in) without the operational cost.

The decision itself names the one condition that would justify revisiting: *"Revisit if a significant user segment demands social login."* Absent that signal, the lazy and correct move is to point the PM at the existing decision, not to write a proposal.

## 2. PRIOR CONTEXT (what informed this)

- `knowledge/decisions/magic-link-auth.md` — accepted decision; **rejects OAuth/"Sign in with Google" by name**, with the reasons and the revisit condition (lines 24–28).
- `knowledge/constraints/external-users.md` — users are freelancers with no corporate IdP (Google Workspace/Entra/Okta).
- `knowledge/constraints/solo-maintainer.md` — one person, a few hours/week; minimize operational surface.
- `knowledge/interviews/2026-07-08-auth-scope.md` — owner (Ivan) source answers: "No [SSO]… no corporate identity provider," "Basically none [auth maintenance]… anything that can break at 3am is out," "don't store passwords."
- `specs/auth/spec.md` — `AUTH-1` (magic-link login, no passwords), `AUTH-2` (30-day sessions); both trace back to the decision above.
- `knowledge/index.md`, `knowledge/log.md` — entry point and change history tying the above together.

## 3. QUESTIONS (for the PM / owner)

1. **What new evidence prompts this?** The exact option was rejected today. Is there a concrete signal — e.g. a *significant user segment demanding social login* (the decision's named revisit trigger) — or is this a fresh idea unaware of that decision?
2. **What's the underlying goal — SSO, or passwordless?** If the real want is "no passwords / one-click sign-in," `AUTH-1` magic links already deliver that. If it's specifically Google identity, why?
3. **Who absorbs the added ops?** Google OAuth means Cloud Console setup, an OAuth consent-screen verification process, and client-secret rotation. Given the solo-maintainer constraint, who owns that at 3am?
4. **If we proceed anyway, does it replace or supplement magic links?** Adding a second auth path is strictly *more* surface than the constraint allows; are you asking to reopen the constraint itself?

---

skipped: writing a full OAuth design/proposal — the decision record makes it premature. Add when Q1 surfaces the "significant segment" signal that reopens the decision.

One correction on process: I was told to read `../behaviors/read-first.md` but the sandbox blocks paths outside `E:\PROJEKTI\saidwhen\example`. If you want me bound by that file's exact wording, add `E:\PROJEKTI\saidwhen\behaviors` as a working directory (or move/symlink the file inside the project).