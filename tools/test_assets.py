"""Check asset URLs across successive publications and nested pages."""
from pathlib import Path
from tempfile import TemporaryDirectory
import unittest
from assets import version_assets


class AssetPublicationTests(unittest.TestCase):
    def build(self, site, css):
        (site / "public").mkdir(parents=True)
        (site / "images").mkdir()
        (site / "docs").mkdir()
        (site / "public/main.css").write_text(css)
        (site / "public/entry.js").write_text('import "./main.js";')
        (site / "public/main.js").write_text('export default {};')
        (site / "images/mark.svg").write_text("<svg/>")
        (site / "index.html").write_text(
            '<link href="public/main.css"><img src="images/mark.svg">'
            '<a href="https://example.com/public/guide">External</a>')
        (site / "docs/page.html").write_text(
            '<script src="../public/entry.js"></script><img src="../images/mark.svg">')
        version_assets(site)
        return next(site.glob("public-*")).name

    def test_changed_style_cannot_reuse_the_previous_publication_url(self):
        with TemporaryDirectory() as directory:
            root = Path(directory)
            first = self.build(root / "first", "body{color:black}")
            same = self.build(root / "same", "body{color:black}")
            changed = self.build(root / "changed", "body{color:white}")
            self.assertEqual(first, same)
            self.assertNotEqual(first, changed)
            html = (root / "changed/index.html").read_text()
            self.assertIn(f'href="{changed}/main.css"', html)
            self.assertIn("https://example.com/public/guide", html)
            nested = (root / "changed/docs/page.html").read_text()
            self.assertIn(f'src="../{changed}/entry.js"', nested)
            self.assertTrue((root / "changed" / changed / "main.js").is_file())
            self.assertEqual((root / "changed/public/main.css").read_text(),
                             (root / "changed" / changed / "main.css").read_text())
            self.assertTrue((root / "changed/images/mark.svg").is_file())


if __name__ == "__main__":
    unittest.main()
