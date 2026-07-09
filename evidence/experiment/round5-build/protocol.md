# Pre-registered protocol — Round 5 (greenfield build A/B)

**Registered:** 2026-07-08, BEFORE any round-5 runs. Approved by the
project owner in the
[sign-off interview](../../../docs/knowledge/interviews/2026-07-08-round5-signoff.md).

## Question

Rounds 1–4 validated read-first behavior against a *pre-authored* knowledge
bundle. This round tests the full loop on a **greenfield build**: when an
agent develops a small app across multiple *fresh* sessions, does the
openspec + saidwhen toolchain (capture during the build, read-first
afterwards) produce informed handling of later requests that conflict with
constraints stated only in the first session — versus a plain agent given
the identical prompts?

## Arms

Both arms use **OpenAI Codex CLI** (`codex exec --sandbox workspace-write`, fresh session
per prompt, no shared context between prompts) and receive the **identical
five prompts, verbatim** ([prompts/](prompts/)). Each arm executes in its own
dedicated git worktree so neither agent can ever observe the other arm's
materials or outputs:

- **Arm C (control):** worktree `E:\PROJEKTI\saidwhen-r5-control`
  (branch `round5-control`). Working dir seeded from
  [fixtures/control/](fixtures/control/) — an **empty directory**. Plain
  Codex, no skills, no ambient instructions, no scaffolding.
- **Arm T (treatment):** worktree `E:\PROJEKTI\saidwhen-r5-treatment`
  (branch `round5-treatment`). Working dir seeded from
  [fixtures/treatment/](fixtures/treatment/):
  - saidwhen skills `wiki-explore`, `wiki-capture`, `wiki-opsx-explore`,
    `wiki-opsx-archive` at `.agents/skills/` (round-4-validated Codex path);
  - empty `docs/knowledge/` bundle (wiki-init skeleton, project one-liner
    filled);
  - `AGENTS.md` = the wiki-init ambient snippet (read-first + capture,
    verbatim);
  - `openspec init --tools codex` output (`openspec/`, `.codex/` skills and
    commands), OpenSpec CLI 1.5.0.

n = **6 independent run sequences per arm** (a sequence = prompts p1–p5 in
order against one fresh fixture copy), 12 sequences, 60 sessions total.

## Task

PocketLedger, a single-page personal expense tracker. Prompt p1 states four
owner constraints in-chat (no build step / no framework; localStorage only,
no backend, no accounts; **EUR only — multi-currency considered and
rejected**, revisit trigger: owner starts spending in another currency
regularly; solo maintainer) and asks for v1. Prompts p2–p3 add features
(category filter + totals; CSV export). Prompts p4–p5 are evaluation probes
in fresh sessions, `Do not modify any files`, with the fixed
RECOMMENDATION / PRIOR CONTEXT / QUESTIONS structure of rounds 2–4:

- **p4 — cloud sync + accounts** (conflicts with the local-only /
  no-backend / no-accounts constraint).
- **p5 — multi-currency + exchange rates** (conflicts with the recorded
  EUR-only rejection and its revisit trigger).

The constraints exist **only in p1's prompt text** at the start. Whether an
arm can cite them at p4/p5 depends entirely on what its agent durably wrote
down during p1–p3. Control may legitimately pass by spontaneously recording
constraints (e.g. in a README); that is the honest comparison.

## Outcomes (per probe run, PASS/FAIL — rubric of rounds 2–4)

Scored on p4 and p5 outputs only; p1–p3 are the build phase.

1. **Informed recommendation** — recommends against proceeding as requested,
   or conditions proceeding on explicitly superseding/revisiting the prior
   constraint (for p5: engages the recorded revisit trigger).
2. **Provenance citation** — cites where the constraint is recorded, by
   path, in the working directory (any file counts — wiki decision, spec,
   README, code comment).
3. **No re-asking** — asks no question whose answer was given in p1 (who the
   user is, accounts/backend stance, currency, maintenance budget). Delta /
   revisit-trigger questions are the prescribed behavior and do not count as
   re-asks.
4. **No fabricated provenance** — cites no file that does not exist; claims
   nothing the working directory does not contain.

**Mechanism data (reported, not gated):** whether Arm T wrote
decisions/interviews into `docs/knowledge/` during p1–p3, whether skills
triggered (event transcripts), and whether OpenSpec artifacts were created.
Secondary observation (not scored): both arms' apps checked for gross
functional parity so the treatment's provenance work isn't subsidized by a
worse app.

## Analysis (pre-registered)

Per probe: Fisher's exact test, Arm T vs Arm C pass counts (n = 6 vs 6).
Primary hypothesis: T > C on criterion 2 (provenance citation) for both
probes; criteria 1 and 3 reported per-criterion. No gate — this is a
comparative round; results reported as measured, including a control win.

## Execution and scoring (disclosed)

[run.ps1](run.ps1) orchestrates one arm per invocation: copies the pristine
fixture to `<worktree>/evidence/experiment/round5-build/runs/<arm>-<n>/app`,
then pipes each prompt into a fresh
`codex exec --sandbox workspace-write --cd <app> --json --output-last-message`
session.
Final messages land in `runs/<arm>-<n>/p<k>.md`, full event transcripts in
`p<k>.events.jsonl`. Arms run from their own worktrees; results are
collected back to this directory on main after scoring.

**Scoring conflict:** as rounds 1–4, the implementing agent orchestrates and
scores (pre-registered rubric, supporting quotes in `results.md`, raw
outputs published for independent re-scoring).

**Shared bench:** operator's global `~/.codex` config loads identically into
both arms. Codex may truncate skill descriptions under its context budget
(observed round 4); the AGENTS.md snippet in Arm T is the designated
fallback and part of the product's documented install.

## Owner sign-off

- [x] Rubric, arms, prompts, and n approved by project owner (Ivan) —
      recorded in the
      [sign-off interview](../../../docs/knowledge/interviews/2026-07-08-round5-signoff.md),
      2026-07-08.
