---
type: Interview
title: Distribution strategy with Ivan
description: Q&A that settled how saidwhen itself is packaged and distributed — skills-first, vendor-neutral, validation-gated.
timestamp: 2026-07-08T02:30:00Z
tags: [distribution, adapters, openspec]
---

# Distribution strategy — 2026-07-08, with Ivan (owner)

Two rounds in one session, exploring OpenSpec interoperability. The second
round revised part of the first after a premise was corrected.

## Round 1 — OpenSpec interop scoping

**Q: What does "no vendor lock-in" mean for the Claude Code skills adapter?**
A: Keep, but demote — rebuild the OpenSpec adapter on a neutral mechanism,
Claude skills become a thin convenience layer.
*Revised in round 2 — see below. The answer was given under the premise that
SKILL.md was Claude-specific; it is in fact the open Agent Skills standard
([agentskills.io](https://agentskills.io/home)) with 16+ implementations
(Codex CLI, Gemini CLI, Cursor, Copilot, …).*

**Q: Primary carrier for the OpenSpec binding?**
A: AGENTS.md snippet. *(Also softened by round 2: the snippet remains the
carrier for the ambient read-first stance, but as an install payload, not
the headline adapter.)*

**Q: Which agent ecosystems should be demonstrably supported?**
A: Anything AGENTS.md-compliant, plus explicitly Cursor, Codex/Copilot, and
Claude Code — Claude Code not privileged.

**Q: How coupled to OpenSpec internals may the integration be?**
A: Loose only — depend on markdown files on disk, the spec grammar, and
relative links. No dependence on CLI flags or schema internals.

## Round 2 — capture round, after the premise correction

**Q: Where should the project's own decisions be recorded?**
A: Dogfood — create this root `knowledge/` bundle and record them publicly.

**Q: Read-first as a skill is an untested delivery mechanism (experiments
validated ambient instructions). How does that gate the restructure?**
A: Validate first — run the A/B round with skill-triggered read-first before
the skills-first restructure ships. The "measurably works" story stays
airtight at every commit.

**Q: Corrected stance on skills, now that SKILL.md is the open standard?**
A: Skills-first — `skills/` becomes the top-level primary deliverable for all
agents; the AGENTS.md snippet is demoted to a wiki-init payload and fallback
for skill-less agents; the `adapters/claude-code` label disappears.

**Q: Scope of the first change alongside the restructure and wiki-init?**
A: All of it — validator bundled into the capture skill, a behaviors↔skills
CI wording guard, a `--check-specs` why-link check, and an OpenSpec-shaped
example.

## Direct statements

- "We don't want vendor lock-in to Claude Code."
- "The entire repo should be designed as skills, so that people can drop-in
  install them."
