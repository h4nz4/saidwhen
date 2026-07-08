"""Validate an OKF bundle against the saidwhen Convention (v0.1).

Machine-checked rules: every document has frontmatter with `type`; every
relative markdown link resolves; every Decision links to evidence and has a
timestamp. Exits 0 on a conformant bundle, 1 otherwise.

Usage: python validate.py <bundle-dir> [--check-specs <specs-dir>]
--check-specs additionally verifies every relative link in the given spec
directory resolves (provenance why-links included) — plain markdown only,
no OpenSpec CLI or grammar dependency.
Stdlib only — vendor this single file if you want the check without the repo.
"""
import argparse
import re
import sys
from pathlib import Path

# ponytail: regex frontmatter parse, swap for a YAML lib if fields get nested
FRONTMATTER = re.compile(r"\A---\n(.*?)\n---\n", re.S)
MD_LINK = re.compile(r"\[[^\]]*\]\(([^)#\s]+)\)")


def validate(bundle: Path) -> list[str]:
    errors = []
    for doc in sorted(bundle.rglob("*.md")):
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
            if not re.search(r"^timestamp:\s*\S", m.group(1), re.M):
                errors.append(f"{rel}: Decision missing required `timestamp`")
    return errors


def check_specs(specs_dir: Path) -> list[str]:
    errors = []
    for doc in sorted(specs_dir.rglob("*.md")):
        text = doc.read_text(encoding="utf-8-sig")
        for link in MD_LINK.findall(text):
            if link.startswith(("http://", "https://")):
                continue
            if not (doc.parent / link).resolve().exists():
                errors.append(f"{doc.as_posix()}: broken link -> {link}")
    return errors


def main(argv=None) -> int:
    parser = argparse.ArgumentParser(description=__doc__.splitlines()[0])
    parser.add_argument("bundle", nargs="?", default="knowledge", help="bundle directory (default: knowledge)")
    parser.add_argument("--check-specs", metavar="DIR", help="also check relative links in a specs directory")
    parser.add_argument("--strict", action="store_true", help="reserved for future conformance levels")
    args = parser.parse_args(argv)

    bundle = Path(args.bundle)
    if not bundle.is_dir():
        print(f"INVALID  {bundle} is not a directory")
        return 1
    errs = validate(bundle)
    if args.check_specs:
        specs = Path(args.check_specs)
        if not specs.is_dir():
            print(f"INVALID  {specs} is not a directory")
            return 1
        errs += check_specs(specs)
    for e in errs:
        print(f"FAIL  {e}")
    print(f"{'INVALID' if errs else 'OK'}  {bundle} ({len(list(bundle.rglob('*.md')))} documents, {len(errs)} errors)")
    return 1 if errs else 0


if __name__ == "__main__":
    sys.exit(main())
