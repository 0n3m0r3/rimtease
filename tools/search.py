"""Adapt the pinned DocFX search assets without forking its worker or renderer."""

import json
from pathlib import Path
import re


def version_search_index(root: Path, worker: str):
    # The worker and its index share one content-versioned directory. A new
    # publication cannot reuse a cached index.json from an earlier page build.
    index = root / "_site/index.json"
    (root / "_site/public/search-index.json").write_bytes(index.read_bytes())
    return replace_once(worker, 'fetch("../index.json")', 'fetch("./search-index.json")')


def replace_once(source, before, after):
    if source.count(before) != 1:
        raise RuntimeError("DocFX search changed; review the search adapter before building.")
    return source.replace(before, after, 1)


def adapt_search(root: Path):
    version = json.loads((root / ".config/dotnet-tools.json").read_text())["tools"]["docfx"]["version"]
    if version != "2.81.0":
        raise RuntimeError("Review the search adapter when upgrading DocFX.")

    public = root / "_site/public"
    worker_path = public / "search-worker.min.js"
    ui_path = public / "search.min.js"
    worker = worker_path.read_text()
    ui = ui_path.read_text()
    worker = version_search_index(root, worker)

    # Reuse DocFX's Lunr instance, index, ranking, cache and result renderer.
    worker = replace_once(worker, "G=i=>e.search(i).map", "G=i=>searchText(w.default,e,i).map")
    # DocFX sets the tokenizer only on a cache miss. Use that same separator
    # before loading either a cached index or a freshly built one.
    separator = r"w.default.tokenizer.separator=/[\s\-.()]+/"
    worker = replace_once(worker, separator + ",", "")
    worker = replace_once(worker, "let{index:e,data:r}=await n();", separator + ";let{index:e,data:r}=await n();")
    worker = 'import { searchText } from "./search-text.js";\n' + worker

    # Keep the worker beside its module when the asset directory is versioned.
    ui = replace_once(ui, 'm+"public/search-worker.min.js"',
                      'new URL("./search-worker.min.js",import.meta.url)')

    # Pass literal text; the worker constructs required clauses after filtering.
    ui = replace_once(ui, "i=s.value,", "i=s.value.trim(),")
    ui = replace_once(ui, 's.value===""', 's.value.trim()===""')
    ui = replace_once(ui,
                      r'let e=i.replace(/\s+/g," ").split(" ").map(t=>"+"+t).join(" ");g.postMessage({q:e})',
                      'g.postMessage({q:i})')

    # Keep catalogue and documentation search in the current browsing context.
    ui = replace_once(ui, 'target="_blank"', 'target="_self"')

    # Modified bundles no longer match upstream signatures or source maps.
    # Preserve dependency license comments; never distribute misleading maps.
    for path, source in ((worker_path, worker), (ui_path, ui)):
        source = re.sub(r"// SIG // Begin signature block.*", "", source, flags=re.S)
        source = re.sub(r"^//# sourceMappingURL=.*$", "", source, flags=re.M)
        path.write_text(source)
        path.with_suffix(path.suffix + ".map").unlink()
