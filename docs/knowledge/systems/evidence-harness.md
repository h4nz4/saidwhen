---
type: Component
title: Evidence harness
description: How claims get validated — pre-registered rounds, isolated worktrees, headless agent runs, published raw outputs.
timestamp: 2026-07-08T20:30:00Z
tags: [architecture, evidence]
---

# Evidence harness

Every quantitative claim in the README traces to a round under
`evidence/experiment/`: a pre-registered `protocol.md` (rubric, arms, and
analysis fixed before any run, owner sign-off recorded in this wiki),
headless agent runs (`claude -p` / `codex exec`, fresh session per prompt,
arms isolated in separate git worktrees so neither can observe the other),
and a `results.md` scoring every run against the rubric with quotes —
plus raw outputs and full event transcripts for independent re-scoring.

**Why this much ceremony:** the implementing agent both runs and scores
the rounds (recorded owner decision) — pre-registration and published raw
data are what keep self-scoring honest. Amendments are legal only before
the first run, and deviations are disclosed in results, including
unflattering ones (round 6 shipped an analysis-script bug fix, disclosed).

Execution cost is bounded by the owner's recorded directive:
[validation runs stay lean and cheap](../constraints/lean-validation-runs.md).
