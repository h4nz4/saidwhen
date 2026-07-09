"""Validate an OKF bundle against the saidwhen Convention (v1.0).

Machine-checked rules: every document has frontmatter with `type`; every
relative markdown link resolves; every Decision links to evidence (an
attributed fact under constraints//domain//systems/, or a legacy interview)
and has a timestamp; every document carrying `source` also carries a
`timestamp`. Exits 0 on a conformant bundle, 1 otherwise.

Usage: python validate.py <bundle-dir> [--check-specs <dir-or-file>]...
                                       [--check-diff <changed-path>... | --check-diff -]
--check-specs (repeatable: specs/docs dirs or single .md files) additionally
verifies every relative link in the given documents resolves, and that no checked document
cites a superseded Decision (docs rot) — plain markdown only, no OpenSpec CLI
or grammar dependency. Supersession links inside the bundle itself are exempt.
--check-diff reports which Decisions govern the given changed paths (advisory,
never fails the run): a Decision opts in with a `scope:` frontmatter field of
whitespace-separated fnmatch globs. Pass `-` to read paths from stdin, e.g.
`git diff --name-only main | python validate.py docs/knowledge --check-diff -`.
Every run also prints an advisory BLOAT line per document over 8 KB — agents
pay for every byte they read, so oversized entries are a token-cost smell to
hand to wiki-gc (split, prune, or archive). Never fails the run.
Stdlib only — vendor this single file if you want the check without the repo.
"""
import argparse
import re
import sys
from fnmatch import fnmatch
from pathlib import Path

# ponytail: regex frontmatter parse, swap for a YAML lib if fields get nested
FRONTMATTER = re.compile(r"\A---\n(.*?)\n---\n", re.S)
MD_LINK = re.compile(r"\[[^\]]*\]\(([^)#\s]+)\)")


def md_links(text: str) -> list[str]:
    """Links outside code — a link inside `backticks` or a ``` fence is syntax
    documentation (e.g. `([why](...))`), not a live link to resolve."""
    text = re.sub(r"```.*?```", "", text, flags=re.S)
    text = re.sub(r"`[^`]*`", "", text)
    return MD_LINK.findall(text)


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

        links = [l for l in md_links(text) if not l.startswith(("http://", "https://"))]
        for link in links:
            if not (doc.parent / link).resolve().exists():
                errors.append(f"{rel}: broken link -> {link}")

        if re.search(r"^source:\s*\S", m.group(1), re.M) \
                and not re.search(r"^timestamp:\s*\S", m.group(1), re.M):
            errors.append(f"{rel}: attributed document (`source`) missing required `timestamp`")

        if typ.group(1) == "Decision":
            evidence = [l for l in links if any(
                d in l for d in ("interviews/", "constraints/", "domain/", "systems/"))]
            if not evidence:
                errors.append(f"{rel}: Decision has no evidence link (fact/constraint/interview)")
            if not re.search(r"^timestamp:\s*\S", m.group(1), re.M):
                errors.append(f"{rel}: Decision missing required `timestamp`")
    return errors


def check_specs(specs_path: Path) -> list[str]:
    errors = []
    docs = [specs_path] if specs_path.is_file() else sorted(specs_path.rglob("*.md"))
    for doc in docs:
        text = doc.read_text(encoding="utf-8-sig")
        for link in md_links(text):
            if link.startswith(("http://", "https://")):
                continue
            target = (doc.parent / link).resolve()
            if not target.exists():
                errors.append(f"{doc.as_posix()}: broken link -> {link}")
            elif target.suffix == ".md":
                fm = FRONTMATTER.match(target.read_text(encoding="utf-8-sig"))
                if fm and re.search(r"^type:\s*Decision\s*$", fm.group(1), re.M) \
                      and re.search(r"^status:\s*superseded\s*$", fm.group(1), re.M):
                    # ponytail: successor hint = first decisions/ link in the stale doc
                    succ = [l for l in md_links(target.read_text(encoding="utf-8-sig"))
                            if "decisions/" in l]
                    hint = f" (successor: {succ[0]})" if succ else ""
                    errors.append(f"{doc.as_posix()}: cites superseded decision -> {link}{hint}")
    return errors


# ponytail: flat per-doc byte cap; per-type budgets if interviews prove noisy
BLOAT_BYTES = 8 * 1024


def check_bloat(bundle: Path) -> list[str]:
    """Advisory: documents whose size makes every agent read expensive."""
    return [f"{doc.relative_to(bundle).as_posix()}: {size / 1024:.1f} KB "
            f"(~{size // 4} tokens per agent read) -> split, prune, or archive (wiki-gc)"
            for doc in sorted(bundle.rglob("*.md"))
            if (size := doc.stat().st_size) > BLOAT_BYTES]


def check_diff(bundle: Path, changed: list[str]) -> list[str]:
    """Advisory: which Decisions (via `scope:` globs) govern the changed paths."""
    changed = [c.strip().replace("\\", "/") for c in changed if c.strip()]
    hits = []
    for doc in sorted(bundle.rglob("*.md")):
        fm = FRONTMATTER.match(doc.read_text(encoding="utf-8-sig"))
        if not fm or not re.search(r"^type:\s*Decision\s*$", fm.group(1), re.M):
            continue
        scope = re.search(r"^scope:\s*(.+)$", fm.group(1), re.M)
        if not scope:
            continue
        status = re.search(r"^status:\s*(\S+)", fm.group(1), re.M)
        matched = sorted({c for c in changed for pat in scope.group(1).split() if fnmatch(c, pat)})
        if matched:
            hits.append(f"{doc.relative_to(bundle).as_posix()} "
                        f"({status.group(1) if status else 'no status'}) governs: {', '.join(matched)}")
    return hits


def main(argv=None) -> int:
    parser = argparse.ArgumentParser(description=__doc__.splitlines()[0])
    parser.add_argument("bundle", nargs="?", default="docs/knowledge", help="bundle directory (default: docs/knowledge)")
    parser.add_argument("--check-specs", metavar="PATH", action="append",
                        help="also check a specs/docs directory or single .md file: links must resolve and must not cite superseded decisions (repeatable)")
    parser.add_argument("--check-diff", metavar="PATH", nargs="+",
                        help="report which Decisions govern these changed paths (advisory; `-` reads paths from stdin)")
    parser.add_argument("--strict", action="store_true", help="reserved for future conformance levels")
    args = parser.parse_args(argv)

    bundle = Path(args.bundle)
    if not bundle.is_dir():
        print(f"INVALID  {bundle} is not a directory")
        return 1
    errs = validate(bundle)
    for d in args.check_specs or []:
        specs = Path(d)
        if not specs.exists():
            print(f"INVALID  {specs} does not exist")
            return 1
        errs += check_specs(specs)
    if args.check_diff:
        changed = sys.stdin.read().splitlines() if args.check_diff == ["-"] else args.check_diff
        for hit in check_diff(bundle, changed):
            print(f"WHY   {hit}")
    for hit in check_bloat(bundle):
        print(f"BLOAT {hit}")
    for e in errs:
        print(f"FAIL  {e}")
    print(f"{'INVALID' if errs else 'OK'}  {bundle} ({len(list(bundle.rglob('*.md')))} documents, {len(errs)} errors)")
    return 1 if errs else 0


if __name__ == "__main__":
    sys.exit(main())
