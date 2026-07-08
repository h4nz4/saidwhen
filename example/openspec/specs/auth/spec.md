# auth Specification

## Purpose

Authentication requirements for TaskLite. Every requirement carries a
`([why](...))` provenance link into [knowledge/](../../../knowledge/) — the
saidwhen ↔ OpenSpec integration in one file.

## Requirements

### Requirement: Magic-link login

The system MUST authenticate users via single-use magic links sent to their
email address; no passwords are stored
([why](../../../knowledge/decisions/magic-link-auth.md)).

#### Scenario: Login with email only

- **WHEN** a user submits their email address to sign in
- **THEN** they receive a single-use, time-limited login link, and no
  password is created or stored

### Requirement: Session lifetime

Sessions MUST expire after 30 days of inactivity
([why](../../../knowledge/decisions/magic-link-auth.md)).

#### Scenario: Inactive session expires

- **WHEN** a session sees no activity for 30 days
- **THEN** the next request requires a fresh magic-link login
