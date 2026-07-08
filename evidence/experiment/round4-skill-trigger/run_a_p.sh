#!/bin/bash
# Round 4, Arm A (ambient positive control), Scenario P — 6 fresh headless runs.
set -u
BASE="$(cd "$(dirname "$0")" && pwd)"
mkdir -p "$BASE/transcripts"
cd "$BASE/../../../example"
for i in 1 2 3 4 5 6; do
  echo "[$(date +%H:%M:%S)] a-p-$i start"
  claude -p "$(cat "$BASE/prompt-p-ambient.txt")" --output-format stream-json --verbose \
    > "$BASE/transcripts/a-p-$i.jsonl" 2> "$BASE/transcripts/a-p-$i.err"
  echo "[$(date +%H:%M:%S)] a-p-$i exit $?"
done
echo "arm A scenario P done"
