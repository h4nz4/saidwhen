# Pre-registered protocol — Round 2 (scenarios 3–5)

**Registered:** 2026-07-08, BEFORE any round-2 runs. Extends the validated
round-1 result (see [../protocol.md](../protocol.md), [../results.md](../results.md))
to the three cases round 1 could not test. Raw outputs land in
`experiment/round2/runs/`; each agent may write only its own answer file.

## Scenario A — stale-evidence challenge (n = 4 per arm)

The pilot's untested case: the decision is **18 months old and its revisit
trigger has fired**. The correct behavior is neither blind obedience nor blind
compliance with the PM — it is a formal reopen.

- **Fixture:** `example-stale/` — decision `single-user-accounts.md`
  (accepted 2025-01-15) rejects team workspaces with revisit trigger
  "if agencies or teams repeatedly request shared use."
  Control: `example-stale-control/` (identical specs, no wiki).
- **Task (both arms, verbatim):** PM reports three design agencies asked this
  month to use TaskLite with their teams; add multi-user team workspaces.
- **Outcome "informed revisit" — PASS iff ALL of:**
  1. Surfaces the prior single-user decision and its rationale.
  2. Neither flatly refuses by treating the 2025 decision as final, NOR
     proceeds as if no prior decision existed: recognizes the agency demand as
     the decision's own revisit trigger and proposes formally superseding /
     reopening the decision (new evidence recorded, decision superseded, spec
     amended) before or as part of building.
  3. Re-asks no recorded fact (why single-user was chosen, maintenance budget).

## Scenario B — constraint-guided scoping (n = 4 per arm)

Usefulness beyond blocking: the request contradicts nothing, but recorded
constraints should shape the proposal.

- **Fixture:** `example/` vs `example-control/` (as round 1).
- **Task (both arms, verbatim):** PM asks for real-time collaborative editing
  so freelancers can work live with their clients.
- **Outcome "constraint-aware proposal" — PASS iff ALL of:**
  1. The recommendation explicitly grounds its scoping in the recorded
     solo-maintainer / minimal-operational-surface constraint (cited by file
     or by its interview evidence).
  2. Re-asks no recorded fact (maintenance budget, who the users are).

## Scenario C — wiki-silent no-harm probe (n = 3 per arm, descriptive)

Falsification attempt: a topic the wiki does not cover. A provenance system
that fabricates provenance is worse than none.

- **Fixture:** `example/` vs `example-control/`.
- **Task (both arms, verbatim):** PM asks for CSV export of tasks.
- **Checks (descriptive, no significance test):**
  1. **No fabricated provenance:** the treatment agent must not cite a
     decision/interview about CSV export or claim the wiki answers questions
     it does not. (Citing genuinely relevant recorded constraints is fine.)
  2. Both arms should ask sensible scoping questions — the wiki must not
     suppress legitimate questions on uncovered topics.

## Analysis

- Scenarios A and B: one-sided Fisher's exact per scenario (α reported, not
  gated: 4v4 perfect separation gives p = 1/70 ≈ 0.0143). Combined evidence
  across A and B (independent scenarios) via Fisher's method; if both are
  perfect separations, combined p ≈ 0.0019.
- Scenario C: descriptive pass/fail table only.
- Scoring: experimenter, unblinded, against these rubrics, quotes recorded,
  raw outputs published — same mitigations as round 1.
- No extensions or data-dependent stopping; whatever the counts are, they are
  reported.
