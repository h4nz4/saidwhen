---
type: Decision
title: Skills-first distribution
description: saidwhen's primary deliverable is a top-level skills/ directory of self-contained, drop-in Agent Skills; the AGENTS.md snippet becomes a wiki-init payload and fallback.
status: accepted
timestamp: 2026-07-08T02:30:00Z
tags: [distribution, adapters]
scope: skills/*
---

# Skills-first distribution

The primary deliverable is `skills/` at the repo root: self-contained
SKILL.md directories per the open
[Agent Skills standard](https://agentskills.io/home), installable by copying
into any supporting agent (Claude Code, Codex CLI, Gemini CLI, Cursor,
Copilot, …). Each skill inlines its behavior wording (with `behaviors/` as
the normative source, guarded in CI) and bundles what it needs to run
standalone — e.g. the validator as `scripts/validate.py` in the capture
skill. The AGENTS.md snippet is demoted from headline adapter to (a) the
payload a `wiki-init` skill offers to install for the ambient read-first
stance, and (b) the fallback for agents without skills support. The
`adapters/claude-code` label disappears; the OpenSpec skills keep their shape.

Shipping is gated by
[validation-gates-skills-first](validation-gates-skills-first.md).

**Amended 2026-07-08** (evidence:
[slim-to-skills interview](../interviews/2026-07-08-slim-to-skills.md)):
the snippet's canonical home is `skills/wiki-init/assets/snippet.md` — there
is no standalone `adapters/` directory. `skills/` is the entire product
surface; `behaviors/` remains only as the normative wording anchor for the
CI sync guard.

**Amended 2026-07-09** (evidence:
[trending-repo goal](../interviews/2026-07-09-trending-goal.md)): manual
copy stops being the *only* install path. The repo ships two one-command
channels off the unchanged `skills/<name>/SKILL.md` layout — `npx skills add
h4nz4/saidwhen` (skills.sh, multi-agent, the vendor-neutral primary) and a
Claude Code plugin/marketplace (`.claude-plugin/plugin.json` +
`marketplace.json`, offered alongside, never sole). The Claude-specific
channel is admissible only because the neutral one leads, per
[no-vendor-lock-in](../constraints/no-vendor-lock-in.md); manual copy remains
documented as the zero-tooling fallback. Rejected making the plugin the
headline install (Claude-only front door contradicts the constraint).

## Evidence

- [Interview 2026-07-08 with Ivan](../interviews/2026-07-08-distribution-strategy.md):
  "the entire repo should be designed as skills, so that people can drop-in
  install them", under the [no-vendor-lock-in](../constraints/no-vendor-lock-in.md)
  constraint.
- External: SKILL.md is the open Agent Skills standard (announced 2025-12-18,
  spec at [agentskills.io](https://agentskills.io/home)) with 16+
  implementations including
  [Codex](https://developers.openai.com/codex/skills), Gemini CLI, Cursor,
  and Copilot — so skill-shaped no longer implies Claude-only.

## Rejected

- **AGENTS.md-primary, skills demoted** ("keep, but demote" from round 1 of
  the same interview) — rejected the same day: it rested on the premise that
  SKILL.md was Claude-specific, which the Agent Skills standard falsifies.
  Revisit if the standard fragments or major agents drop support.
- **Coequal adapters** (skills and snippet as equal peers) — rejected: more
  surface to keep in sync, weaker story, no single obvious install path.
- **Everything ambient via AGENTS.md only** — rejected: moment-shaped
  behaviors (capture, gc, archive-harvest) fit conditional skill loading;
  forcing them into always-on context bloats every conversation.
