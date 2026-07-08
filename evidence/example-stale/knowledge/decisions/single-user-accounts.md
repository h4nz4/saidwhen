---
type: Decision
title: Single-user accounts
description: TaskLite accounts are strictly single-user; no teams, sharing, or roles.
status: accepted
timestamp: 2025-01-15T10:00:00Z
tags: [accounts, scope]
---

# Single-user accounts

Each TaskLite account belongs to exactly one user. No team workspaces, no
sharing, no roles or permissions.

## Evidence

- [Interview 2025-01-15 with Ivan](../interviews/2025-01-15-account-model.md):
  users are individual freelancers and nobody has asked for team features;
  the project is [solo-maintained](../constraints/solo-maintainer.md) and
  multi-tenancy (roles, invitations, permission checks) is the single largest
  complexity multiplier a task tracker can take on.

## Rejected

- **Multi-user team workspaces** — rejected: no user demand as of 2025-01, and
  the permission/invitation/billing surface is unaffordable for a
  [solo maintainer](../constraints/solo-maintainer.md).
  **Revisit if agencies or teams repeatedly request shared use.**
