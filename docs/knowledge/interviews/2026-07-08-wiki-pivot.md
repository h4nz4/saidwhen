---
type: Interview
title: Product pivot to an OKF wiki — design interview with Ivan
description: Twelve answers fixing the shape of the saidwhen 2.0 pivot — wiki as the product, provenance as plumbing, bidirectional OpenSpec loop.
timestamp: 2026-07-08T18:30:00Z
tags: [product, distribution]
---

# Wiki-pivot design interview — 2026-07-08, with Ivan (owner)

Context: after round 5 and the render PoC, the owner reframed the product:
"The main focus of the skills should not be provenance itself anymore. But
an OKF Wiki, that is highly interoperable with OpenSpec."

**Q: What is the wiki's primary job?**
A: All three equally — agent project memory, the OpenSpec knowledge layer,
and a human-facing project wiki maintained by agents.

**Q: What content belongs in the wiki?**
A: Non-derivable knowledge plus curated architecture — Component/system
pages are in scope, with upkeep discipline.

**Q: How deep does OpenSpec interoperability go?**
A: Bidirectional lifecycle — propose pulls wiki context in, archive writes
knowledge back, spec capabilities mirror wiki pages, the validator bridges
both directions.

**Q: Skill suite structure?**
A: One integrated suite; OpenSpec interop is first-class in every relevant
skill, not an add-on pack.

**Q: Default capture form?**
A: Facts only, no quotes — pure extracted statements with attribution
metadata; no dialogue transcripts, no verbatim anchor quotes. (Accepted
risk, raised and understood: a wrong extraction cannot be re-checked
against original wording.)

**Q: Where does provenance sit?**
A: Internal integrity mechanism — timestamps/sources/statuses enforced by
the validator, but the pitch is the wiki + OpenSpec loop; provenance is
plumbing.

**Q: The render layer?**
A: Core deliverable — CI-published browsable site compiled from the bundle
on every push; the human-facing face of the product.

**Q: Does the name survive?**
A: Keep "saidwhen".

**Q: Evidence strategy for the new pitch?**
A: Run a new wiki-first validation round measuring the new promises
(onboarding quality, spec-loop benefits, token economy); rounds 1–5 remain
as trust-layer evidence.

**Q: Convention impact?**
A: v1.0, clean break — redesign the Convention around the wiki product,
drop interview-centric wording, provide migration notes for v0.1 bundles.

**Q: Who keeps curated architecture pages current?**
A: Both — opsx:archive updates affected Component pages at the moment a
change lands; wiki-gc periodically audits them against reality and flags
drift.

**Q: What ships first?**
A: Full vertical slice — rewritten skills + Convention v1.0 + render-in-CI
+ repositioned README, released together as saidwhen 2.0.
