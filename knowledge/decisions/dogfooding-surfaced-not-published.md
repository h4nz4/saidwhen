---
type: Decision
title: Dogfooding surfaced in README, workspace stays private
description: The README credits OpenSpec and presents root knowledge/ as the project's live bundle; public docs get the full --check-specs pass in CI; the openspec/ workspace remains untracked.
status: accepted
timestamp: 2026-07-08T06:30:00Z
tags: [distribution, docs, dogfooding]
---

# Dogfooding surfaced in README, workspace stays private

The README attributes [OpenSpec](https://github.com/Fission-AI/OpenSpec)
wherever the `wiki-opsx-*` adapters appear and carries a proof-point section
presenting root `knowledge/` as the project's real, CI-validated bundle,
deep-linking [skills-first-distribution](skills-first-distribution.md) as
the exhibit. CI runs the validator's `--check-specs` pass (link resolution
plus superseded-decision citation detection) over the public documents —
README, CONVENTION, CONTRIBUTING, VALIDATION — which required
`--check-specs` to accept single files; the standalone link checker was
retired as a strict subset.

## Evidence

- [Interview 2026-07-08 with Ivan](../interviews/2026-07-08-dogfooding-visibility.md):
  attribute OpenSpec, mention the dogfooding, surface + CI teeth — not
  workspace publication.

## Rejected

- **Re-tracking the `openspec/` workspace** to make the adapter-path
  dogfooding publicly browsable — rejected: reopens the deliberate untrack
  of maintainer tooling and carries workspace noise into the product repo.
  Revisit if users ask to see real delta specs with why-links in the wild,
  or if a public reference for the `wiki-opsx-*` flow proves necessary
  beyond `example/openspec/`.
- **Pointing `--check-specs` at a directory (`.` or `evidence/`)** instead
  of extending it to files — rejected: the walk would sweep in
  deliberately-broken fixtures (`evidence/example-stale/`) and transcripts.
