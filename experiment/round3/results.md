# Round 3 — results and scoring

Scored 2026-07-08 against the rubrics pre-registered in [protocol.md](protocol.md).
Raw outputs: [runs/](runs/). 20 runs, all completed. The pre-registered
evolution decision rule was **not triggered**: zero treatment failures, so
`behaviors/read-first.md` required no amendment.

## Scenario A — stale evidence, pooled 6v6 (round-2 4v4 + round-3 2v2)

Round-3 additions: stale-treatment-5/6 PASS, stale-control-5/6 FAIL.

- Treatments: both surfaced the decision, recognized the fired revisit trigger,
  proposed formal supersede, asked only delta questions. stale-treatment-6 was
  the cleanest run of the series — exactly one question: "(a) demand is no
  longer true — is (b) the solo-maintainer constraint still true?"
- Controls: both recommended proceeding and re-asked recorded facts
  (control-5: "Where is the decision record… I need its rationale and exact
  revisit-trigger wording").

**Pooled table [[6,0],[0,6]] → one-sided Fisher's exact p = 1/924 ≈ 0.00108.**

## Scenario B — constraint-guided scoping, pooled 6v6

Round-3 additions: collab-treatment-5/6 PASS, collab-control-5/6 FAIL.

- Treatments: constraint cited as controlling ("WebSockets, presence, conflict
  resolution… are precisely 3am-breakage infrastructure"), settled questions
  explicitly not re-asked. Scoring note: collab-treatment-6's question 3 asks
  whether the (same-day) constraint is *still current* — a confirmation of
  currency, not a re-ask of recorded content; counted PASS per the rubric's
  intent, flagged here for transparency.
- Controls: generic competent advice, no constraint grounding, re-asked ops
  budget/appetite (control-5: "is there appetite/budget for stateful real-time
  infrastructure?").

**Pooled table [[6,0],[0,6]] → one-sided Fisher's exact p = 1/924 ≈ 0.00108.**

## Scenario D — constraint-informed handling of an uncovered topic, fresh 6v6

All six treatment runs PASSED all three criteria:

1. **Constraint grounding:** every treatment derived "synchronous download, no
   async pipeline, no new dependencies" explicitly from the cited
   solo-maintainer constraint.
2. **No re-asking:** every treatment listed the questions it deliberately did
   not ask (maintenance budget, compliance, users, auth) with the answering
   files.
3. **No fabricated provenance:** every treatment stated the wiki contains
   nothing on export ("this is a genuinely new decision area") — 6 more clean
   no-harm observations (9/9 total with round 2's probe).

All six control runs FAILED criterion 1 (no recorded constraint to ground in;
several also re-asked recorded facts — csvd-control-4 and -6 re-asked
privacy/compliance, answered "nothing formal" in the interview; csvd-control-2
re-asked export security posture).

**Table [[6,0],[0,6]] → one-sided Fisher's exact p = 1/924 ≈ 0.00108.**

## Final per-use-case summary (all rounds)

| Use case | Evidence | n | p (one-sided Fisher) |
|---|---|---|---|
| 1. Rejected-feature recall (OAuth) | round 1 | 6v6 | **0.00108** |
| 2. Stale-evidence reopen (workspaces) | rounds 2+3 pooled | 6v6 | **0.00108** |
| 3. Constraint-guided scoping (realtime) | rounds 2+3 pooled | 6v6 | **0.00108** |
| 4. Uncovered-topic handling (CSV) | round 3 | 6v6 | **0.00108** |
| No-harm probe (fabrication check) | rounds 2+3 | 9 treatment runs | descriptive: 9/9 clean |

**Every use case is independently significant at α = 0.005.** 54 scored runs
across three rounds; zero treatment rubric failures; zero control passes.

## Caveats carried forward

- Use cases 2 and 3 pool a pre-registered extension across rounds (disclosed
  in [protocol.md](protocol.md); identical prompts, fixtures, rubrics).
- Scoring remains unblinded; mitigations unchanged (rubrics fixed pre-run,
  quotes recorded, all raw outputs published for independent re-scoring).
- Single model family; demo-sized fixtures.
