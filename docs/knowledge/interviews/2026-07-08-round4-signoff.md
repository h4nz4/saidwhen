---
type: Interview
title: Round-4 protocol sign-off with Ivan
description: Q&A that fixed the round-4 (skill-triggered delivery) gate rule, cohorts, execution, and control arm before registration.
timestamp: 2026-07-08T03:30:00Z
tags: [evidence, distribution]
---

# Round-4 protocol sign-off — 2026-07-08, with Ivan (owner)

Amends the draft gate in
[validation-gates-skills-first](../decisions/validation-gates-skills-first.md).

**Q: Sign off the drafted gate rule (Arm S 6/6; n=9 extension at 5/6, gate
≥8/9; snippet fallback on failure)?**
A: Stricter — keep that gate and add round-3-style probes (fabrication /
uncovered-topic checks) to the round.

**Q: Which agent(s) run Arm S?**
A: Claude Code plus one non-Claude agent. (Environment note, discovered
after the answer: no non-Claude Agent-Skills CLI is currently installed on
the bench machine — the second cohort needs an install before it can run.)

**Q: Who executes the runs?**
A: The implementing agent orchestrates headless runs AND scores them.
Conflict acknowledged: scoring one's own gate — disclosed in the protocol
and results, with raw outputs published for independent re-scoring, same
mitigation as the unblinded scoring in rounds 1–3.

**Q: Arm A (ambient positive control) — re-run fresh or reuse historical?**
A: Re-run fresh alongside Arm S, so both arms share model version and date.
