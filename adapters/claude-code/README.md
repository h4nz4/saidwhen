# Claude Code adapter

Three skills binding the saidwhen behaviors to Claude Code.

## Install

Copy the three skill directories into your project's `.claude/skills/`
(or `~/.claude/skills/` for all projects):

```
.claude/skills/
├── wiki-explore/SKILL.md
├── wiki-capture/SKILL.md
└── wiki-gc/SKILL.md
```

Invoke as `/wiki-explore`, `/wiki-capture`, `/wiki-gc` — or let Claude trigger
them from their descriptions.

## Sync rule

Each SKILL.md contains only tool-specific binding (frontmatter, triggers) and
points at the normative wording in [behaviors/](../../behaviors/) — the single
source of truth. Do not fork behavioral wording into the skills; change
`behaviors/` and keep the skills as pointers. Semantic behavior changes
require re-validation (see [CONTRIBUTING.md](../../CONTRIBUTING.md)).
