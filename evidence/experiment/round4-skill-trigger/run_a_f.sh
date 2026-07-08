#!/bin/bash
# Round 4, Arm A (ambient positive control), Scenario F — 6 fresh headless runs.
set -u
BASE="$(cd "$(dirname "$0")" && pwd)"
mkdir -p "$BASE/transcripts"
cd "$BASE/../../../example"
for i in 1 2 3 4 5 6; do
  echo "[$(date +%H:%M:%S)] a-f-$i start"
  claude -p "$(cat "$BASE/prompt-f-ambient.txt")" --output-format stream-json --verbose \
    > "$BASE/transcripts/a-f-$i.jsonl" 2> "$BASE/transcripts/a-f-$i.err"
  echo "[$(date +%H:%M:%S)] a-f-$i exit $?"
done
echo "arm A scenario F done"
