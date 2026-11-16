#!/usr/bin/env python3
"""Validate generated navigation, assets, anchors and public-content boundaries."""
from html.parser import HTMLParser
import json
from pathlib import Path
import re
from urllib.parse import unquote, urlsplit

ROOT = Path(__file__).resolve().parents[1]
SITE = (ROOT / "_site").resolve()

class Page(HTMLParser):
    def __init__(self, content):
        super().__init__()
        self.ids = set()
        self.links = []
        self.feed(content)

    def handle_starttag(self, tag, attrs):
        attrs = dict(attrs)
        if attrs.get("id"):
            self.ids.add(attrs["id"])
        if tag == "a" and attrs.get("name"):
            self.ids.add(attrs["name"])
        for key in ("href", "src"):
            if attrs.get(key):
                self.links.append(attrs[key])

def check():
    pages = {p.resolve(): Page(p.read_text()) for p in SITE.rglob("*.html")}
    required = ("index.html", "mods/body.html", "docs/index.html",
                "docs/visuals/body.html", "docs/visuals/health-display.html")
    errors = [f"Missing page: {name}" for name in required if (SITE / name) not in pages]
    index = SITE / "index.json"
    if not index.is_file():
        errors.append("Search index missing")
    else:
        search = json.loads(index.read_text())
        for name in required:
            if name not in search:
                errors.append(f"Page missing from search: {name}")
    checked = 0
    for path, page in pages.items():
        for link in page.links:
            url = urlsplit(link)
            if url.scheme or url.netloc or link in ("", "#"):
                continue
            if url.path.startswith("/"):
                errors.append(f"Root-relative link breaks a subdirectory preview: {link}")
                continue
            target = (path.parent / unquote(url.path)).resolve() if url.path else path
            if not target.is_relative_to(SITE):
                errors.append(f"Link escapes output: {link}")
                continue
            if target.is_dir():
                target /= "index.html"
            checked += 1
            if not target.is_file():
                errors.append(f"{path.relative_to(SITE)}: missing {link}")
            elif url.fragment and target in pages and unquote(url.fragment) not in pages[target].ids:
                errors.append(f"{path.relative_to(SITE)}: missing anchor {link}")
    private = re.compile(r"https?://(?:orbit|internal)\.[^\s\"<>]+|\b(?:RIMWE|RIMTE|RTB|RTT|DOC)-\d+\b|/home/[^/\s]+/|/mnt/[a-z]/Users/|[A-Za-z]:\\+Users\\+")
    for path in SITE.rglob("*"):
        if not path.is_file():
            continue
        if path.suffix.lower() in (".dll", ".exe", ".pdb"):
            errors.append(f"Binary included: {path.name}")
        if path.suffix.lower() in (".html", ".json", ".xml", ".md", ".yml"):
            if private.search(path.read_text(errors="replace")):
                errors.append(f"Private reference in output: {path.relative_to(SITE)}")
    if errors:
        raise SystemExit("\n".join(errors[:40]))
    print(f"Checked {len(pages)} HTML pages, {checked} local links and all five search entries; public-output boundaries passed.")

if __name__ == "__main__":
    check()
