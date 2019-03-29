from logger import logger

from src.core.utils.json_validator import JsonValidator
from src.pivotal_services.base_service import BaseService


class ProjectService(BaseService):

    def __init__(self):
        BaseService.__init__(self)
        self.project_url = "/projects"

    def get_all_projects(self):
        return self.request_handler.get_request(self.config.get_base_url() + self.project_url)

    def create_project(self, name):
        return self.request_handler.post_request(self.project_url, name)


    def validate_project_schema(self, project_response):
        try:
            JsonValidator.json_validator(project_response, open("path_to_json_schema").json())
            return True, None
        except Exception as e:
            logger.info("Schema Validation Failed with: %s" % e.message())
            return False, e.message