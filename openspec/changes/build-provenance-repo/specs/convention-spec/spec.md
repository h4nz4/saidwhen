## ADDED Requirements

### Requirement: Versioned convention document
The repo SHALL contain a CONVENTION.md defining the Provenance Convention
v0.1: bundle layout under `knowledge/`, the five concept types (Decision,
Interview, Term, Constraint, Component), required and recommended frontmatter
fields, reserved files (`index.md`, `log.md`), and OKF conformance.

#### Scenario: Reader can implement from the document alone
- **WHEN** a developer reads CONVENTION.md with no other context
- **THEN** they can produce a bundle that passes the validator without
  consulting any other file

### Requirement: Provenance linking rules
The convention SHALL define the provenance chain as normative: a Decision MUST
link to at least one evidence document (Interview, Constraint, or external
source); a spec requirement SHOULD link to the Decision that produced it; all
links are relative markdown links.

#### Scenario: Decision without evidence is non-conformant
- **WHEN** a bundle contains a Decision document with no link to an interview,
  constraint, or external source
- **THEN** the convention declares it non-conformant and the validator reports
  an error for it

### Requirement: Staleness and supersession semantics
The convention SHALL define decision lifecycle: `status` values (`accepted`,
`superseded`, `revisit`), the recommended `## Rejected` section with revisit
triggers, and the rule that superseding a decision preserves the old document
with updated status rather than deleting it.

#### Scenario: Reopened decision keeps its history
- **WHEN** a decision is superseded by a new one
- **THEN** the original file remains in the bundle with `status: superseded`
  and a link to its successor, and `log.md` records the supersession
