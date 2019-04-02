from src.pivotal_services.base_service import BaseService


class ProjectService(BaseService):

    def __init__(self):
        BaseService.__init__(self)
        self.project_url = "https://www.pivotaltracker.com/services/v5/projects"

    def get_all_projects(self):
        return self.request_handler.get_request(self.project_url)

    def new_project(self, name):
        body = "{\"name\":\""+name+"\"}"
        return self.request_handler.post_request(self.project_url, body)

    def get_project(self, project_id):
        id = 9999999 if project_id is None else project_id
        return self.request_handler.get_request(self.project_url + "/" + id)

    def update_project(self, id, name):
        return self.request_handler.put_request(self.project_url + "/" + id, name)

    def delete_project(self, id):
        return self.request_handler.delete_request(self.project_url + "/" + id)