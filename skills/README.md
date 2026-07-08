# Skills

saidwhen's primary deliverable: six self-contained skills in the open
[Agent Skills](https://agentskills.io/home) format (SKILL.md). Copy a skill's
directory into your agent's skills folder — that's the whole install. Each
skill embeds its behavior wording verbatim (normative source:
[behaviors/](../behaviors/), machine-checked in CI) and bundles what it needs
to run without this repo.

| Skill | What it does |
|---|---|
| [wiki-init](wiki-init/) | Scaffold a `docs/knowledge/` bundle; optionally install the ambient AGENTS.md snippet |
| [wiki-explore](wiki-explore/) | Read-first: consult the wiki before planning or asking anything |
| [wiki-capture](wiki-capture/) | Record decisions/interviews at the moment they crystallize (bundles the validator as `scripts/validate.py`) |
| [wiki-gc](wiki-gc/) | Periodic curation: merge, flag stale, repair links, prune, find gaps |
| [wiki-opsx-explore](wiki-opsx-explore/) | OpenSpec explore, wiki-first; why-link convention for delta specs |
| [wiki-opsx-archive](wiki-opsx-archive/) | OpenSpec archive, then harvest decisions into the bundle |

## Install paths

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
  decisions, so docs rot becomes a CI failure instead of a surprise.
