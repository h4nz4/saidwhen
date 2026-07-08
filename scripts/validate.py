"""Validate an OKF bundle against the Provenance Convention.

Checks: frontmatter has `type`, relative markdown links resolve, and every
Decision links to at least one evidence file (interview/constraint/external).
Usage: python scripts/validate.py <bundle-dir>
"""
import re
import sys
from pathlib import Path

# ponytail: regex frontmatter parse, swap for a YAML lib if fields get nested
FRONTMATTER = re.compile(r"\A---\n(.*?)\n---\n", re.S)
MD_LINK = re.compile(r"\[[^\]]*\]\(([^)#\s]+)\)")


def validate(bundle: Path) -> list[str]:
    errors = []
    for doc in bundle.rglob("*.md"):
        text = doc.read_text(encoding="utf-8-sig")  # tolerate Windows BOM
        rel = doc.relative_to(bundle)

        m = FRONTMATTER.match(text)
        if not m:
            errors.append(f"{rel}: missing YAML frontmatter")
            continue
        typ = re.search(r"^type:\s*(\S+)", m.group(1), re.M)
        if not typ:
            errors.append(f"{rel}: frontmatter missing required `type`")
            continue

        links = [l for l in MD_LINK.findall(text) if not l.startswith(("http://", "https://"))]
        for link in links:
            if not (doc.parent / link).resolve().exists():
                errors.append(f"{rel}: broken link -> {link}")

        if typ.group(1) == "Decision":
            evidence = [l for l in links if "interviews/" in l or "constraints/" in l]
            if not evidence:
                errors.append(f"{rel}: Decision has no evidence link (interview/constraint)")
    return errors


if __name__ == "__main__":
    bundle = Path(sys.argv[1] if len(sys.argv) > 1 else "knowledge")
    errs = validate(bundle)
    for e in errs:
        print(f"FAIL  {e}")
    print(f"{'INVALID' if errs else 'OK'}  {bundle} ({len(list(bundle.rglob('*.md')))} documents, {len(errs)} errors)")
    sys.exit(1 if errs else 0)
