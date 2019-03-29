import requests
import json


class RequestHandler:

    def __init__(self, header, base_url):
        self.header = header
        self.base_url = base_url

    def get_request(self, url):
        return requests.get(url=self.base_url + url, headers=self.header)

    def post_request(self, url, body):
        return requests.post(url=self.base_url + url, data=json.dumps(body), headers=self.header)

    def put_request(self, url, body):
        return requests.put(url=self.base_url + url, data=json.dumps(body), headers=self.header)

    def delete_request(self, url):
        return requests.delete(url=self.base_url + url, headers=self.header)
