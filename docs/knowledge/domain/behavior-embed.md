---
type: Term
title: Behavior embed
description: The verbatim copy of normative behavior wording inside a skill, machine-checked against behaviors/.
timestamp: 2026-07-08T20:30:00Z
---

A **behavior embed** is the block between
`<!-- saidwhen:behavior <name> -->` markers inside a SKILL.md or the
AGENTS.md snippet: a verbatim copy of the normative wording in
`behaviors/<name>.md`. Skills are delivery vehicles, not forks — the
embed lets a skill work standalone while `check_sync.py` guarantees in CI
that exactly one normative source exists.
