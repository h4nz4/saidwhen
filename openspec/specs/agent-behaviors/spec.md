# agent-behaviors Specification

## Purpose
TBD - created by syncing change build-provenance-repo. Defines the tool-agnostic agent behavior files: read-first, capture, no-fabrication, and curation.

## Requirements

### Requirement: Read-first behavior
The repo SHALL provide `behaviors/read-first.md` instructing agents to read
`knowledge/index.md` before planning or asking, never ask a question the wiki
answers, respect accepted decisions with current evidence, and ask only the
delta question when evidence is stale. The validated wording from the PoC
SHALL be preserved except where the split into multiple files requires
structural edits.

#### Scenario: Agent encounters a previously rejected request
- **WHEN** an agent following read-first.md receives a request the bundle
  records as rejected with current evidence
- **THEN** it recommends against proceeding, citing the decision file, and
  asks no question the wiki answers

#### Scenario: Agent encounters a fired revisit trigger
- **WHEN** the request matches a decision's recorded revisit trigger and the
  decision's evidence is stale
- **THEN** the agent proposes formally superseding the decision and asks only
  whether the remaining evidence still holds

### Requirement: Capture behavior
The repo SHALL provide `behaviors/capture.md` instructing agents to write
crystallized decisions as Decision documents with evidence links and a
`## Rejected` section, record new human answers as Interview documents, append
one line to `log.md` per write, and update `index.md` for load-bearing
concepts.

#### Scenario: Decision crystallizes during a session
- **WHEN** a design choice is settled with the human during agent work
- **THEN** the agent writes the Decision and Interview documents, the log
  line, and the index entry, and the resulting bundle passes the validator

### Requirement: No-fabrication rule
The behavior files SHALL instruct agents that when the wiki does not cover a
topic they must say so and proceed with normal questioning, never citing
non-existent documents.

#### Scenario: Uncovered topic
- **WHEN** an agent following the behaviors handles a request on a topic with
  no recorded decisions or constraints
- **THEN** it states the wiki is silent on the topic, applies any genuinely
  relevant recorded constraints, and asks its scoping questions normally

### Requirement: Curation behavior
The repo SHALL provide `behaviors/gc.md` defining a periodic curation pass:
merge duplicate concepts, flag decisions whose evidence has aged past their
revisit triggers, and repair broken links, with every change logged.

#### Scenario: Duplicate concepts
- **WHEN** the gc pass finds two documents describing the same fact
- **THEN** it merges them into one, leaves a link from the removed path or
  updates all inbound links, and appends the merge to `log.md`
