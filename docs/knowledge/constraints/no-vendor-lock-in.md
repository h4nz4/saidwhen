---
type: Constraint
title: No vendor lock-in
description: saidwhen's packaging and adapters must not privilege a single agent vendor; every deliverable must work across agent ecosystems.
timestamp: 2026-07-08T02:30:00Z
tags: [distribution]
---

# No vendor lock-in

Everything saidwhen ships — behaviors, adapters, tooling — must be usable
from any coding agent, not just Claude Code. Vendor-specific artifacts are
acceptable only as thin conveniences over a portable core.

Stated by Ivan in the
[2026-07-08 distribution interview](../interviews/2026-07-08-distribution-strategy.md):
"We don't want vendor lock-in to Claude Code."

**Extended 2026-07-09** (Ivan, in the
[trending-goal session](../interviews/2026-07-09-trending-goal.md)): the
constraint covers hosting platforms too — "there should be 0% vendor lock
in on GitHub". Publishing paths must stay host-neutral: the rendered wiki
is plain static HTML deployable to any static host; no deliverable may
depend on a GitHub-specific feature.
