## ADDED Requirements

### Requirement: Validator CLI
The repo SHALL provide `validator/validate.py`, a single-file, stdlib-only
Python CLI that validates a bundle directory and exits 0 on a conformant
bundle and 1 otherwise, printing one line per violation.

#### Scenario: Conformant bundle passes
- **WHEN** `python validator/validate.py example/knowledge` runs against the
  example bundle
- **THEN** it prints an OK summary with document count and exits 0

#### Scenario: Violations are itemized
- **WHEN** the validator runs against a bundle containing a broken link, a
  document without `type`, and an evidence-less Decision
- **THEN** it prints one FAIL line per violation naming the file and rule, and
  exits 1

### Requirement: Validation rules
The validator SHALL check: (1) every `.md` document has YAML frontmatter with
a `type` field, (2) every relative markdown link resolves to an existing file,
(3) every `type: Decision` document links to at least one evidence document
(interview or constraint).

#### Scenario: External links ignored
- **WHEN** a document contains an `https://` link
- **THEN** the validator does not attempt to resolve it and reports no error
  for it

### Requirement: Encoding tolerance
The validator SHALL accept files with or without a UTF-8 BOM.

#### Scenario: Windows-authored file
- **WHEN** a document was written by a tool that prepends a UTF-8 BOM
- **THEN** frontmatter is still parsed and no spurious error is reported

### Requirement: Validator test suite
The repo SHALL include automated tests for the validator covering the pass
case, each violation class, and the BOM case, runnable via `python -m pytest`
or `python -m unittest`.

#### Scenario: Tests run in CI
- **WHEN** the CI workflow executes the validator test job
- **THEN** all tests pass on a clean checkout with no dependency installation
