---
type: Decision
title: Magic-link authentication
description: TaskLite authenticates via emailed single-use magic links; no passwords, no OAuth.
status: accepted
timestamp: 2026-07-08T10:00:00Z
tags: [auth, security]
---

# Magic-link authentication

TaskLite authenticates users with single-use magic links emailed to them.
No passwords are stored; no third-party OAuth providers are integrated.

## Evidence

- [Users are external freelancers](../constraints/external-users.md) — no
  corporate IdP to integrate with.
- [Solo maintainer](../constraints/solo-maintainer.md) — auth must be
  near-zero maintenance.
- [No password storage](../constraints/no-password-storage.md) — the owner
  rejects password liability outright.

## Rejected

- **OAuth / "Sign in with Google" SSO** — rejected because
  [users have no corporate IdP](../constraints/external-users.md) and each
  OAuth provider adds credential rotation, console setup, and breakage surface
  a [solo maintainer](../constraints/solo-maintainer.md) cannot afford.
  Revisit if a significant user segment demands social login.
- **Passwords** — rejected outright per the
  [no-password-storage](../constraints/no-password-storage.md) fact: storage,
  reset flows, and breach liability are the highest-maintenance option.
