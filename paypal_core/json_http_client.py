import json
from braintreehttp import HttpClient

class JsonHttpClient(HttpClient):

    def parse_response_body(self, resp):
        return json.loads(resp.text)