# Validation: does the provenance convention actually change agent behavior?

**Date:** 2026-07-08 · **Method:** A/B experiments with independent agents on an identical task.
**Headline result:** treatment 6/6 vs control 0/6 on the pre-registered outcome;
one-sided Fisher's exact **p ≈ 0.0011 < α = 0.005** ([experiment/results.md](experiment/results.md)).

This file documents the pilot (n=1 per arm) first, then the pre-registered
statistical replication (n=6 per arm).

## Hypothesis

An agent given (a) an OKF knowledge bundle following [CONVENTION.md](CONVENTION.md)
and (b) the [read-first behavior](behaviors/read-first.md) will, when asked to
implement something that was previously rejected:

- **H1 (recall):** find and cite the prior decision and its human evidence unprompted;
- **H2 (no re-asking):** not re-ask questions the wiki already answers;
- **H3 (staleness delta):** ask only the delta question ("is the evidence still true?") instead of re-litigating or blindly obeying.

A control agent without the wiki is expected to blindly propose the rejected
option and/or re-interview the human.

## Setup

| | Treatment | Control |
|---|---|---|
| Working dir | [example/](example/) | [example-control/](example-control/) |
| Specs | identical (magic-link auth) | identical, minus `([why](...))` links |
| `knowledge/` bundle | present (6 docs, validates OK) | absent |
| Behavior instruction | read-first.md | none |
| Task (identical) | *PM: "Let's add 'Sign in with Google' (OAuth SSO). Evaluate and propose."* | same |

Both agents: same model, same "do not modify files" rule, same required output
sections (recommendation / prior context / questions). Run in parallel.

## Results

| Criterion | Treatment | Control |
|---|---|---|
| Recommendation | **Do not proceed** — cited the accepted decision, its `## Rejected` entry naming Google SSO, and the revisit trigger | **Proceed** (via spec amendment) toward the previously rejected option; proposed OAuth requirements, account-linking design, and a "generic OIDC provider abstraction" |
| H1: cited provenance | ✅ decision + interview + both constraints, all with paths | — (nothing to find; noted the gap) |
| H2: re-asked answered questions | ✅ zero — explicitly listed the three questions it *refused* to re-ask | ❌ 5 questions, including *"do you recall the original rationale for magic-link-only?"* and *"add or replace?"* — both answered in the wiki it didn't have |
| H3: delta question only | ✅ exactly one: "decided 2026-07-08 because no IdP + solo maintainer — has the revisit trigger (user demand) actually fired?" | ❌ n/a — re-interviewed from scratch |
| Cost | ~46k tokens, 7 tool calls | ~45k tokens, 4 tool calls |

Near-identical cost, opposite outcomes. The control agent wasn't dumb — its
OAuth plan was competent. It was **uninformed**: it confidently planned a
feature the project owner rejected that same morning, and put the burden of
remembering *why* back on the human.

## Experiment 2 — pre-registered statistical replication

The pilot above established the mechanism; experiment 2 established reliability.
Protocol (outcome rubric, n, test, α) was registered in
[experiment/protocol.md](experiment/protocol.md) **before** any runs; the pilot
is excluded from the analysis.

- **Design:** 6 treatment runs (wiki + read-first behavior) vs 6 control runs
  (no wiki), fresh independent agents, identical task, run in parallel.
- **Outcome ("informed handling"):** recommends against the rejected feature
  (or conditions it on formally superseding the decision) AND cites the
  decision's rationale AND re-asks no wiki-answered question.
- **Result:** treatment **6/6 pass**, control **0/6 pass**. Every control run
  recommended proceeding toward the rejected feature and re-asked the recorded
  rationale ("Why was magic-link-only chosen originally?").
- **Test:** one-sided Fisher's exact on [[6,0],[0,6]]:
  **p = 1/924 ≈ 0.00108 < α = 0.005**. H₀ rejected at the pre-registered level.
- Per-run scoring with quotes: [experiment/results.md](experiment/results.md).
  Raw outputs: [experiment/runs/](experiment/runs/).

## Round 2 — three new scenarios (pre-registered)

Round 2 targeted the three gaps round 1 admitted, with rubrics and analysis
pre-registered in [experiment/round2/protocol.md](experiment/round2/protocol.md)
before any runs. Full scoring: [experiment/round2/results.md](experiment/round2/results.md).

| Scenario | What it tests | Result |
|---|---|---|
| A: Stale evidence | Decision 18 months old, revisit trigger fired — reopen formally, don't obey or override blindly | Treatment 4/4 vs control 0/4 (p ≈ 0.014) |
| B: Constraint-guided scoping | Unblocked request — do recorded constraints shape the proposal? | Treatment 4/4 vs control 0/4 (p ≈ 0.014) |
| C: Wiki-silent probe | Uncovered topic — does the agent fabricate provenance? | 3/3 clean, no fabricated citations, questions not suppressed |

Combined evidence across A and B (Fisher's method): **p ≈ 0.0019**.

## Round 3 — every use case individually significant (pre-registered)

Round 3 ([experiment/round3/protocol.md](experiment/round3/protocol.md))
extended scenarios A and B to 6v6 (disclosed pre-registered extension) and
promoted the CSV case to a proper 6v6 difference test (Scenario D,
"constraint-informed handling"). Full scoring:
[experiment/round3/results.md](experiment/round3/results.md).

| Use case | n | p (one-sided Fisher) |
|---|---|---|
| Rejected-feature recall (round 1) | 6v6 | **0.00108** |
| Stale-evidence reopen (rounds 2+3) | 6v6 | **0.00108** |
| Constraint-guided scoping (rounds 2+3) | 6v6 | **0.00108** |
| Uncovered-topic handling (round 3) | 6v6 | **0.00108** |
| No-harm fabrication probe (rounds 2+3) | 9 runs | descriptive: 9/9 clean |

## Verdict

**Hypothesis validated: every use case independently significant at
α = 0.005.** 54 scored runs across three pre-registered rounds; zero treatment
rubric failures; zero control passes. The pre-registered behavior-evolution
rule was never triggered — `behaviors/read-first.md` needed no amendment.

## Limitations (honest ones)

- **Single model family.** Round 2 closed the single-scenario gap (stale
  evidence, constraint-guided scoping, wiki-silent all tested); other models
  and larger, older wikis remain untested.
- **Unblinded scoring.** Outputs reveal their arm, so the experimenter-scored
  rubric could bias judgments. Mitigations: binary objective criteria fixed
  before the runs, quotes recorded per run, and raw outputs published for
  independent re-scoring.
- **Fresh timestamps:** the decision was hours old, making "respect it" easy.
  The interesting H3 case — evidence old enough to genuinely challenge — was
  only exercised rhetorically (the agent asked about the revisit trigger).
- **Demo-sized wiki** (6 documents). Read-first is trivially cheap here; a
  500-concept bundle needs the `index.md` progressive-disclosure discipline to
  actually hold.
- The control's README still *mentioned* a `knowledge/` directory (it noticed
  the gap). If anything this strengthens the result: knowing provenance should
  exist doesn't help when the files aren't there.

## Reproduce

1. `python scripts/validate.py example/knowledge` → expect `OK`.
2. Give one agent the treatment prompt (workdir `example/`, follow
   `behaviors/read-first.md`) and one the control prompt (workdir
   `example-control/`), task: *"add Sign in with Google — evaluate and propose."*
3. Score against H1–H3.
