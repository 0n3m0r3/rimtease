"""Give each generated asset directory a content-based URL before publication."""
import hashlib
from pathlib import Path
import re
from urllib.parse import urlsplit, urlunsplit


def version_assets(site: Path):
    names = {}
    for name in ("public", "images"):
        folder = site / name
        digest = hashlib.sha256()
        for path in sorted(folder.rglob("*")):
            if path.is_file():
                digest.update(path.relative_to(folder).as_posix().encode() + b"\0")
                digest.update(path.read_bytes())
                digest.update(b"\0")
        names[name] = f"{name}-{digest.hexdigest()[:16]}"
        folder.rename(site / names[name])

    def rewrite(match):
        url = urlsplit(match["url"])
        if url.scheme or url.netloc:
            return match[0]
        parts = url.path.split("/")
        for index, part in enumerate(parts):
            if part in names:
                parts[index] = names[part]
                break
        path = "/".join(parts)
        return f'{match["prefix"]}{urlunsplit(url._replace(path=path))}{match["quote"]}'

    attributes = re.compile(r"""(?P<prefix>\b(?:href|src)=(?P<quote>["']))(?P<url>[^"']+)(?P=quote)""")
    for path in site.rglob("*.html"):
        path.write_text(attributes.sub(rewrite, path.read_text()))
