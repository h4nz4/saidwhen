"""CI guard: adapter/skill copies must match their canonical sources.

Two checks, per the single-source-of-behavior-truth rule:
1. Every `<!-- saidwhen:behavior <name> ... -->` block in adapters/ and
   skills/ matches (whitespace-insensitively) the same-named block in
   behaviors/<name>.md.
2. Every bundled file copy (validator, snippet) is byte-identical to its
   canonical source.

Exits 0 when everything is in sync, 1 otherwise. Stdlib only.
"""
import re
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
BLOCK = re.compile(r"<!-- saidwhen:behavior (\S+)[^>]*-->\n(.*?)<!-- /saidwhen:behavior", re.S)
# (canonical file, glob of bundled copies that must stay byte-identical)
COPIES = [
    ("validator/validate.py", "skills/*/scripts/validate.py"),
]
# ponytail: guard checks blocks that exist; a skill that silently drops its
# marker block escapes — add a required-coverage map if that ever happens.


def norm(text: str) -> str:
    return " ".join(text.split())


def main() -> int:
    errors = []

    canon = {}
    for f in sorted((ROOT / "behaviors").glob("*.md")):
        for name, body in BLOCK.findall(f.read_text(encoding="utf-8")):
            canon[name] = norm(body)
    if not canon:
        errors.append("no marked behavior regions found in behaviors/")

    embeds = 0
    for base in ("adapters", "skills"):
        for md in sorted(ROOT.glob(f"{base}/**/*.md")):
            for name, body in BLOCK.findall(md.read_text(encoding="utf-8")):
                embeds += 1
                rel = md.relative_to(ROOT).as_posix()
                if name not in canon:
                    errors.append(f"{rel}: unknown behavior marker '{name}'")
                elif norm(body) != canon[name]:
                    errors.append(f"{rel}: embedded '{name}' wording diverges from behaviors/{name}.md")

    copies = 0
    for canonical, pattern in COPIES:
        src = ROOT / canonical
        for copy in sorted(ROOT.glob(pattern)):
            copies += 1
            if copy.read_bytes() != src.read_bytes():
                errors.append(f"{copy.relative_to(ROOT).as_posix()}: differs from {canonical}")

    for e in errors:
        print(f"FAIL  {e}")
    print(f"{'INVALID' if errors else 'OK'}  sync guard ({embeds} embeds, {copies} file copies, {len(errors)} errors)")
    return 1 if errors else 0


if __name__ == "__main__":
    sys.exit(main())
