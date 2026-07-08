# Authentication

## Requirements

### AUTH-1: Magic-link login

The system MUST authenticate users via single-use magic links sent to their
email address. No passwords are stored.
<!-- why: ../../knowledge/decisions/magic-link-auth.md -->
([why](../../knowledge/decisions/magic-link-auth.md))

### AUTH-2: Session lifetime

Sessions MUST expire after 30 days of inactivity.
([why](../../knowledge/decisions/magic-link-auth.md))
