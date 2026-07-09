#!/usr/bin/env python3
"""Stop hook: keep the wiki current with OpenSpec archives.

Fires when the agent tries to stop. If a change was archived more recently
than the wiki's log was touched, it blocks with a one-line nudge to harvest.
Silent (exit 0) whenever the wiki is already current — zero tokens on the
happy path. Self-clears the moment the agent updates docs/knowledge/log.md.

Install (Claude Code): copy this file to .claude/hooks/ and register it as a
Stop hook in .claude/settings.json (see wiki-opsx-archive SKILL.md). Other
agents: run it however your harness fires an end-of-turn command; it reads the
Stop payload on stdin and emits Claude Code's block JSON on stdout.

ponytail: mtime signal, not a state file. Archiving is a rename into
openspec/changes/archive/, which bumps that dir's own mtime; harvesting
touches log.md. Newest-of-the-two wins. Upgrade to a manifest only if archives
and harvests start interleaving out of order.
"""
import json
import pathlib
import sys

root = pathlib.Path.cwd()
archive = root / "openspec" / "changes" / "archive"
log = root / "docs" / "knowledge" / "log.md"

# Drain the Stop-hook payload; we don't need it.
try:
    json.load(sys.stdin)
except Exception:
    pass

# Silent unless there's both an archive to harvest from and a wiki to harvest into.
if archive.is_dir() and log.is_file() and archive.stat().st_mtime > log.stat().st_mtime:
    print(json.dumps({
        "decision": "block",
        "reason": (
            "An OpenSpec change was archived but docs/knowledge/log.md hasn't "
            "changed since. Harvest the change's durable decisions and facts "
            "into docs/knowledge/ and append a log.md line (the wiki-opsx-archive "
            "behavior). If nothing is durable enough to keep, add a log.md line "
            "saying so — that satisfies this check too."
        ),
    }))

sys.exit(0)
