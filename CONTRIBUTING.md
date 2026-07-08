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

## Adding an adapter

Adapters live in `adapters/<tool>/` and contain **only tool-specific
binding** — frontmatter, triggers, lifecycle hooks, install steps. The
normative wording lives in [behaviors/](behaviors/) alone; adapters point at
it or embed it verbatim with a "edit there, not here" header. Include a
README with install steps (aim for 3) and the sync rule.

## Everything else

- Evidence under [evidence/](evidence/) is immutable history — link fixes
  only, never content edits.
- Validator stays single-file and stdlib-only; that constraint is the
  product.
- Run before pushing: `python -m unittest` in `validator/`, then
  `python validator/validate.py example/knowledge` from the repo root.
