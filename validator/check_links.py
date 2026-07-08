"""Check that relative markdown links in the given files resolve.

Usage: python check_links.py README.md CONVENTION.md ...
Exits 0 if every relative link resolves, 1 otherwise. Stdlib only.
"""
import re
import sys
from pathlib import Path

MD_LINK = re.compile(r"\[[^\]]*\]\(([^)#\s]+)\)")


def check(files: list[str]) -> list[str]:
    errors = []
    for name in files:
        f = Path(name)
        for link in MD_LINK.findall(f.read_text(encoding="utf-8-sig")):
            if link.startswith(("http://", "https://", "mailto:")):
                continue
            if not (f.parent / link).resolve().exists():
                errors.append(f"{f}: broken link -> {link}")
    return errors


if __name__ == "__main__":
    errs = check(sys.argv[1:])
    for e in errs:
        print(f"FAIL  {e}")
    print(f"{'INVALID' if errs else 'OK'}  {len(sys.argv) - 1} files, {len(errs)} broken links")
    sys.exit(1 if errs else 0)
