import requests

class RequestHandler:

    def __init__(self, header, base_url):
        self.header = header
        self.base_url = base_url

    def get_request(self, url):
        return requests.get(url=self.base_url + url , headers=self.header)

    #TODO: Complete with the other methods