from src.core.request_handler import RequestHandler
from src.core.utils.property_reader import PropertyReader


class BaseService:
    def __init__(self):
        # TODO: Add Property reader
        # self.property_reader =
        # {"X-TrackerToken": self.property_reader.get_token()}

        # "X-TrackerToken: $TOKEN" "https://www.pivotaltracker.com/services/v5/me?fields=%3Adefault"
        # self.request_handler = RequestHandler(header={"X-TrackerToken": "290548f427d7f7d10b461e95036ea3a3"},
        #                                      base_url="https://www.pivotaltracker.com/services/v5")

        self.config = PropertyReader()
        self.request_handler = RequestHandler(header={"X-TrackerToken": self.config.get_token()},
                                              base_url=self.config.get_base_url())
