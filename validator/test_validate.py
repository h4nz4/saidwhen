"""Tests for validate.py — runnable via `python -m pytest` or `python -m unittest`."""
import tempfile
import unittest
from pathlib import Path

from validate import check_bloat, check_diff, validate, main

GOOD_DECISION = """---
type: Decision
status: accepted
timestamp: 2026-07-08T10:00:00Z
---
Evidence: [interview](../interviews/talk.md)
"""
INTERVIEW = """---
type: Interview
timestamp: 2026-07-08T09:00:00Z
---
Q&A body with an [external link](https://example.com/ok).
"""


class ValidateTests(unittest.TestCase):
    def setUp(self):
        self._tmp = tempfile.TemporaryDirectory()
        self.bundle = Path(self._tmp.name)
        (self.bundle / "decisions").mkdir()
        (self.bundle / "interviews").mkdir()

    def tearDown(self):
        self._tmp.cleanup()

    def write(self, rel, text, encoding="utf-8"):
        p = self.bundle / rel
        p.write_text(text, encoding=encoding)
        return p

    def test_conformant_bundle_passes(self):
        self.write("decisions/d.md", GOOD_DECISION)
        self.write("interviews/talk.md", INTERVIEW)
        self.assertEqual(validate(self.bundle), [])

    def test_missing_type_reported(self):
        self.write("decisions/d.md", "---\ntitle: no type here\n---\nbody")
        errs = validate(self.bundle)
        self.assertTrue(any("missing required `type`" in e for e in errs))

    def test_missing_frontmatter_reported(self):
        self.write("decisions/d.md", "just a body, no frontmatter")
        errs = validate(self.bundle)
        self.assertTrue(any("missing YAML frontmatter" in e for e in errs))

    def test_broken_link_reported(self):
        self.write("interviews/talk.md", INTERVIEW.replace("Q&A body", "[gone](nope.md) body"))
        errs = validate(self.bundle)
        self.assertTrue(any("broken link -> nope.md" in e for e in errs))

    def test_external_links_ignored(self):
        self.write("interviews/talk.md", INTERVIEW)
        self.assertEqual(validate(self.bundle), [])

    def test_decision_without_evidence_reported(self):
        self.write("decisions/d.md", GOOD_DECISION.replace("[interview](../interviews/talk.md)", "no links"))
        errs = validate(self.bundle)
        self.assertTrue(any("no evidence link" in e for e in errs))

    def test_decision_without_timestamp_reported(self):
        self.write("decisions/d.md", GOOD_DECISION.replace("timestamp: 2026-07-08T10:00:00Z\n", ""))
        self.write("interviews/talk.md", INTERVIEW)
        errs = validate(self.bundle)
        self.assertTrue(any("missing required `timestamp`" in e for e in errs))

    def test_bom_tolerated(self):
        self.write("decisions/d.md", GOOD_DECISION, encoding="utf-8-sig")
        self.write("interviews/talk.md", INTERVIEW, encoding="utf-8-sig")
        self.assertEqual(validate(self.bundle), [])

    def test_check_specs_broken_why_link_fails(self):
        self.write("decisions/d.md", GOOD_DECISION)
        self.write("interviews/talk.md", INTERVIEW)
        with tempfile.TemporaryDirectory() as specs:
            (Path(specs) / "spec.md").write_text(
                f"### Requirement: X\nMUST hold. ([why]({(self.bundle / 'decisions' / 'gone.md').as_posix()}))",
                encoding="utf-8")
            self.assertEqual(main([str(self.bundle), "--check-specs", specs]), 1)

    def test_check_specs_resolving_why_link_passes(self):
        self.write("decisions/d.md", GOOD_DECISION)
        self.write("interviews/talk.md", INTERVIEW)
        with tempfile.TemporaryDirectory() as specs:
            (Path(specs) / "spec.md").write_text(
                f"### Requirement: X\nMUST hold. ([why]({(self.bundle / 'decisions' / 'd.md').as_posix()})) "
                "plus an [external](https://example.com) link",
                encoding="utf-8")
            self.assertEqual(main([str(self.bundle), "--check-specs", specs]), 0)

    def test_check_specs_ignores_link_in_code_span(self):
        # A link shown inside backticks documents the syntax; it must not be
        # resolved. Regression: bare `...` passed only on Windows (trailing-dot
        # stripping) and broke Linux CI.
        self.write("decisions/d.md", GOOD_DECISION)
        self.write("interviews/talk.md", INTERVIEW)
        with tempfile.TemporaryDirectory() as specs:
            (Path(specs) / "spec.md").write_text(
                "Every requirement carries a `([why](...))` link.\n"
                f"### Requirement: X\nMUST hold. ([why]({(self.bundle / 'decisions' / 'd.md').as_posix()}))",
                encoding="utf-8")
            self.assertEqual(main([str(self.bundle), "--check-specs", specs]), 0)

    def test_check_specs_superseded_citation_fails(self):
        self.write("decisions/new.md", GOOD_DECISION)
        self.write("decisions/old.md", GOOD_DECISION.replace(
            "status: accepted", "status: superseded").replace(
            "Evidence:", "Superseded by [new](../decisions/new.md). Evidence:"))
        self.write("interviews/talk.md", INTERVIEW)
        with tempfile.TemporaryDirectory() as docs:
            (Path(docs) / "arch.md").write_text(
                f"We use X ([why]({(self.bundle / 'decisions' / 'old.md').as_posix()}))",
                encoding="utf-8")
            self.assertEqual(main([str(self.bundle), "--check-specs", docs]), 1)

    def test_bundle_internal_supersession_chain_passes(self):
        self.write("decisions/new.md", GOOD_DECISION)
        self.write("decisions/old.md", GOOD_DECISION.replace(
            "status: accepted", "status: superseded").replace(
            "Evidence:", "Superseded by [new](../decisions/new.md). Evidence:"))
        self.write("interviews/talk.md", INTERVIEW)
        with tempfile.TemporaryDirectory() as docs:
            (Path(docs) / "arch.md").write_text(
                f"We use X ([why]({(self.bundle / 'decisions' / 'new.md').as_posix()}))",
                encoding="utf-8")
            self.assertEqual(main([str(self.bundle), "--check-specs", docs]), 0)

    def test_check_specs_accepts_single_file(self):
        self.write("decisions/new.md", GOOD_DECISION)
        self.write("decisions/old.md", GOOD_DECISION.replace(
            "status: accepted", "status: superseded").replace(
            "Evidence:", "Superseded by [new](../decisions/new.md). Evidence:"))
        self.write("interviews/talk.md", INTERVIEW)
        with tempfile.TemporaryDirectory() as docs:
            bad = Path(docs) / "readme.md"
            bad.write_text(
                f"[gone](nope.md) and X ([why]({(self.bundle / 'decisions' / 'old.md').as_posix()}))",
                encoding="utf-8")
            self.assertEqual(main([str(self.bundle), "--check-specs", str(bad)]), 1)
            good = Path(docs) / "clean.md"
            good.write_text(
                f"X ([why]({(self.bundle / 'decisions' / 'new.md').as_posix()}))",
                encoding="utf-8")
            self.assertEqual(main([str(self.bundle), "--check-specs", str(good)]), 0)

    def test_check_specs_repeatable(self):
        self.write("decisions/d.md", GOOD_DECISION)
        self.write("interviews/talk.md", INTERVIEW)
        with tempfile.TemporaryDirectory() as ok_dir, tempfile.TemporaryDirectory() as bad_dir:
            (Path(ok_dir) / "fine.md").write_text("no links here", encoding="utf-8")
            (Path(bad_dir) / "broken.md").write_text("[gone](nope.md)", encoding="utf-8")
            self.assertEqual(
                main([str(self.bundle), "--check-specs", ok_dir, "--check-specs", bad_dir]), 1)

    def test_fact_evidence_accepted(self):
        # v1.0: an attributed fact (domain/ or systems/) is valid Decision evidence
        (self.bundle / "domain").mkdir()
        self.write("domain/tenant.md",
                   "---\ntype: Term\nsource: Ivan\ntimestamp: 2026-07-08T09:00:00Z\n---\nA tenant is one org.")
        self.write("decisions/d.md", GOOD_DECISION.replace(
            "[interview](../interviews/talk.md)", "[fact](../domain/tenant.md)"))
        self.assertEqual(validate(self.bundle), [])

    def test_source_without_timestamp_reported(self):
        self.write("decisions/d.md", GOOD_DECISION)
        self.write("interviews/talk.md", INTERVIEW)
        (self.bundle / "constraints").mkdir()
        self.write("constraints/eur.md", "---\ntype: Constraint\nsource: Ivan\n---\nEUR only.")
        errs = validate(self.bundle)
        self.assertTrue(any("missing required `timestamp`" in e and "constraints" in e for e in errs))

    def test_v01_interview_evidence_still_valid(self):
        # regression: v0.1 bundles (interview evidence, no source fields) stay conformant
        self.write("decisions/d.md", GOOD_DECISION)
        self.write("interviews/talk.md", INTERVIEW)
        self.assertEqual(validate(self.bundle), [])

    def test_check_diff_scope_hit(self):
        self.write("decisions/d.md", GOOD_DECISION.replace(
            "status: accepted", "status: accepted\nscope: index.html src/auth/*"))
        self.write("interviews/talk.md", INTERVIEW)
        hits = check_diff(self.bundle, ["src/auth/login.js", "README.md", "index.html"])
        self.assertEqual(len(hits), 1)
        self.assertIn("decisions/d.md", hits[0])
        self.assertIn("accepted", hits[0])
        self.assertIn("index.html", hits[0])
        self.assertIn("src/auth/login.js", hits[0])
        self.assertNotIn("README.md", hits[0])

    def test_check_diff_no_scope_no_match_no_error(self):
        # decisions without scope are skipped; unmatched paths produce no hits;
        # advisory output never fails the run
        self.write("decisions/d.md", GOOD_DECISION)
        self.write("decisions/scoped.md", GOOD_DECISION.replace(
            "status: accepted", "status: accepted\nscope: src/*"))
        self.write("interviews/talk.md", INTERVIEW)
        self.assertEqual(check_diff(self.bundle, ["docs/readme.md"]), [])
        self.assertEqual(main([str(self.bundle), "--check-diff", "docs/readme.md"]), 0)
        self.assertEqual(main([str(self.bundle), "--check-diff", "src/app.js"]), 0)

    def test_check_diff_windows_paths_normalized(self):
        self.write("decisions/d.md", GOOD_DECISION.replace(
            "status: accepted", "status: accepted\nscope: src/auth/*"))
        self.write("interviews/talk.md", INTERVIEW)
        hits = check_diff(self.bundle, ["src\\auth\\login.js"])
        self.assertEqual(len(hits), 1)

    def test_check_bloat_advisory_only(self):
        self.write("decisions/d.md", GOOD_DECISION)
        self.write("interviews/talk.md", INTERVIEW)
        self.assertEqual(check_bloat(self.bundle), [])
        self.write("interviews/huge.md", INTERVIEW + "x" * 9000)
        hits = check_bloat(self.bundle)
        self.assertEqual(len(hits), 1)
        self.assertIn("interviews/huge.md", hits[0])
        self.assertIn("tokens per agent read", hits[0])
        self.assertEqual(main([str(self.bundle)]), 0)  # advisory: never fails

    def test_exit_codes(self):
        self.write("decisions/d.md", GOOD_DECISION)
        self.write("interviews/talk.md", INTERVIEW)
        self.assertEqual(main([str(self.bundle)]), 0)
        self.write("decisions/bad.md", "no frontmatter")
        self.assertEqual(main([str(self.bundle)]), 1)
        self.assertEqual(main([str(self.bundle / "does-not-exist")]), 1)


if __name__ == "__main__":
    unittest.main()
