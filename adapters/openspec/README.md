# OpenSpec adapter (reference integration)

Binds saidwhen to the [OpenSpec](https://github.com/Fission-AI/OpenSpec)
spec-driven workflow — the sharpest lifecycle moments available: explore and
propose consult the wiki, archive harvests it.

## Install

Copy the skill directories into your project's `.claude/skills/`. They layer
on top of the standard `opsx` skills — invoke these instead when the project
has a `knowledge/` bundle.

```
.claude/skills/
├── wiki-opsx-explore/SKILL.md   # explore, wiki-first
└── wiki-opsx-archive/SKILL.md   # archive, then harvest decisions
```

(Propose needs no dedicated skill: wiki-opsx-explore's read-first rules apply
to any planning conversation, and OpenSpec design.md decisions get harvested
at archive time.)

## Sync rule

These skills contain only OpenSpec-specific binding and point at the
normative wording in [behaviors/](../../behaviors/) — the single source of
truth. Do not fork behavioral wording here. Semantic behavior changes require
re-validation (see [CONTRIBUTING.md](../../CONTRIBUTING.md)).
