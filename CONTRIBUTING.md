# Contributing to saidwhen

## The one rule that isn't normal

**Semantic edits to `behaviors/*.md` require re-validation before merge.**
The behavior wording is not prose — it's the tested artifact. It went 27/27
treatment runs across three pre-registered experiment rounds without a single
rubric failure ([evidence/VALIDATION.md](evidence/VALIDATION.md)). If your PR
changes what a behavior *instructs* (not typos/formatting):

1. Re-run at least the round-1 scenario: one agent in
   [example/](example/) following your edited behavior, task *"add Sign in
   with Google — evaluate and propose"*, scored against the rubric in
   [evidence/experiment/protocol.md](evidence/experiment/protocol.md).
2. Attach the transcript and scoring to the PR.

A behavior edit that can't pass the existing rubric doesn't merge, however
good it sounds.

## Amending the convention

CONVENTION.md is versioned (currently v0.1). Amendments go through an issue
first: state the problem, the proposed rule, and its migration cost.
Amendments MUST be backward-compatible within the major version — a
conformant v0.1 bundle stays conformant through every v0.x. Breaking rules
wait for v1.0 and need a migration note.

Changes to machine-checked conformance rules must land together with the
matching [validator](validator/) change and tests.

## Adding a skill (or adapter)

Skills live in `skills/<name>/` and must be **self-contained drop-ins**: a
SKILL.md whose behavior rules are embedded verbatim between
`<!-- saidwhen:behavior <name> ... -->` markers, plus any bundled assets
(the wiki-capture skill carries the validator as `scripts/validate.py`).
The normative wording lives in [behaviors/](behaviors/) alone — the embed is
a copy, and CI enforces it: `python validator/check_sync.py` fails on any
divergence between an embedded block and its behavior file, or between a
bundled file copy and its canonical source. Add new skills to the table in
[skills/README.md](skills/README.md).

Two guardrails beyond wording sync:

- **New delivery mechanisms need validation.** Skill-delivered read-first
  is validated ([round 4](evidence/experiment/round4-skill-trigger/results.md));
  a new mechanism (hook, MCP, another trigger model) can't claim parity in
  the README until it passes an equivalent pre-registered round.
- The AGENTS.md snippet lives at its single canonical home,
  `skills/wiki-init/assets/snippet.md` — the ambient fallback and the
  wiki-init payload. It carries the same marked regions and the same sync
  guard applies.

## Everything else

- Evidence under [evidence/](evidence/) is immutable history — link fixes
  only, never content edits.
- Validator stays single-file and stdlib-only; that constraint is the
  product.
- Run before pushing, from the repo root: `python -m unittest discover -s
  validator`, `python validator/validate.py example/knowledge --check-specs
  example/openspec/specs`, `python validator/validate.py knowledge`, and
  `python validator/check_sync.py`.
