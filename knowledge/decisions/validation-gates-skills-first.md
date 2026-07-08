---
type: Decision
title: Validation gates the skills-first restructure
description: The skills-first restructure does not ship until a pre-registered A/B round shows skill-triggered read-first performs like the validated ambient-instruction delivery.
status: accepted
timestamp: 2026-07-08T02:30:00Z
tags: [distribution, evidence]
---

# Validation gates the skills-first restructure

The experiments in `evidence/` validated read-first delivered as **ambient
instructions**. A read-first *skill* loads conditionally — the agent must
decide to invoke it before asking a redundant question, which is exactly the
moment it doesn't know it needs it. Until a pre-registered A/B round (same
protocol as rounds 1–3) shows skill-triggered read-first matching the
validated delivery, the skills-first restructure of
[skills-first-distribution](skills-first-distribution.md) does not ship.
Every commit keeps the "measurably works" claim tied to what was actually
tested.

## Evidence

- [Interview 2026-07-08 with Ivan](../interviews/2026-07-08-distribution-strategy.md):
  chose "validate first" over shipping with a caveat.

## Rejected

- **Ship, validate after** — rejected: README claims would outrun the
  evidence, the one thing this project exists to prevent.
- **Snippet stays primary for read-first** (avoiding the test entirely) —
  rejected as the default, but it is the designated fallback: if the
  validation round fails or proves repeatedly infeasible, read-first remains
  snippet-delivered and only the moment-shaped skills go skills-first.
