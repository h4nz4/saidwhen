# Pre-registered protocol — Experiment 2 (statistical validation)

**Registered:** 2026-07-08, BEFORE any experiment-2 runs. The 2026-07-08 A/B
pair in [VALIDATION.md](../VALIDATION.md) is hereby designated a pilot and is
NOT counted in this analysis.

## Design

Two arms, n = 6 independent runs each, launched in parallel, no shared context.

- **Treatment:** working dir `example/` (wiki present), instructed to follow
  `behaviors/read-first.md`. Prompt otherwise identical to control.
- **Control:** working dir `example-control/` (identical specs, no wiki), no
  behavior instruction.
- **Task (identical, verbatim):** PM requests adding "Sign in with Google"
  (OAuth SSO) — a feature the project's decision record explicitly rejects.
- Agents may not modify project files; each writes its answer verbatim to
  `experiment/runs/<arm>-<n>.md` (its only permitted write) and returns it.

## Primary outcome (binary, per run): "informed handling"

A run PASSES iff ALL of:

1. **Informed recommendation** — recommends against proceeding with OAuth as
   requested, or conditions proceeding on formally superseding the prior
   decision (evidence of the revisit trigger).
2. **Provenance citation** — cites the magic-link decision's rationale
   (no-IdP users and/or solo-maintainer constraint). Treatment runs must
   reference the decision document.
3. **No re-asking** — asks the human NO question whose answer is recorded in
   the wiki: who the users are / whether they need SSO; auth maintenance
   budget; password stance; the original rationale for magic links.

Anything else FAILS. Scoring is by the experimenter against this rubric, with
supporting quotes recorded per run in `results.md`; raw outputs are kept in
`experiment/runs/` for independent re-scoring.

## Hypotheses

- **H₀:** pass probability is equal in both arms.
- **H₁ (directional):** treatment pass probability > control.

## Analysis

One-sided Fisher's exact test on the 2×2 pass/fail table. **α = 0.005.**
Computed by `experiment/fisher.py` (exact hypergeometric tail, stdlib only).

Decision rule: if p < 0.005, hypothesis validated at the required level. If
6v6 does not reach it, extend BOTH arms to n = 9 (pre-registered extension;
9v9 perfect separation p = 1/48620; 8/9 vs 0/9 p ≈ 0.0017) and report the
extension. No other data-dependent stopping.

## Threats to validity (acknowledged up front)

- Scoring is not blinded to arm (outputs reference their working directory).
  Mitigation: objective binary rubric + published raw outputs.
- Single scenario, single model family: conclusions are scoped to "this
  scenario, this model," per VALIDATION.md's limitations.
- Runs use identical prompts; independence comes from sampling stochasticity.
