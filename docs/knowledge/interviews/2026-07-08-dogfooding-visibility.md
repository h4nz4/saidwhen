---
type: Interview
title: Dogfooding visibility and OpenSpec attribution with Ivan
description: Q&A that scoped surfacing the project's own dogfooding — README attribution for OpenSpec, knowledge/ as a proof point, CI teeth via --check-specs on public docs; re-tracking the openspec/ workspace rejected.
timestamp: 2026-07-08T06:30:00Z
tags: [docs, distribution, dogfooding]
---

# Dogfooding visibility — 2026-07-08, with Ivan (owner)

**Q: Does saidwhen depend on OpenSpec?**
A: No — confirmed the coupling is one-directional (only the two `wiki-opsx-*`
adapter skills touch it; core skills and validator are OpenSpec-free). But
the repo *is* developed with OpenSpec, invisibly.

**Q: What should change?**
A: "We should make the dogfooding better. We should attribute OpenSpec in
the readme. And mention the dogfooding."

**Q: How far should better dogfooding go?** (options offered: surface-only;
CI superseded-citation check on public docs; re-track `openspec/` workspace)
A: Surface + CI teeth (options 1+2). Re-tracking the workspace stays out of
scope — the untrack decision stands; dogfooding is proven via `knowledge/`
and CI, not by publishing maintainer tooling.
