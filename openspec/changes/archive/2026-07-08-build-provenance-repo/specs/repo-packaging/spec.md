## ADDED Requirements

### Requirement: Public README
The repo SHALL have a README containing: the one-line pitch, the
provenance-chain diagram, a quickstart reaching a working wiki-aware agent in
at most 5 minutes using the AGENTS.md adapter, a layer overview
(convention/behaviors/adapters), and an evidence table where every
quantitative claim links to the protocol or results file that backs it.

#### Scenario: Claim traceability
- **WHEN** the README states a quantitative result (e.g. "6/6 vs 0/6",
  "p ≈ 0.0011")
- **THEN** the statement links to the evidence file that produced it, and the
  link resolves in CI

### Requirement: Evidence archive
All experiment artifacts (protocols, run transcripts, results, control and
stale fixtures, VALIDATION.md) SHALL live under `evidence/`, moved intact with
internal links updated; experiment content SHALL NOT be edited beyond link
fixes.

#### Scenario: Reproducibility preserved
- **WHEN** a visitor follows the reproduce steps in the moved VALIDATION.md
- **THEN** every referenced protocol, fixture, and transcript path resolves
  within `evidence/`

### Requirement: Example project
The repo SHALL keep `example/` (TaskLite) at the root as the browsable demo:
a conformant bundle with a complete spec → decision → interview chain,
validating clean in CI.

#### Scenario: GitHub browsing
- **WHEN** a visitor clicks from a spec requirement's why-link on GitHub
- **THEN** they land on the decision document, and its evidence links land on
  the interview — all rendered by GitHub's markdown viewer

### Requirement: Continuous integration
The repo SHALL have a GitHub Actions workflow that on every push and PR runs
the validator test suite, validates `example/knowledge`, and checks that
relative markdown links in README.md and CONVENTION.md resolve.

#### Scenario: Broken example fails CI
- **WHEN** a PR introduces a broken link or evidence-less Decision into the
  example bundle
- **THEN** the workflow fails with the validator's violation output

### Requirement: License and contribution scaffolding
The repo SHALL include an MIT LICENSE and a CONTRIBUTING.md that documents:
how to propose convention amendments, the rule that semantic edits to
`behaviors/*.md` require re-running the round-3 evaluation rubric, and how to
add an adapter.

#### Scenario: Behavior-edit guardrail is discoverable
- **WHEN** a contributor opens CONTRIBUTING.md intending to edit
  behaviors/read-first.md
- **THEN** they find the requirement to re-validate against the published
  rubric before merge
