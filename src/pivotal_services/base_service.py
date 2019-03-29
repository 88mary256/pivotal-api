from src.core.request_handler import RequestHandler


class BaseService:
    def __init__(self):
        # TODO: Add Property reader
        # self.property_reader =
        # {"X-TrackerToken": self.property_reader.get_token()}

        # "X-TrackerToken: $TOKEN" "https://www.pivotaltracker.com/services/v5/me?fields=%3Adefault"
        self.request_handler = RequestHandler(header={"X-TrackerToken": "290548f427d7f7d10b461e95036ea3a3"},
                                              base_url="https://www.pivotaltracker.com/services/v5")
