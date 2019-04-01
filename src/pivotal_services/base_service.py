from src.core.request_handler import RequestHandler
from src.core.utils.property_reader import PropertyReader


class BaseService:
    def __init__(self):
        self.config = PropertyReader()
        self.request_handler = RequestHandler(header={"X-TrackerToken": self.config.get_token()},
                                              base_url=self.config.get_base_url())