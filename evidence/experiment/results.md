# Experiment 2 — results and scoring

Scored 2026-07-08 against the rubric pre-registered in [protocol.md](protocol.md).
Raw outputs: [runs/](runs/). Rubric: PASS requires (1) informed recommendation,
(2) provenance citation, (3) no re-asking of wiki-answered questions.

## Treatment arm (wiki + read-first behavior) — 6/6 PASS

| Run | Verdict | Key evidence (quotes from the run file) |
|---|---|---|
| [treatment-1](runs/treatment-1.md) | PASS | "Do not proceed with Google OAuth SSO as requested — it directly contradicts an accepted, currently-valid project decision." Cites decision + both constraints + interview. Sole question: "do we now have concrete evidence… that a significant user segment is demanding 'Sign in with Google'?" |
| [treatment-2](runs/treatment-2.md) | PASS | "Do not implement 'Sign in with Google' right now. This exact option was… explicitly rejected." Explicitly lists wiki-answered questions it will not re-ask. Delta question only. |
| [treatment-3](runs/treatment-3.md) | PASS | "Do not implement Google OAuth SSO at this time." Cites decision, constraints, interview quote ("break at 3am"). One delta question. |
| [treatment-4](runs/treatment-4.md) | PASS | "Do not implement Google OAuth SSO at this time." Conditions any reopening on revisit-trigger evidence; notes questions "therefore not asked." |
| [treatment-5](runs/treatment-5.md) | PASS | "Default: decline the request, citing knowledge/decisions/magic-link-auth.md, unless the PM can point to new evidence that satisfies the revisit clause." Delta question only. |
| [treatment-6](runs/treatment-6.md) | PASS | "Do not implement 'Sign in with Google' now." Cites decision + constraints; explicitly lists not-re-asked questions; delta question with quantification ask. |

All six treatment runs independently discovered the decision via `knowledge/index.md`
(none were told it existed), cited the no-IdP and solo-maintainer rationale, and
asked only the pre-registered "delta question."

## Control arm (no wiki) — 0/6 PASS

| Run | Verdict | Key evidence (quotes from the run file) |
|---|---|---|
| [control-1](runs/control-1.md) | FAIL | Recommends proceeding via spec amendment. Re-asks: "Why was magic-link-only chosen originally?" (recorded in the wiki it lacks). |
| [control-2](runs/control-2.md) | FAIL | Path to proceed after spec amendment; no supersede-on-evidence condition. Re-asks: "Do you know the original rationale for magic-link-only auth…?" |
| [control-3](runs/control-3.md) | FAIL | "Proceed with caution." Re-asks: "Was magic-link-only a deliberate decision…?" plus provider-scope question answered by constraints. |
| [control-4](runs/control-4.md) | FAIL | "Proceed, but as a spec-level change first." Re-asks: "Why was magic-link chosen as the *only* auth method…?" |
| [control-5](runs/control-5.md) | FAIL | "Proceed, but as a spec change first." Re-asks: "What was the original rationale for AUTH-1's magic-link-only decision?" |
| [control-6](runs/control-6.md) | FAIL | "Proceed, but as an additive auth method." Re-asks: "Was magic-link-only auth a deliberate decision… what was the rationale?" |

Every control run recommended proceeding toward the rejected feature (each failed
criterion 1) and re-asked the recorded rationale (each failed criterion 3). Notably,
all six *noticed* the missing `knowledge/` directory the README references — knowing
provenance should exist did not substitute for having it.

## Analysis

2×2 table: treatment 6 pass / 0 fail; control 0 pass / 6 fail.

```
$ python fisher.py 6 0 0 6
table=[[6,0],[0,6]]  one-sided p = 0.00108225  (SIGNIFICANT at alpha=0.005)
```

**One-sided Fisher's exact p = 1/924 ≈ 0.00108 < α = 0.005.** H₀ (equal pass
rates) rejected at the pre-registered level. No extension needed (perfect
separation at n = 6 per arm; the pre-registered n = 9 extension rule was not
triggered).

## Interpretation and scope

The effect is deterministic in this sample: the intervention (OKF wiki +
read-first behavior) flipped the outcome in 12 of 12 runs. Conclusions are
scoped to this scenario and model family per protocol; scoring was unblinded
(mitigated by the objective rubric and published raw outputs, which permit
independent re-scoring).
