import json
import threading
import unittest
import urllib.error
import urllib.request

import app


class ServiceTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.server = app.make_server(0, "127.0.0.1")
        cls.base = f"http://127.0.0.1:{cls.server.server_address[1]}"
        cls.thread = threading.Thread(target=cls.server.serve_forever, daemon=True)
        cls.thread.start()

    @classmethod
    def tearDownClass(cls):
        cls.server.shutdown()
        cls.server.server_close()

    def get(self, path):
        with urllib.request.urlopen(self.base + path, timeout=3) as r:
            return r.status, json.load(r)

    def test_root_greets(self):
        status, body = self.get("/")
        self.assertEqual(status, 200)
        self.assertIn("message", body)

    def test_healthz_ok(self):
        status, body = self.get("/healthz")
        self.assertEqual(status, 200)
        self.assertEqual(body["status"], "ok")

    def test_notes_list(self):
        status, body = self.get("/notes")
        self.assertEqual(status, 200)
        self.assertEqual(len(body), 3)
        self.assertEqual(body[0]["id"], 1)

    def test_unknown_path_is_404(self):
        with self.assertRaises(urllib.error.HTTPError) as ctx:
            self.get("/nope")
        self.assertEqual(ctx.exception.code, 404)


if __name__ == "__main__":
    unittest.main()
