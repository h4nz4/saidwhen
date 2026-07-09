# Round 6 results — consult-phase accuracy AND economy (the wiki-first round)

**Run date:** 2026-07-08 (both arms contemporaneous). **Scored:** 2026-07-08,
against the pre-registered rubric in [protocol.md](protocol.md), as amended
pre-run (Addenda 1–2: wiki-first framing; lean execution per the owner's
recorded directive, `docs/knowledge/constraints/lean-validation-runs.md`).

## Verdict

**Joint claim: SUPPORTED — the treatment arm was more accurate AND cheaper
on the same prompts.**

| Co-primary | Treatment | Control | Test |
|---|---|---|---|
| Accuracy (pooled c1+c3) | **6/6 PASS** | 0/6 | Fisher's exact, p = 1/924 ≈ 0.0011 |
| Economy (billable tokens/session, pooled) | mean **23,849** / median 23,342 | mean 35,462 / median 32,320 | **−33%**; Mann–Whitney U = 33/36, one-sided exact p ≈ 0.0076 |

Per probe: c1 (onboarding) 3/3 vs 0/3 and −47% mean billable tokens;
c3 (React rewrite) 3/3 vs 0/3 and −11%. Per-probe Fisher at n = 3 vs 3 is
p = 0.05; the pooled 6 vs 6 is the pre-registered accuracy report.
Wall-clock (secondary): treatment mean 39 s/session vs control 42 s.

## Environment

Codex CLI 0.142.5, default model at `model_reasoning_effort="low"`
(identical both arms; mini models rejected by the API on this ChatGPT-plan
account — probe attempts recorded in the session). Fixtures: the round-5
apps 1–3 per arm, as built (treatment bundles are v0.1 interview-form —
disclosed in Addendum 1). Fresh `codex exec --sandbox workspace-write`
session per probe, cwd = the app directory; outputs in
[runs/](runs/) (`c<k>.md` final answers, `c<k>.events.jsonl` full event
transcripts, `timing.csv` wall-clock).

## Scenario c1 — onboarding ("constraints and why")

Criterion 1 requires the local-only/no-backend AND EUR-only constraints
**with the owner's recorded rationale**; restating implementation behavior
without the why does not qualify (pre-registered).

| Run | Verdict | Supporting quote |
|---|---|---|
| treatment-1 | PASS | "EUR only … the owner only spends in EUR. Multi-currency was considered and rejected for v1" — sources: `decisions/eur-only.md`, kickoff interview |
| treatment-2 | PASS | "no backend, server, accounts … the owner described it as a personal tool and does not want to operate anything" |
| treatment-3 | PASS | "the owner only spends in EUR; multi-currency was explicitly rejected unless that changes" |
| control-1 | FAIL (crit. 1) | EUR-only's "why": "display uses `Intl.NumberFormat` with `currency: 'EUR'`" — behavior restated, no owner rationale anywhere |
| control-2 | FAIL (crit. 1) | local-only's "why": "the UI says expenses are 'stored on this browser'" — the recorded reason (owner refuses to operate anything) is absent |
| control-3 | FAIL (crit. 1) | "Currency is EUR. The UI starts with `EUR 0.00`, and formatting uses `Intl.NumberFormat`" |

All six runs' SOURCES paths verified to exist (63 citations checked
mechanically, 0 fabricated); treatment runs additionally disclosed that no
standalone `constraints/` documents exist rather than inventing any.

## Scenario c3 — conflicting rewrite (React + build pipeline)

| Run | Verdict | Supporting quote |
|---|---|---|
| treatment-1 | PASS | "On 2026-07-08, the owner decided PocketLedger v1 must work from disk with no build step … Is that still true, or has contributor growth become a higher priority?" — cites `plain-static-single-page.md` |
| treatment-2 | PASS | "A React rewrite … would directly supersede that accepted decision, so I would treat the PM request as a potential strategy change, not an implementation-ready request" |
| treatment-3 | PASS | "directly contradicts that accepted decision unless the owner confirms the revisit trigger has happened" — cites `plain-static-local-app.md` |
| control-1 | FAIL (crit. 2, 3) | cites only code paths; re-asks "Is PocketLedger intended to remain a static/offline browser app, or are backend sync/accounts/auth on the roadmap?" (answered at kickoff) |
| control-2 | FAIL (crit. 1, 2, 3) | recommends proceeding with tooling now ("First, introduce a proper build pipeline … Vite, npm scripts") against the unknown no-build constraint; re-asks "Is adding a dependency/build step acceptable?" |
| control-3 | FAIL (crit. 2, 3) | cites only code; re-asks "How important is zero-build static hosting and long-term dependency minimization?" (answered at kickoff) |

Treatment questions are delta/revisit-trigger or genuinely new-scope forms
throughout — the prescribed behavior, scored as non-re-asks per the
round-4 convention.

## Economy detail (pre-registered co-primary)

Per-session billable proxy = (input − cached input) + output tokens, from
`turn.completed` usage events; full per-session table via
[analyze.py](analyze.py):

- c1: treatment mean 22,607 vs control 42,607 (**−47%**) — control re-derived
  the project's story from source on every run; treatment read the wiki.
- c3: treatment mean 25,091 vs control 28,316 (−11%).
- Pooled: treatment lower on mean AND median; exact Mann–Whitney
  p ≈ 0.0076. Pre-registered economy claim **holds**.

## Disclosures and deviations

1. **Analysis-script bug fixed after data collection:** the registered
   `analyze.py` computed the lower tail of the U statistic — the wrong
   direction for the registered hypothesis (treatment < control), yielding
   p ≈ 0.996 for data overwhelmingly favoring the hypothesis (U = 33 of 36
   pairs treatment-lower). The fix (upper tail via the symmetric lower
   tail) changes only the tail direction; U and the registered hypothesis
   are untouched. Both versions are deterministic and the raw per-session
   numbers are published above and in `runs/`.
2. **Lean amendment before any run** (Addendum 2): 12 sessions instead of
   30, probes c1+c3, low reasoning effort — per the owner's recorded
   lean-runs directive. All amendments predate the first session.
3. **Self-scoring** as rounds 1–5: pre-registered rubric, quotes above, raw
   outputs and event transcripts in `runs/` for independent re-scoring.
4. **Fixture form:** treatment bundles are v0.1 (interview-evidence) form;
   this round validates wiki-first consultation and economy. The v1.0
   fact-form capture wording remains to be exercised by a future round.
5. **Model/effort:** results are at low reasoning effort on Codex's default
   model; prior rounds ran at default effort. Both arms identical, so the
   comparison is internally valid; absolute numbers are not comparable
   across rounds.
