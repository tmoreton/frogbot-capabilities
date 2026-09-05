from __future__ import annotations

import json
import unittest
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
SITE = ROOT / "site"


class SiteTests(unittest.TestCase):
    def test_required_pages_exist(self) -> None:
        for path in (
            "index.html",
            "library/index.html",
            "contribute/index.html",
            "privacy/index.html",
            "terms/index.html",
            "invite/index.html",
            "404.html",
            "CNAME",
        ):
            self.assertTrue((SITE / path).is_file(), path)

    def test_public_links_use_app_subdomain(self) -> None:
        pages = "\n".join(path.read_text() for path in SITE.rglob("*.html"))
        self.assertIn("https://app.froggybot.com/", pages)
        self.assertNotIn('href="/app', pages)

    def test_library_loads_the_same_origin_catalog(self) -> None:
        script = (SITE / "scripts/library.js").read_text()
        self.assertIn("fetch('/catalog.json'", script)
        self.assertIn("tool.enabled !== false", script)
        self.assertIn("requiredToolIds", script)

    def test_catalog_points_at_current_repository(self) -> None:
        catalog = json.loads((ROOT / "catalog.json").read_text())
        self.assertEqual(catalog["repository"], "tmoreton/frogbot-skills")


if __name__ == "__main__":
    unittest.main()
