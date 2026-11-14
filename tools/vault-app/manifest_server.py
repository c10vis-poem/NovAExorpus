#!/usr/bin/env python3
"""One-shot local page for the GitHub App manifest flow.

Serves a page at http://127.0.0.1:PORT/ with one button. The button posts a
pre-filled app manifest to GitHub; after "Create GitHub App" GitHub redirects
back to /callback?code=..., and this server writes the code to OUT_FILE and
exits. Usage: manifest_server.py PORT OUT_FILE APP_NAME
"""
import html
import json
import secrets
import sys
from http.server import BaseHTTPRequestHandler, HTTPServer
from urllib.parse import parse_qs, urlparse

PORT = int(sys.argv[1])
OUT_FILE = sys.argv[2]
APP_NAME = sys.argv[3]
STATE = secrets.token_hex(16)
DONE = []

MANIFEST = {
    "name": APP_NAME,
    "url": "https://github.com/c10vis-poem/NovAExorpus",
    "redirect_url": f"http://127.0.0.1:{PORT}/callback",
    "public": False,
    # No webhooks: the app only mints tokens inside Actions runs.
    "hook_attributes": {"url": "https://github.com/c10vis-poem/NovAExorpus", "active": False},
    # contents:write is what repository_dispatch needs; pull_requests:write lets
    # the vault's future receiver open PRs that trigger CI (GITHUB_TOKEN PRs do not).
    "default_permissions": {"contents": "write", "pull_requests": "write"},
    "default_events": [],
}

PAGE = f"""<!doctype html><meta charset="utf-8">
<meta name="viewport" content="width=device-width,initial-scale=1">
<title>Create vault app</title>
<body style="font:18px sans-serif;max-width:32em;margin:2em auto;padding:0 16px">
<p>Tap the button, then tap <b>Create GitHub App</b> on the GitHub page.</p>
<form action="https://github.com/settings/apps/new?state={STATE}" method="post">
<input type="hidden" name="manifest" value="{html.escape(json.dumps(MANIFEST))}">
<button style="font-size:20px;padding:12px 20px">Create {html.escape(APP_NAME)} on GitHub</button>
</form></body>"""


class Handler(BaseHTTPRequestHandler):
    def log_message(self, *args):
        pass

    def _send(self, body, status=200):
        data = body.encode()
        self.send_response(status)
        self.send_header("Content-Type", "text/html; charset=utf-8")
        self.send_header("Content-Length", str(len(data)))
        self.end_headers()
        self.wfile.write(data)

    def do_GET(self):
        url = urlparse(self.path)
        if url.path == "/":
            self._send(PAGE)
            return
        if url.path != "/callback":
            self._send("not found", 404)
            return
        q = parse_qs(url.query)
        if q.get("state", [""])[0] != STATE or not q.get("code"):
            self._send("State mismatch or no code; start setup.sh again.", 400)
            return
        with open(OUT_FILE, "w") as f:
            f.write(q["code"][0])
        self._send("<p style='font:18px sans-serif'>Done. Go back to Termux.</p>")
        DONE.append(True)


if __name__ == "__main__":
    server = HTTPServer(("127.0.0.1", PORT), Handler)
    while not DONE:
        server.handle_request()
    server.server_close()
