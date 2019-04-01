from src.pivotal_services.base_service import BaseService


class ProjectService(BaseService):

    def __init__(self):
        BaseService.__init__(self)
        self.project_url = "/projects"

    def new_project(self, name):
        return self.request_handler.post_request(self.config.get_base_url() + self.project_url, name)

    def get_all_projects(self):
        return self.request_handler.get_request(self.config.get_base_url() + self.project_url)

    def get_project(self, id):
        return self.request_handler.get_request(self.config.get_base_url() + self.project_url + "/" + id)

    def update_project(self, id, name):
        return self.request_handler.put_request(self.config.get_base_url() + self.project_url + "/" + id, name)

    def delete_project(self, id):
        return self.request_handler.delete_request(self.config.get_base_url() + self.project_url + "/" + id)

'''
    def validate_project_schema(self, project_response):
        try:
            JsonValidator.json_validator(project_response, open("path_to_json_schema").json())
            return True, None
        except Exception as e:
            logger.info("Schema Validation Failed with: %s" % e.message())
            return False, e.message
'''