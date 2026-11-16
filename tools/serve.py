#!/usr/bin/env python3
"""Serve the real build on loopback under a portable subdirectory."""
import argparse
from functools import partial
from http.server import SimpleHTTPRequestHandler, ThreadingHTTPServer
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
PREFIX = "/rimtease/"

class Handler(SimpleHTTPRequestHandler):
    def do_GET(self):
        if self.path in ("/", PREFIX.rstrip("/")):
            self.send_response(302)
            self.send_header("Location", PREFIX)
            self.end_headers()
            return
        if not self.path.startswith(PREFIX):
            self.send_error(404)
            return
        self.path = "/" + self.path[len(PREFIX):]
        super().do_GET()

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--port", type=int, default=8093)
    args = parser.parse_args()
    if not (ROOT / "_site/index.html").is_file():
        raise SystemExit("Build the site before starting the preview.")
    handler = partial(Handler, directory=str(ROOT / "_site"))
    print(f"Preview: http://localhost:{args.port}{PREFIX}", flush=True)
    ThreadingHTTPServer(("127.0.0.1", args.port), handler).serve_forever()
