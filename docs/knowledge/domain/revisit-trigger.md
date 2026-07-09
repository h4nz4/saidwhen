---
type: Term
title: Revisit trigger
description: The observable condition under which a decision should be reopened.
timestamp: 2026-07-08T20:30:00Z
---

A **revisit trigger** is the observable condition, recorded in a
Decision's `## Rejected` section, under which the decision should be
reopened — e.g. *"revisit multi-currency only if the owner starts spending
in another currency regularly."* Triggers make decisions falsifiable
instead of permanent: when one fires, the decision moves to
`status: revisit` and awaits a human answer to the delta question.
