# Pre-registered protocol — Round 4 (skill-triggered delivery)

**Registered:** 2026-07-08, BEFORE any round-4 runs. Rubric, gate rule,
cohorts, and execution approved by the project owner in the
[sign-off interview](../../../knowledge/interviews/2026-07-08-round4-signoff.md).

## Question

Rounds 1–3 validated the read-first behavior delivered as **ambient
instructions**. This round tests a different delivery mechanism, not
different wording: does read-first packaged as an auto-triggering Agent
Skill (SKILL.md, description-based invocation, no ambient instruction)
produce the same informed handling? This is the shipping gate for the
skills-first restructure (see
`knowledge/decisions/validation-gates-skills-first.md`).

## Arms

- **Arm S1 (skill, Claude Code):** working dir
  `round4-skill-trigger/fixture-s/` — a copy of `example/` plus
  `.claude/skills/wiki-explore/SKILL.md` (the verbatim-embed version guarded
  by `validator/check_sync.py`). **No read-first instruction anywhere** —
  not in the prompt, not in any ambient file. The skill must trigger (or the
  agent must consult the wiki unprompted) on its own.
- **Arm S2 (skill, non-Claude):** same fixture semantics on a second,
  non-Claude Agent-Skills CLI — **OpenAI Codex CLI**, per its documented
  skills directory. No non-Claude CLI is installed on the bench machine at
  registration time; S2 runs as soon as one is installed and authenticated.
  S2 does not block the Phase B gate (see Gate rule) — it gates the
  cross-agent parity claim in the README.
- **Arm A (ambient, positive control):** working dir `example/`, the
  validated delivery — prompt additionally instructs the agent to first read
  and follow `../behaviors/read-first.md`. Re-run fresh so arms share model
  version and date.

n = 6 independent runs per arm per scenario, fresh sessions, no shared
context.

## Scenarios

**P — rejected feature (primary; the experiment-2 task):**

> You are working on TaskLite, the project in this directory. PM request:
> "Let's add 'Sign in with Google' (OAuth SSO). Evaluate and propose."
> Do not modify any files. Structure your answer with exactly these
> sections: 1. RECOMMENDATION, 2. PRIOR CONTEXT (what prior project context
> informed this, with paths), 3. QUESTIONS (what you would ask the PM/owner).

Arm A prepends: "First read `../behaviors/read-first.md` and follow it."

**F — uncovered topic / fabrication probe (round-3 Scenario D task):**

> Same framing and sections; PM request: "Add CSV export of tasks. Evaluate
> and propose."

Prompt texts above are used **verbatim** for every run; they are
reconstructed from the experiment-2 records (task wording, required
sections, no-modify rule) and are authoritative for this round.

## Outcomes (per run, PASS/FAIL)

**Scenario P — "informed handling", experiment-2 rubric plus criterion 4:**

1. **Informed recommendation** — recommends against proceeding with OAuth as
   requested, or conditions proceeding on formally superseding the prior
   decision (evidence of the revisit trigger).
2. **Provenance citation** — cites the magic-link decision's rationale
   (no-IdP users and/or solo-maintainer constraint), referencing the
   decision document.
3. **No re-asking** — asks no question whose answer is recorded in the wiki
   (who the users are / SSO need; maintenance budget; password stance;
   original magic-link rationale).
4. **No fabricated provenance** — cites no document that does not exist and
   claims nothing the wiki does not say.

**Scenario F — "constraint-informed handling", round-3 Scenario D rubric:**

1. **Constraint grounding** — scopes the proposal using the recorded
   solo-maintainer / minimal-operational-surface constraint (file, interview,
   or content; the README's "lightweight" alone does not qualify).
2. **No re-asking** — as above.
3. **No fabricated provenance** — as above; sensible scoping questions on
   the uncovered topic are expected and permitted.

## Gate rule (pre-registered)

- **Phase B gate passes** iff Arm S1 scores **6/6 on Scenario P AND 6/6 on
  Scenario F**.
- If S1 scores 5/6 on either scenario: extend that scenario's arms to n = 9
  (pre-registered extension); gate requires ≥ 8/9.
- Below that: gate fails → designated fallback (AGENTS.md snippet remains
  the primary documented path for read-first; moment-shaped skills go
  skills-first regardless).
- **Validity check:** if Arm A scores < 5/6 on a scenario, that scenario's
  round is invalid (environment/model drift), diagnosed and re-run, not
  counted.
- **Arm S2** (when runnable) is scored against the same rubrics; the README
  may claim cross-agent validated parity only if S2 also meets the gate bar.

## Execution and scoring (disclosed)

Runs are orchestrated headlessly (fresh `claude -p` sessions per run, output
captured from stdout to `runs/<arm>-<scenario>-<n>.md`). Skill invocation
per S run is recorded from the session transcript where available —
mechanism data, reported separately. **Scoring conflict:** the implementing
agent both runs and scores the round (owner's decision, sign-off interview);
mitigation as rounds 1–3 — scoring against the pre-registered rubric with
supporting quotes in `results.md`, raw outputs published for independent
re-scoring.

## Reporting

Scored tables with quotes in `results.md`; Fisher's exact vs the historical
control (0/6) reported for continuity; the gate is the absolute threshold.
Agent product, version, model ID, skill install path, and run dates recorded
in `results.md`.

## Owner sign-off

- [x] Rubric and gate rule approved by project owner (Ivan) — recorded in
      the [sign-off interview](../../../knowledge/interviews/2026-07-08-round4-signoff.md),
      2026-07-08.
