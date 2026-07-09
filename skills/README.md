# Skills

saidwhen's primary deliverable: eight self-contained skills in the open
[Agent Skills](https://agentskills.io/home) format (SKILL.md) that together
maintain a project wiki — an OKF bundle at `docs/knowledge/` serving agents
as project memory, [OpenSpec](https://github.com/Fission-AI/OpenSpec) as its
knowledge layer, and humans via compiled views. Copy a skill's directory
into your agent's skills folder — that's the whole install. Each skill
embeds its behavior wording verbatim (normative source:
[behaviors/](../behaviors/), machine-checked in CI) and bundles what it
needs to run without this repo.

| Skill | What it does |
|---|---|
| [wiki-init](wiki-init/) | Scaffold the `docs/knowledge/` wiki; optionally install the ambient AGENTS.md snippet and CI |
| [wiki-bootstrap](wiki-bootstrap/) | Populate a fresh wiki from an existing codebase — architecture pages, glossary, use cases; proposes, never invents whys |
| [wiki-explore](wiki-explore/) | Read-first: the wiki is project memory — consult it before planning, asking, or spelunking code |
| [wiki-capture](wiki-capture/) | Record knowledge as attributed facts and decisions at the moment it crystallizes (bundles the validator as `scripts/validate.py`) |
| [wiki-render](wiki-render/) | Compile the wiki into a browsable static HTML site — disposable views, zero LLM tokens (bundles the renderer) |
| [wiki-gc](wiki-gc/) | Periodic curation: merge, flag stale, audit Component drift, repair links, prune, find gaps |
| [wiki-opsx-explore](wiki-opsx-explore/) | OpenSpec explore/propose, wiki-first: recorded context flows into proposals by link |
| [wiki-opsx-archive](wiki-opsx-archive/) | OpenSpec archive: harvest facts and decisions into the wiki, update affected Component pages |

## Install

One command, either channel:

```bash
# Any agent (Claude Code, Cursor, Codex, 20+ others)
npx skills add h4nz4/saidwhen

# Claude Code — full suite as a plugin
/plugin marketplace add h4nz4/saidwhen
/plugin install saidwhen@saidwhen
```

`npx skills add` is the vendor-neutral path (skills.sh reads the
`skills/<name>/SKILL.md` layout directly); the plugin marketplace is the
Claude Code convenience, offered alongside — never the only path. `add`
without a skill name pulls the whole suite; append names for a subset.

### Or copy the directories manually

| Agent | Project-level | User-level |
|---|---|---|
| Claude Code | `.claude/skills/<skill>/` | `~/.claude/skills/<skill>/` |
| Codex (CLI & app) | `.agents/skills/<skill>/` | `~/.codex/skills/<skill>/` |
| Others (Gemini CLI, Cursor, Copilot, …) | per the [Agent Skills spec](https://agentskills.io/home) — most read a project skills directory; some require manual placement | varies |

## Honest support notes

- **Auto-triggering varies by agent.** Skill-triggered read-first is
  validated on Claude Code and Codex CLI
  ([round 4](../evidence/experiment/round4-skill-trigger/results.md): 6/6 on
  both scenarios, both agents; the skill auto-triggered in 24/24 runs).
  Other agents load the same files but their triggering is untested here.
- **Context budgets can truncate skill descriptions** (observed on Codex with
  many skills installed). If your agent doesn't reliably trigger
  wiki-explore, install the ambient
  [AGENTS.md snippet](wiki-init/assets/snippet.md) — `wiki-init` offers
  this during setup. The snippet is the designated fallback, not a downgrade:
  it carries the identical validated wording.
- Skills work without this repo present; the `behaviors/` references inside
  them name the normative source, not a runtime dependency.
- Your project docs (including AGENTS.md/CLAUDE.md) can carry
  `([why](...))` links into `docs/knowledge/` too — the bundled validator's
  `--check-specs <dir>` flags broken links *and* citations of superseded
  decisions, and `--check-diff` maps a diff's changed paths back to the
  decisions that govern them, so docs rot and forgotten constraints both
  become CI findings instead of surprises.
