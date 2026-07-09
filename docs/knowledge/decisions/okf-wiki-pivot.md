---
type: Decision
title: saidwhen 2.0 — the product is an OKF wiki in a loop with OpenSpec
status: accepted
timestamp: 2026-07-08T18:40:00Z
tags: [product, distribution]
scope: skills/* CONVENTION.md README.md render/* behaviors/*
---

# saidwhen 2.0: OKF wiki, OpenSpec loop, provenance as plumbing

## Decision

saidwhen's product is an **agent-maintained OKF project wiki, highly
interoperable with OpenSpec** — serving agents (project memory), the spec
workflow (knowledge layer), and humans (CI-published rendered site) equally.
Provenance (who-said-when, statuses, evidence links) is demoted from
headline to internal integrity mechanism, enforced by the validator.
Content scope: non-derivable knowledge (facts, constraints, decisions,
domain terms) **plus curated architecture** (Component pages), captured as
**attributed facts without transcripts or quotes**. OpenSpec interop is
bidirectional: propose pulls wiki context in; archive writes knowledge back
and updates affected Component pages; wiki-gc audits them for drift. Ships
as one integrated suite, as a full vertical slice (skills + Convention v1.0
+ render-in-CI + README), keeping the name "saidwhen", with a new
wiki-first validation round backing the new pitch.

## Rationale

The write-time token premium bought files nobody enjoys reading; the owner
wants the paid tokens to yield a visible, rich, trustworthy knowledge base
— while keeping the measured consult-time economy (small canonical files,
compiled presentation).

## Evidence

- [Design interview, 2026-07-08](../interviews/2026-07-08-wiki-pivot.md) —
  twelve owner answers fixing job, scope, interop depth, capture form,
  provenance role, render, name, evidence, convention, upkeep, milestone.

## Rejected

- **Provenance-first positioning (status quo)** — undersells the wiki; the
  owner's complaint: token premium with only skinny .md files to show.
- **Anchor quotes on captured facts** — rejected by owner for pure
  extraction. Accepted risk: extraction errors can't be re-verified against
  original wording; revisit if wrong-extraction incidents surface.
- **Split suite (core + opsx pack)** — one integrated suite instead.
- **Convention v0.2 backward-compatible amendment** — clean v1.0 break with
  migration notes instead.
- **LLM-generated narrative docs as stored truth** — rich pages remain a
  compiled, disposable render layer; the bundle stays the small source of
  truth.

Revisit triggers: extraction-error incidents (quotes), standalone-wiki
adopters who don't use OpenSpec (suite split), v0.1 bundle migration pain
(convention break).
