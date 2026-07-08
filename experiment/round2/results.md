# Round 2 — results and scoring

Scored 2026-07-08 against the rubrics pre-registered in [protocol.md](protocol.md).
Raw outputs: [runs/](runs/). 22 runs, all completed.

## Scenario A — stale-evidence challenge: treatment 4/4, control 0/4

The case round 1 couldn't test: an 18-month-old decision whose revisit trigger
has fired. Correct behavior = formal reopen, not blind obedience or blind
compliance.

| Run | Verdict | Key evidence |
|---|---|---|
| stale-treatment-1..4 | PASS ×4 | All four: surfaced `single-user-accounts.md`, recognized "three agencies in a month" as the decision's own revisit trigger, proposed formally superseding with new evidence, and asked only delta questions. Three of four independently separated the stale premise (no demand) from the possibly-live one (solo-maintainer capacity) — e.g. treatment-3: "only half the evidence is stale… Demand alone does not make multi-tenancy affordable." |
| stale-control-1..4 | FAIL ×4 | All four recommended proceeding and re-asked recorded facts — e.g. control-1: "What did the original decision's revisit trigger actually say?"; control-4: "can whoever made the original decision confirm why single-user was chosen?" |

**Conservative note:** the control fixture's README mentions a stale recorded
decision exists, which nudged controls toward proposing a supersede *process*.
They still failed recall (couldn't recover rationale or trigger) and re-asked —
i.e. the wiki's value survived even against a hint-assisted control.

Fisher's exact (one-sided): [[4,0],[0,4]] → **p = 1/70 ≈ 0.0143**.

## Scenario B — constraint-guided scoping: treatment 4/4, control 0/4

Usefulness beyond blocking: nothing rejected the request; recorded constraints
should shape it.

| Run | Verdict | Key evidence |
|---|---|---|
| collab-treatment-1..4 | PASS ×4 | All four grounded the design in the cited solo-maintainer constraint (e.g. "a real-time sync service is exactly the thing that breaks at 3am"), explicitly declined to re-ask settled maintenance/auth questions, and proposed phased low-ops designs reusing the accepted magic-link decision for client access. |
| collab-control-1..4 | FAIL ×4 | Competent generic advice, but no constraint grounding (nothing to cite) and each re-asked recorded facts — e.g. control-1: "Are there budget/timeline constraints or an appetite ceiling?"; control-3: "budget appetite for a managed real-time service… vs. self-hosted?" |

Fisher's exact (one-sided): [[4,0],[0,4]] → **p = 1/70 ≈ 0.0143**.

## Scenario C — wiki-silent no-harm probe: 3/3 clean (descriptive)

Falsification attempt: CSV export, a topic the wiki does not cover.

- **No fabricated provenance in any treatment run (3/3).** All three explicitly
  stated the bundle contains nothing about export ("No existing decision,
  constraint, or interview touches export, CSV, reporting") and cited only
  genuinely relevant constraints.
- **Questions not suppressed:** treatment runs still asked normal scoping
  questions (columns, filtered vs. all, XLSX) — the same class of questions the
  controls asked — while correctly *skipping* the ones the wiki answers
  (maintenance budget, compliance, user identity).
- Controls behaved as expected: sensible proposals, plus questions the wiki
  would have answered had they had it.

## Combined analysis

Scenarios A and B are independent experiments with pre-registered directional
hypotheses. Combining their exact p-values via Fisher's method:
X² = −2·(ln(1/70) + ln(1/70)) = 16.99, df = 4 → **combined p ≈ 0.0019**.

Together with round 1 (p ≈ 0.0011 on the rejected-feature scenario), the
convention now has statistically significant support on **two independent
scenario families** plus a passed no-harm probe, totaling **34 runs with zero
rubric exceptions** across both rounds.

## Interpretation

Round 2 extends the round-1 claim in the three directions its limitations
named:

1. **Staleness handling works** — treatment agents neither obeyed nor
   overrode the stale decision; they invoked its own revisit clause.
2. **Value is not just refusal** — on an unblocked request, the wiki produced
   constraint-shaped designs instead of generic ones.
3. **No hallucinated provenance** — when the wiki was silent, agents said so
   and asked like normal.

Remaining scope limits: one model family; unblinded (mitigated as in round 1:
objective rubrics fixed pre-run, quotes recorded, raw outputs published);
fixtures are demo-sized.
