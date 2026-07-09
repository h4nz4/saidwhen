---
type: Interview
title: Trending-repo goal with Ivan
description: Owner's directive — evolve saidwhen toward a trending repo; auto human-readable docs and lower token costs are the two goals.
timestamp: 2026-07-09T00:00:00Z
tags: [direction]
---

# Trending-repo goal — 2026-07-09, with Ivan (owner)

**Q: What should saidwhen evolve toward?**
A (verbatim): "Please help me evolve saidwhen into a trending repository.
Goals: saidwhen should generate meaningful, useful, human readable
documentation automatically / semi automatically; it should decrease token
costs."

**Q (follow-up, same session): a GitHub Pages deploy was proposed for the
live-docs goal — acceptable?**
A (verbatim): "No, there should be 0% vendor lock in on GitHub..." — the
Pages deploy was retracted before merge; the
[no-vendor-lock-in](../constraints/no-vendor-lock-in.md) constraint now
explicitly covers hosting platforms. Publishing stays host-neutral: static
HTML, any host, user's choice.

Acted on the same day:

- The validator gains an advisory BLOAT check (per-doc size over 8 KB) so
  bundles stay cheap to read — agents pay for every byte, and oversized
  entries are handed to wiki-gc instead of taxing every future read.
- wiki-render's CI guidance states the host-neutral contract explicitly.
