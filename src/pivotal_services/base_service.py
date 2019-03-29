from src.core.request_handler import RequestHandler


class BaseService:
    def __init__(self):
        #TODO: Add Property reader
        # self.property_reader =
        # {"X-TrackerToken": self.property_reader.get_token()}

        # "X-TrackerToken: $TOKEN" "https://www.pivotaltracker.com/services/v5/me?fields=%3Adefault"
        self.request_handler = RequestHandler(header={"X-TrackerToken": "88b633b0ad42d626978b021f0d1d49a6"}, base_url="https://www.pivotaltracker.com/services/v5")
        self.request_handler_post = RequestHandler(header={"X-TrackerToken": "88b633b0ad42d626978b021f0d1d49a6",
                                                           "Content-Type": "application/json"},
                                              base_url="https://www.pivotaltracker.com/services/v5")