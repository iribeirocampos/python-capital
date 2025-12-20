import json


class CapitalAPIException(Exception):
    def __init__(self, response, status_code, text):
        self.code = 0
        try:
            json_res = json.loads(text)
        except ValueError:
            self.message = f"Invalid JSON error message from Binance: {response.text}"
        else:
            self.code = json_res["errorCode"]
        self.status_code = status_code
        self.response = response
        self.request = getattr(response, "request", None)

    def __str__(self):  # pragma: no cover
        return "APIError(status code=%s) || Capital.com Error: %s" % (
            self.status_code,
            self.code,
        )
