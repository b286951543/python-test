import requests


class HttpClient:
    def send(self, method, url, **kwargs):
        res = requests.request(method, url, **kwargs)
        return res
