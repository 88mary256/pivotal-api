import json

import requests


class RequestHandler:

    def __init__(self, header, base_url):
        self.header = header
        self.base_url = base_url

    def get_request(self, url):
        return requests.get(url=url, headers=self.header)

    def post_request(self, url):
        return requests.post(url=url, headers=self.header)

    def put_request(self, url):
        return requests.put(url=url, headers=self.header)

    def delete_request(self, url):
        return requests.delete(url=url, headers=self.header)
