"""Tiny notes service: GET /, GET /healthz, GET /notes. Stdlib only."""
import json
import os
from http.server import BaseHTTPRequestHandler, ThreadingHTTPServer

NOTES = [
    {"id": 1, "text": "Learn Git"},
    {"id": 2, "text": "Write a CI pipeline"},
    {"id": 3, "text": "Ship a container"},
]


class Handler(BaseHTTPRequestHandler):
    def _send(self, status, payload):
        body = json.dumps(payload).encode("utf-8")
        self.send_response(status)
        self.send_header("Content-Type", "application/json")
        self.send_header("Content-Length", str(len(body)))
        self.end_headers()
        self.wfile.write(body)

    def do_GET(self):
        path = self.path.split("?", 1)[0]
        if path == "/":
            self._send(200, {"message": "Hello from the notes service"})
        elif path == "/healthz":
            self._send(200, {"status": "ok"})
        elif path == "/notes":
            self._send(200, NOTES)
        else:
            self._send(404, {"error": "not found"})

    def log_message(self, fmt, *args):
        pass


def make_server(port, host="0.0.0.0"):
    return ThreadingHTTPServer((host, port), Handler)


def main():
    port = int(os.environ.get("PORT", "8080"))
    make_server(port).serve_forever()


if __name__ == "__main__":
    main()
