"""Smoke tests for wiki_render.py — both bundles compile, all internal links resolve."""
import re
import tempfile
import unittest
from pathlib import Path

from wiki_render import render_single, render_site

ROOT = Path(__file__).resolve().parent.parent
BUNDLES = [ROOT / "docs" / "knowledge", ROOT / "example" / "knowledge"]
HREF = re.compile(r'href="([^"#]+)"')


class RenderTests(unittest.TestCase):
    def test_site_renders_and_links_resolve(self):
        for bundle in BUNDLES:
            with tempfile.TemporaryDirectory() as out:
                pages = render_site(bundle, Path(out))
                names = {p.name for p in pages}
                self.assertIn("index.html", names)
                self.assertGreater(len(pages), 1)
                for page in pages:
                    for href in HREF.findall(page.read_text(encoding="utf-8")):
                        if href.startswith(("http://", "https://")):
                            continue
                        self.assertIn(href, names,
                                      f"{bundle.name}/{page.name}: dangling link -> {href}")

    def test_site_pages_carry_disposable_contract(self):
        with tempfile.TemporaryDirectory() as out:
            for page in render_site(BUNDLES[0], Path(out)):
                self.assertIn("disposable view", page.read_text(encoding="utf-8"))

    def test_single_file_mode(self):
        html = render_single(BUNDLES[1])
        self.assertIn("<!DOCTYPE html>", html)
        self.assertIn("disposable view", html)
        # single-file links are in-page anchors, never .html files
        self.assertNotIn('href="index.html"', html)


if __name__ == "__main__":
    unittest.main()
