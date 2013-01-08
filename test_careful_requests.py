# -*- coding: utf-8 -*-

import json
import unittest

from careful_requests import Careful
from careful_requests.utils import lower_keys

class TestCarefulHTTPAdapter(unittest.TestCase):
    def setUp(self):
        self.session = Careful(config={"base_headers": {}})

    def test_skip_accept_encoding(self):
        response = self.session.get("http://httpbin.org/get", headers={}, config={"base_headers": {}})
        request_headers = lower_keys(response.request.headers)
        response_headers = lower_keys(json.loads(response.text)["headers"])
        self.assertIn("host", response_headers)
        self.assertNotIn("accept-encoding", response_headers)

    def test_https(self):
        response = self.session.get("https://httpbin.org/get", headers={}, config={"base_headers": {}})
        self.assertIn("host", lower_keys(json.loads(response.text)["headers"]))

    def test_https_skip_accept_encoding(self):
        response = self.session.get("https://httpbin.org/get", headers={}, config={"base_headers": {}})
        self.assertNotIn("accept-encoding", lower_keys(json.loads(response.text)["headers"]))

if __name__ == "__main__":
    unittest.main()
