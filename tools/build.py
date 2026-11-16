#!/usr/bin/env python3
"""Build the static preview and verify its links and public output."""
from pathlib import Path
import shutil
import subprocess
from search import adapt_search

ROOT = Path(__file__).resolve().parents[1]

if __name__ == "__main__":
    site = ROOT / "_site"
    if site.is_symlink():
        raise RuntimeError("Build output must not be a symlink.")
    if site.exists():
        shutil.rmtree(site)
    subprocess.run(["dotnet", "tool", "run", "docfx", "--", "build", "docfx.json",
                    "--warningsAsErrors"], cwd=ROOT, check=True)
    adapt_search(ROOT)
    manifest = site / "manifest.json"
    if manifest.exists():
        local = ROOT / ".local"
        local.mkdir(exist_ok=True)
        shutil.move(manifest, local / "docfx-build-manifest.json")
    subprocess.run(["python3", "tools/check.py"], cwd=ROOT, check=True)
