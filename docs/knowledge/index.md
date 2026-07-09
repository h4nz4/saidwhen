---
type: Index
title: saidwhen knowledge base
description: Entry point to this repo's own wiki — the project dogfoods its convention.
timestamp: 2026-07-08T20:30:00Z
---

# saidwhen knowledge base

The saidwhen project's own wiki. The demo bundle lives in
[example/knowledge/](../../example/knowledge/); this one is real.

## Use cases

What this wiki (and the product it documents) is for:

- **Agent memory** — an agent starting any task reads this index first and
  never re-asks what's recorded ([read-first](../../behaviors/read-first.md)).
- **Onboarding** — "what are the binding constraints and why?" is answered
  from [decisions](decisions/) and [constraints](constraints/), with names
  and dates.
- **PR review** — `--check-diff` maps changed files to the
  [decisions](decisions/) that govern them; `--check-specs` fails CI when
  docs cite superseded decisions.
- **OpenSpec loop** — proposals pull context from here; archiving writes
  knowledge back and updates [systems/](systems/) pages.
- **Human browsing** — CI compiles this bundle into the rendered wiki site
  on every push.

## Systems (architecture)

- [Three-layer architecture](systems/three-layer-architecture.md) — bundle / behaviors+skills / compiled presentation, and why nothing flows upward
- [Validation tooling](systems/validation-tooling.md) — validate.py + check_sync.py: conformance, docs-rot, diff impact, single-source guard
- [Render layer](systems/render-layer.md) — compiled disposable views; why presentation is generated, never stored
- [Evidence harness](systems/evidence-harness.md) — pre-registered rounds, worktree isolation, published raw outputs

## Decisions

- [saidwhen 2.0 — the product is an OKF wiki in a loop with OpenSpec](decisions/okf-wiki-pivot.md) — accepted 2026-07-08
- [Skills-first distribution](decisions/skills-first-distribution.md) — accepted 2026-07-08
- [Validation gates the skills-first restructure](decisions/validation-gates-skills-first.md) — accepted 2026-07-08
- [Dogfooding surfaced in README, workspace stays private](decisions/dogfooding-surfaced-not-published.md) — accepted 2026-07-08
- [A Stop hook auto-enforces the OpenSpec→wiki harvest](decisions/openspec-wiki-hook.md) — accepted 2026-07-09

## Constraints

- [No vendor lock-in](constraints/no-vendor-lock-in.md) — no agent vendor is privileged
- [Validation runs stay lean and cheap](constraints/lean-validation-runs.md) — owner directive (Ivan, 2026-07-08)

## Glossary

- [Attributed fact](domain/attributed-fact.md) — the default captured unit: statement + source + timestamp
- [Delta question](domain/delta-question.md) — "decided then because X — still true?"
- [Revisit trigger](domain/revisit-trigger.md) — the condition that reopens a decision
- [Behavior embed](domain/behavior-embed.md) — verbatim skill copies of normative wording, CI-guarded
- [Disposable view](domain/disposable-view.md) — rendered output: compiled, dated, never edited

## Interviews

- [2026-07-08 — distribution strategy with Ivan](interviews/2026-07-08-distribution-strategy.md)
- [2026-07-08 — round-4 protocol sign-off with Ivan](interviews/2026-07-08-round4-signoff.md)
- [2026-07-08 — round-5 protocol sign-off with Ivan](interviews/2026-07-08-round5-signoff.md)
- [2026-07-08 — round-6 goal and sign-off with Ivan](interviews/2026-07-08-round6-signoff.md)
- [2026-07-08 — wiki-pivot design interview with Ivan](interviews/2026-07-08-wiki-pivot.md)
- [2026-07-08 — dogfooding visibility with Ivan](interviews/2026-07-08-dogfooding-visibility.md)
- [2026-07-09 — trending-repo goal with Ivan](interviews/2026-07-09-trending-goal.md)

## History

See [log.md](log.md).
