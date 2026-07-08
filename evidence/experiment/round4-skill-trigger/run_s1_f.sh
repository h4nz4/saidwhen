#!/bin/bash
# Round 4, Arm S1 (skill, Claude Code), Scenario F — 6 fresh headless runs.
set -u
BASE="$(cd "$(dirname "$0")" && pwd)"
mkdir -p "$BASE/transcripts"
cd "$BASE/fixture-s"
for i in 1 2 3 4 5 6; do
  echo "[$(date +%H:%M:%S)] s1-f-$i start"
  claude -p "$(cat "$BASE/prompt-f.txt")" --output-format stream-json --verbose \
    > "$BASE/transcripts/s1-f-$i.jsonl" 2> "$BASE/transcripts/s1-f-$i.err"
  echo "[$(date +%H:%M:%S)] s1-f-$i exit $?"
done
echo "arm S1 scenario F done"
