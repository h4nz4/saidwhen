"""Extract round-4 run answers and mechanism data from stream-json transcripts.

For each transcripts/<name>.jsonl: writes the final answer to runs/<name>.md
and prints one summary line: name, whether the wiki-explore skill was invoked,
whether any knowledge/ file was read, and the model ID. Stdlib only.
"""
import json
import sys
from pathlib import Path

BASE = Path(__file__).resolve().parent


def parse_codex(t: Path):
    """Codex `exec --json` transcript -> (result_text, skill, read_knowledge, model)."""
    result_text, skill, read_knowledge = None, False, False
    for line in t.read_text(encoding="utf-8").splitlines():
        try:
            obj = json.loads(line)
        except json.JSONDecodeError:
            continue
        item = obj.get("item", {})
        if obj.get("type") == "item.completed":
            if item.get("type") == "agent_message":
                result_text = item.get("text")
            else:
                blob = json.dumps(item)
                if "wiki-explore" in blob:
                    skill = True
                if "knowledge" in blob:
                    read_knowledge = True
    return result_text, skill, read_knowledge, "codex-cli-0.142.5"


def main() -> int:
    runs = BASE / "runs"
    runs.mkdir(exist_ok=True)
    rows = []
    for t in sorted((BASE / "transcripts").glob("*.jsonl")):
        if t.stem.startswith("s2-"):
            result_text, skill, read_knowledge, model = parse_codex(t)
            if result_text is None:
                rows.append((t.stem, skill, read_knowledge, model, "NO RESULT"))
            else:
                (runs / f"{t.stem}.md").write_text(result_text, encoding="utf-8")
                rows.append((t.stem, skill, read_knowledge, model, "ok"))
            continue
        result_text, skill, read_knowledge, model = None, False, False, "?"
        for line in t.read_text(encoding="utf-8").splitlines():
            try:
                obj = json.loads(line)
            except json.JSONDecodeError:
                continue
            if obj.get("type") == "system" and obj.get("subtype") == "init":
                model = obj.get("model", "?")
            if obj.get("type") == "assistant":
                for block in obj.get("message", {}).get("content", []):
                    if block.get("type") != "tool_use":
                        continue
                    inp = json.dumps(block.get("input", {}))
                    if block.get("name") == "Skill" and "wiki-explore" in inp:
                        skill = True
                    if "knowledge" in inp and block.get("name") in ("Read", "Grep", "Glob", "Bash"):
                        read_knowledge = True
            if obj.get("type") == "result":
                result_text = obj.get("result")
        if result_text is None:
            rows.append((t.stem, skill, read_knowledge, model, "NO RESULT"))
            continue
        (runs / f"{t.stem}.md").write_text(result_text, encoding="utf-8")
        rows.append((t.stem, skill, read_knowledge, model, "ok"))
    print(f"{'run':<10} {'skill':<6} {'read-knowledge':<15} {'model':<20} status")
    for name, skill, rk, model, status in rows:
        print(f"{name:<10} {str(skill):<6} {str(rk):<15} {model:<20} {status}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
