## Why

The PoC validated the core hypothesis across 54 pre-registered runs (every use
case p ≈ 0.0011): an OKF-based provenance wiki plus a read-first behavior makes
AI agents recall decisions, reopen stale ones correctly, scope to constraints,
and never fabricate provenance. What exists today is validation scaffolding —
to become a public, potentially trending GitHub repo it needs to be packaged as
an installable, documented product: a polished convention spec, portable
behavior adapters, a demo people can run in 5 minutes, and the evidence
presented as a first-class selling point.

## What Changes

- Restructure the working directory into a publishable repo layout
  (convention, behaviors, adapters, example, validator, evidence).
- Finalize CONVENTION.md as a versioned spec (v0.1) with conformance rules.
- Add adapters that bind the read-first behavior to real tools:
  Claude Code skills (`wiki-explore`, `wiki-capture`, `wiki-gc`), an
  OpenSpec skill pack, and a copy-paste `AGENTS.md` snippet.
- Ship the validator as a proper CLI entry point with tests and CI (GitHub
  Actions: validate example bundle + run validator self-tests).
- Write the public README: pitch, provenance-chain diagram, 5-minute
  quickstart, evidence table linking to the experiment transcripts.
- Add contribution scaffolding: LICENSE (MIT), CONTRIBUTING.md.
- Keep the full experiment record (protocols, transcripts, results) as
  `evidence/` — the repo's differentiator versus other agent-memory projects.

## Capabilities

### New Capabilities
- `convention-spec`: the versioned Provenance Convention document — bundle
  layout, concept types, frontmatter fields, linking rules, log discipline,
  conformance criteria.
- `bundle-validation`: the validator CLI — frontmatter checks, link
  resolution, decision-evidence rule, exit codes, BOM tolerance.
- `agent-behaviors`: the tool-agnostic behavior prompts — read-first,
  capture-on-decision, staleness delta-questioning, no-fabrication rule.
- `tool-adapters`: bindings of the behaviors to concrete tools — Claude Code
  skills, OpenSpec skill pack, AGENTS.md snippet — with install instructions.
- `repo-packaging`: the public-facing repo surface — README with quickstart
  and evidence table, example project, evidence archive, license, CI.

### Modified Capabilities

(none — no existing specs in this project)

## Impact

- Everything currently at the repo root is reorganized; `example-control/`,
  `example-stale/`, `example-stale-control/` and `experiment/` move under
  `evidence/` (they are experiment fixtures, not product).
- `scripts/validate.py` becomes the `bundle-validation` CLI with tests.
- New dirs: `adapters/`, `evidence/`, `.github/workflows/`.
- No external dependencies added — stdlib Python + markdown only.
