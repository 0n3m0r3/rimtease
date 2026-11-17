"""Keep search content and worker URLs coherent across site publications."""
from pathlib import Path
from tempfile import TemporaryDirectory
import unittest

from assets import version_assets
from search import version_search_index


class SearchPublicationTests(unittest.TestCase):
    def publish(self, root, content):
        site = root / "_site"
        (site / "public").mkdir(parents=True)
        (site / "images").mkdir()
        (site / "index.json").write_text(content)
        worker = version_search_index(root, 'const response = fetch("../index.json");')
        (site / "public/search-worker.js").write_text(worker)
        (site / "index.html").write_text('<script src="public/search-worker.js"></script>')
        version_assets(site)
        return next(site.glob("public-*"))

    def test_content_change_alone_changes_the_index_and_worker_location(self):
        with TemporaryDirectory() as directory:
            root = Path(directory)
            first = self.publish(root / "first", '{"mods": ["Body"]}')
            same = self.publish(root / "same", '{"mods": ["Body"]}')
            revised = self.publish(root / "revised", '{"mods": ["Body", "BDSM"]}')
            self.assertEqual(first.name, same.name)
            self.assertNotEqual(first.name, revised.name)
            self.assertEqual((first / "search-index.json").read_text(), '{"mods": ["Body"]}')
            self.assertEqual((revised / "search-index.json").read_text(),
                             '{"mods": ["Body", "BDSM"]}')
            self.assertIn('fetch("./search-index.json")',
                          (revised / "search-worker.js").read_text())
            self.assertIn(revised.name, (revised.parent / "index.html").read_text())
