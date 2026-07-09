# Pre-registered protocol — Round 6 (consult-phase accuracy AND economy)

**Registered:** 2026-07-08, BEFORE any round-6 runs.

**Addendum (2026-07-08, still before any run):** this round is the
**wiki-first validation round** gating the saidwhen 2.0 README claims
(onboarding quality via c1, proposal informed-ness via c2/c3, consult-phase
token economy via the co-primary economy outcome) — see
`docs/knowledge/decisions/okf-wiki-pivot.md` and the repo-packaging spec's
"Wiki-first evidence round" requirement. Disclosure: the treatment fixtures
were built with the v0.1 (interview-based) capture wording; results validate
wiki-first consultation and economy, and the v1.0 fact-form capture wording
remains flagged for a follow-up round if this one's results don't transfer
on inspection.

**Addendum 2 (2026-07-08, still before any run) — lean execution, owner
directive:** the owner directed that this round run much leaner and on a
cheap model (recorded:
`docs/knowledge/constraints/lean-validation-runs.md`). Amended execution,
identical for both arms: **apps 1–3 only** (3 per arm), **probes c1 and c3
only** (onboarding + conflicting rewrite; c2 dropped — uncovered-topic
handling is already round-3-validated), and Codex's default model at
`model_reasoning_effort="low"` (mini models are unavailable to ChatGPT-plan
accounts; low effort is the available cost lever). 12 sessions total.
Analysis unchanged; accuracy additionally reported pooled across probes
(6 vs 6, Fisher's exact); the economy pool is 6 vs 6 sessions.

## Question

Round 5 showed the openspec+saidwhen treatment produced categorically better
informed handling (10/10 vs 0/10 probe passes at n = 5) at a ~24% sequence
token premium concentrated in the *write* phase, while its *read*-phase
sessions were 19–45% cheaper. This round tests the joint claim directly, at
session level: **on consult-phase work — evaluating requests against an
existing codebase — does the saidwhen-built project make the agent BOTH more
accurate AND cheaper than the vanilla-built project, on the same prompts?**

Accuracy and economy are **co-primary** pre-registered outcomes: the claim
holds only if the treatment arm wins both.

## Design

Reuses the ten completed round-5 apps as fixtures — 5 control-built
(vanilla), 5 treatment-built (with `docs/knowledge/` bundles and skills, as
they finished round 5, unmodified). Three new consult prompts
([prompts/](prompts/)), identical verbatim for every app, each a fresh
`codex exec --sandbox workspace-write` session with cwd = that app
directory, in the arm's own round-5 worktree:

- **c1 — onboarding/provenance:** new maintainer asks for the project's
  binding constraints *and why each exists*, with sources.
- **c2 — uncovered feature (budgets + alerts):** round-3-style
  constraint-informed scoping probe; the wiki is silent on budgets.
- **c3 — conflicting rewrite (React + build pipeline):** conflicts with the
  recorded plain-HTML / no-build-step / no-framework decision.

n = 5 apps × 3 prompts × 2 arms = 30 sessions. No app files are modified
(prompts say so); run order c1→c2→c3 per app.

## Outcomes

### Co-primary 1 — accuracy (PASS/FAIL per session, rubric of rounds 2–5)

**c1:** (1) states both the local-only/no-backend/no-accounts constraint AND
the EUR-only constraint **with the owner's recorded rationale** (personal
tool / doesn't want to operate anything; owner only spends EUR — a
restatement of current implementation behavior without the why does not
count); (2) every SOURCES path exists in the app directory; (3) no
fabricated provenance.

**c2:** (1) scopes the proposal using recorded constraints (local-only, no
backend for alerts/notifications, solo-maintainer simplicity); (2) asks no
question whose answer is recorded in the working directory (or was given in
the round-5 kickoff and recorded); (3) no fabricated provenance — saying the
project has no budget decision is correct, inventing one is a FAIL.

**c3:** (1) recommends against the React/build-pipeline rewrite as
requested, or conditions it on explicitly superseding the recorded
no-framework/no-build-step decision; (2) cites where that constraint is
recorded, by path; (3) no re-asking of recorded answers (delta/revisit
questions are the prescribed behavior); (4) no fabricated provenance.

A session passes only if all its criteria hold. Per prompt: Fisher's exact,
treatment vs control pass counts (5 vs 5).

### Co-primary 2 — economy (tokens per session)

From each session's `--json` event stream: sum `turn.completed` usage —
`input_tokens`, `cached_input_tokens`, `output_tokens`. Cost metric
per session: **billable proxy = (input_tokens − cached_input_tokens) +
output_tokens**; total input and output also reported.

Pre-registered test: one-sided Mann–Whitney U (treatment < control) on the
billable proxy, pooled across the 15 sessions per arm, plus per-prompt
means/medians and the full per-session table. **The economy claim holds iff
the treatment mean AND median are lower pooled, and the Mann–Whitney
one-sided p < 0.05.**

### Joint claim (the round's headline)

Supported only if BOTH co-primaries hold. Reported honestly either way; a
split result (accurate but not cheaper, or vice versa) is reported as such.

### Secondary (reported, not gated)

Wall-clock per session (runner timestamps), shell-command counts, and
whether treatment sessions read the wiki vs re-derived from code (event
transcripts).

## Threats and disclosures (pre-registered)

- **Fixture inheritance:** arms consult the apps their own arm built —
  that inheritance (wiki present vs absent) *is the treatment*; app
  functionality was checked for gross parity in round 5.
- **Session mix:** this round measures consult-phase economics only. The
  write-phase premium measured in round 5 (~+24% per build sequence, with
  OpenSpec ceremony included) is quoted alongside the result; the honest
  composite claim is "cheaper per consult session, premium at write time,
  net direction depends on a project's read/write ratio."
- **Self-scoring:** as rounds 1–5 — pre-registered rubric, quotes in
  results.md, raw outputs and event transcripts published.
- **Round-5 context:** round 5 was stopped by the owner at 5/6 sequences
  per arm (usage limits); this round consumes its completed sequences and
  was registered while round-5 sequence 6 remains unrun.
- **Environment:** operator's global `~/.codex` config loads identically
  into both arms; Codex may truncate skill descriptions (round-4 note).

## Execution

[run.ps1](run.ps1) orchestrates one arm per invocation (fresh sessions,
outputs to `<worktree>/evidence/experiment/round6-consult/runs/<arm>-<n>/`,
final messages `c<k>.md`, transcripts `c<k>.events.jsonl`, per-session
start/end timestamps in `timing.csv`). Analysis script computes the token
sums and Mann–Whitney exactly (stdlib only).

## Owner sign-off

- [x] Owner (Ivan) set the session goal: "I would need some way to have
      saidwhen prove as a tool that increases accuracy of implementations
      and economizes at the same time (saves tokens/time etc)" —
      2026-07-08, recorded in
      [the sign-off interview](../../../docs/knowledge/interviews/2026-07-08-round6-signoff.md).
      Registered before any round-6 session ran.
