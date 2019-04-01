from src.pivotal_services.base_service import BaseService


class WorkspaceServices(BaseService):
    def __init__(self):
        BaseService.__init__(self)
        self.ws_url = "/my/workspaces"

    def get_all_workspaces (self):
        return self.request_handler.get_request(self.config.get_base_url() + self.ws_url)


    def post_all_workspaces (self):
        return self.request_handler.get_request(self.config.get_base_url() + self.ws_url)