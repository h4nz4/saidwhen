"""Tests for validate.py — runnable via `python -m pytest` or `python -m unittest`."""
import tempfile
import unittest
from pathlib import Path

from validate import validate, main

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

    def test_exit_codes(self):
        self.write("decisions/d.md", GOOD_DECISION)
        self.write("interviews/talk.md", INTERVIEW)
        self.assertEqual(main([str(self.bundle)]), 0)
        self.write("decisions/bad.md", "no frontmatter")
        self.assertEqual(main([str(self.bundle)]), 1)
        self.assertEqual(main([str(self.bundle / "does-not-exist")]), 1)


if __name__ == "__main__":
    unittest.main()
