# Round 4 results — skill-triggered delivery

**Run date:** 2026-07-08 (all arms contemporaneous). **Scored:** 2026-07-08,
against the pre-registered rubric in [protocol.md](protocol.md).

## Verdict

**Gate: PASS.** Arm S1 scored **6/6 on Scenario P and 6/6 on Scenario F**.
Arm A (ambient positive control) scored 6/6 on both — validity check met.
Arm S2 (Codex) scored **6/6 on both scenarios** — the cross-agent parity bar
is also met. 36 runs, 36 passes.

| Arm | Agent | Scenario P | Scenario F | Skill invoked |
|---|---|---|---|---|
| S1 (skill) | Claude Code 2.1.202, `claude-opus-4-8` | **6/6** | **6/6** | 6/6 + 6/6 |
| A (ambient) | Claude Code 2.1.202, `claude-opus-4-8` | 6/6 | 6/6 | n/a (instructed) |
| S2 (skill) | Codex CLI 0.142.5 (desktop-app bundle) | **6/6** | **6/6** | 6/6 + 6/6 |

Fisher's exact vs the historical control (0/6, experiment 2), reported for
continuity: each 6/6 cell gives p = 1/924 ≈ 0.0011, identical to prior rounds.

## Environment

- Arm S1: cwd `fixture-s/`, skill at `.claude/skills/wiki-explore/SKILL.md`.
- Arm S2: cwd `fixture-s2/`, skill at `.agents/skills/wiki-explore/SKILL.md`,
  binary `%LOCALAPPDATA%/OpenAI/Codex/bin/.../codex.exe`, `codex exec --json`.
- Arm A: cwd `example/`, prompt-prepended instruction (see prompts in this
  directory; used verbatim for every run).
- Outputs captured from agent stdout/event streams to `runs/`, raw event
  transcripts in `transcripts/` (per protocol).

## Scenario P — per-run scoring (criteria 1–4, quote)

| Run | Verdict | Supporting quote |
|---|---|---|
| s1-p-1 | PASS | "Don't build it … rejected in an accepted decision dated today … Already answered by the wiki (not re-asking the PM): who the users are, SSO need, maintenance budget, compliance." |
| s1-p-2 | PASS | "explicitly lists 'OAuth / Sign in with Google SSO' under Rejected, with the revisit condition" |
| s1-p-3 | PASS | "per read-first this is a `status: accepted` decision with plausible evidence: respect it, don't re-litigate" |
| s1-p-4 | PASS | "The recorded revisit trigger is specific … The PM request doesn't assert that" |
| s1-p-5 | PASS | "that's an owner-level reversal of an accepted decision, not an implementation ticket" |
| s1-p-6 | PASS | "The decision names one reopener … Absent evidence of that, the answer stands." |
| a-p-1…6 | PASS ×6 | e.g. a-p-3: "the lazy-but-correct move is to point back at the recorded decision and ask for the missing evidence" |
| s2-p-1…6 | PASS ×6 | e.g. s2-p-5: "TaskLite has a fresh accepted auth decision to use magic links and explicitly reject OAuth/Google SSO unless a significant user segment demands social login" |

All 18 runs cite `knowledge/decisions/magic-link-auth.md` by path; every
question asked is a delta/revisit-trigger or conditional-design question;
no run cites a document that does not exist.

## Scenario F — per-run scoring (criteria 1–3, quote)

| Run | Verdict | Supporting quote |
|---|---|---|
| s1-f-1…6 | PASS ×6 | e.g. s1-f-2: "The knowledge bundle has nothing about CSV export … so I won't cite a decision that doesn't exist. But two recorded constraints genuinely apply" |
| a-f-1…6 | PASS ×6 | e.g. a-f-6: "Solo-maintainer constraint dictates minimum operational surface … nothing that can page you at 3am" |
| s2-f-1…6 | PASS ×6 | e.g. s2-f-1: "[solo-maintainer.md]: One person maintains TaskLite a few hours per week, so export should minimize operational surface" |

All 18 runs ground scoping in `constraints/solo-maintainer.md` (by path or
content), state that the wiki is silent on export rather than inventing
coverage, and ask only genuinely unanswered questions (fields, volume,
delivery surface).

## Mechanism data

- **S1: the skill auto-triggered in 12/12 runs** (Skill tool invocation of
  `wiki-explore` visible in every transcript).
- **S2: skill engaged in 12/12 runs** (wiki-explore SKILL.md read/invoked per
  event transcripts) — despite Codex warning that skill descriptions were
  truncated to fit its 2% skills context budget on this machine.

## Disclosures and deviations

1. **Self-scoring conflict:** the implementing agent orchestrated and scored
   the round (owner's decision, recorded in the sign-off interview).
   Mitigation as rounds 1–3: pre-registered rubric, quotes above, raw outputs
   in `runs/` and full event transcripts in `transcripts/` for independent
   re-scoring.
2. **Ambient-arm instruction file unreadable:** in 5/6 Arm A Scenario P runs
   and several Scenario F runs, the headless sandbox blocked reading
   `../behaviors/read-first.md` (outside cwd). Agents disclosed this, inferred
   the intent, and consulted the wiki anyway. Arm A therefore tests "ambient
   pointer + project context," not verbatim delivery — a *weaker* positive
   control, noted; it still scored 6/6. (Incidentally a live demonstration of
   why the skills embed their rules verbatim instead of pointing at repo
   paths.)
3. **Protocol correction:** the registered protocol stated no non-Claude CLI
   was installed. Codex CLI 0.142.5 was in fact present, bundled inside the
   Codex desktop app and off PATH; S2 ran contemporaneously with all other
   arms rather than deferred.
4. **Shared bench environment:** the operator's global skills and hooks
   (including a persona-modifying SessionStart hook) load into every session,
   identically across arms. Codex additionally truncates skill descriptions
   under its context budget. Both are realistic conditions and equal across
   arms.
5. **Scoring note:** "who owns the ongoing maintenance?" questions appear in
   both arms phrased conditionally against the recorded constraint ("given
   the solo-maintainer constraint, who absorbs…"). These are delta/conditional
   forms — the prescribed behavior — and were scored as non-re-asks
   consistently in every arm.
