---
type: Component
title: Validation tooling
description: validate.py and check_sync.py — what each guards and why both are single-file stdlib.
timestamp: 2026-07-08T20:30:00Z
tags: [architecture, tooling]
---

# Validation tooling

Two guards, both deliberately vendorable (single file, stdlib only, no
install) so any project can copy them without adopting this repo:

- **`validator/validate.py`** — bundle conformance (frontmatter, link
  resolution, Decision evidence, `source`⇒`timestamp`), plus two bridge
  checks: `--check-specs` walks any markdown for broken links and citations
  of superseded decisions (docs rot as a CI failure), and `--check-diff`
  maps a diff's changed paths to the Decisions whose `scope` globs govern
  them (advisory `WHY` lines for PR review). Every run also emits advisory
  `BLOAT` lines for documents over 8 KB — agents pay tokens for every byte
  they read, so oversized entries get flagged for wiki-gc instead of
  quietly taxing each future read.
- **`validator/check_sync.py`** — the single-source-of-truth guard: every
  `saidwhen:behavior` block embedded in a skill must match its
  `behaviors/*.md` original, and every bundled file copy (validator,
  renderer) must be byte-identical to canon. A divergence fails CI.

**Why this shape:** trust in the wiki is the product; the validator is what
lets a stranger (or an agent) trust a bundle it didn't write. Keeping it
dependency-free is a recorded stance — see
[no-vendor-lock-in](../constraints/no-vendor-lock-in.md) and the
[skills-first decision](../decisions/skills-first-distribution.md).
