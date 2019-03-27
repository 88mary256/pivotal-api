from src.core.request_handler import RequestHandler


class BaseService:
    def __init__(self):
        #TODO: Add Property reader
        # self.property_reader =
        # {"X-TrackerToken": self.property_reader.get_token()}

        # "X-TrackerToken: $TOKEN" "https://www.pivotaltracker.com/services/v5/me?fields=%3Adefault"
        self.request_handler = RequestHandler(header={"X-TrackerToken": "4b9cc0db37214309c0937d6e459a3f6d"}, base_url="https://www.pivotaltracker.com/services/v5")