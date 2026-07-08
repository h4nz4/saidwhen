#!/bin/bash
# Round 4, Arm S2 (skill, Codex CLI), Scenarios P and F — 6 fresh runs each.
set -u
BASE="$(cd "$(dirname "$0")" && pwd)"
CODEX="C:/Users/Ivan/AppData/Local/OpenAI/Codex/bin/ea1c60319a1dcb19/codex.exe"
mkdir -p "$BASE/transcripts"
cd "$BASE/fixture-s2"
for sc in p f; do
  for i in 1 2 3 4 5 6; do
    echo "[$(date +%H:%M:%S)] s2-$sc-$i start"
    "$CODEX" exec --skip-git-repo-check --json "$(cat "$BASE/prompt-$sc.txt")" \
      > "$BASE/transcripts/s2-$sc-$i.jsonl" 2> "$BASE/transcripts/s2-$sc-$i.err"
    echo "[$(date +%H:%M:%S)] s2-$sc-$i exit $?"
  done
done
echo "arm S2 scenarios P+F done"
