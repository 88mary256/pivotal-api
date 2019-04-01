from behave import given, then, when
from src.pivotal_services.base_service import BaseService


class ProjectService(BaseService):

    def __init__(self):
        BaseService.__init__(self)
        self.project_url = "/projects"


    def get_all_projects(self):
        return self.request_handler.get_request(self.config.get_base_url() + self.project_url)