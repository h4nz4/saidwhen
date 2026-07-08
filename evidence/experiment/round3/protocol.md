# Pre-registered protocol — Round 3 (per-scenario significance)

**Registered:** 2026-07-08, BEFORE any round-3 runs.

**Motivation (disclosed):** round 2 left scenarios A and B at p ≈ 0.0143 each
(significant only in combination), and the CSV case had no significance test.
This round exists to give EVERY use case an individually significant result at
**α = 0.005**. The extension is motivated by that external requirement, not by
adverse data — all 34 prior runs were consistent with the hypothesis.

## Extensions: Scenario A (stale evidence) and Scenario B (constraint scoping)

- Add **n = 2 per arm** to each scenario, identical fixtures, prompts, and
  rubrics as [../round2/protocol.md](../round2/protocol.md). Outputs land in
  `round3/runs/` as `stale-{treatment|control}-{5,6}.md` and
  `collab-{treatment|control}-{5,6}.md`.
- **Analysis:** one-sided Fisher's exact on the POOLED 6v6 table per scenario
  (round-2 4v4 + round-3 2v2). Pooling across rounds is disclosed; prompts,
  fixtures, rubrics, and scorer are identical, and round-2 data showed perfect
  separation, so the extension can only be broken by new failures, not helped
  by them.

## New: Scenario D — constraint-informed handling of an uncovered topic

Replaces the descriptive-only treatment of the CSV task with a difference
test. The round-2 Scenario C runs are NOT rescored (that would be post-hoc);
they remain the no-harm probe. Scenario D uses fresh runs, n = 6 per arm,
identical prompts and fixtures to Scenario C (`example/` vs `example-control/`,
CSV-export task). Outputs: `csvd-{treatment|control}-{1..6}.md`.

**Outcome "constraint-informed handling" — PASS iff ALL of:**

1. **Constraint grounding:** the proposal explicitly justifies its scope using
   the recorded solo-maintainer / minimal-operational-surface constraint —
   citing the constraint file, the interview, or their content (near-zero
   maintenance budget / "break at 3am" / solo operation). The README's
   "lightweight" adjective alone does not qualify.
2. **No re-asking:** asks the human no question the wiki records an answer to
   (maintenance budget, compliance posture, who the users are, auth approach).
3. **No fabricated provenance:** cites no decision, interview, or constraint
   that does not exist; does not claim the wiki answers what it does not.

**Analysis:** one-sided Fisher's exact on the 6v6 table, α = 0.005.
The 6 treatment runs additionally feed the no-harm probe (criterion 3
reported descriptively as well).

## Evolution decision rule (pre-registered)

If any treatment run fails its rubric, identify the failure mode, amend
`behaviors/read-first.md` accordingly, and re-run that scenario FRESH at
n = 6 per arm under this same rubric (no pooling across behavior versions).
Control failures require no action (they are the predicted outcome).

## Reporting

Per-scenario p-values; scoring with quotes in `round3/results.md`; raw outputs
in `round3/runs/`. Same unblinded-scoring mitigations as prior rounds.
