---
type: Interview
title: Docs provenance scoping with Ivan
description: Q&A that scoped extending saidwhen to project documentation — rot detection first, generation deferred, validator-only mechanics.
timestamp: 2026-07-08T05:45:00Z
tags: [docs, distribution]
---

# Docs provenance scoping — 2026-07-08, with Ivan (owner)

**Q: Where does project documentation live in your daily work?**
A: In-repo markdown (README, docs/, architecture notes) plus AGENTS.md /
CLAUDE.md agent-facing docs. Nothing external (no Confluence/Notion) —
relative why-links and CI validation apply directly.

**Q: Which docs capability is the actual point?**
A: Rot detection (docs citing superseded decisions get flagged), generating
docs from the bundle, and capturing architecture notes (Component type).
Not the glossary — domain/ Terms stay dormant.

**Q: How to handle the evidence discipline for new docs behavior?**
A: Validator-only first — ship the mechanical parts (superseded-link
detection, documented why-link pattern for docs) with no new skill and no
new behavioral claims. Doc generation and any docs skill come later, gated
on validation (round-4 precedent).

**Q: Process?**
A: Archive skills-first-restructure as complete; open a fresh
docs-provenance change with its own artifacts.
