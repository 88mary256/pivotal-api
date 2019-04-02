
from src.pivotal_services.base_service import BaseService


class EpicService(BaseService):

    def __init__(self):
        BaseService.__init__(self)
        self.base_url = self.config.get_base_url()

    def get_url(self, url):
        return self.base_url + url

    def get_all_epics(self, project_id):
        url = self.get_url("/projects/" + str(project_id) + "/epics")
        return self.request_handler.get_request(url)

    def get_all_epics_with_filter(self, project_id, filter):
        url = self.get_url("/projects/" + str(project_id) + "/epics?fields=" + filter)
        return self.request_handler.get_request(url)

    def get_epic_on_project(self, project_id, epic_id):
        url = self.get_url("/projects/" + str(project_id) + "/epics/" + str(epic_id))
        return self.request_handler.get_request(url)

    def get_epic(self, epic_id):
        url = self.get_url("/epics/" + str(epic_id))
        return self.request_handler.get_request(url)

    def create_epic(self, project_id, epic):
        url = self.get_url("/projects/" + str(project_id) + "/epics")
        result = self.request_handler.post_request(url, epic)
        return result

    def modify_epic(self, project_id, epic_id, epic):
        url = self.get_url("/projects/" + str(project_id) + "/epics/" + str(epic_id))
        return self.request_handler.put_request(url, epic)

    def delete_epic(self, project_id, epic_id):
        url = self.get_url("/projects/" + str(project_id) + "/epics/" + str(epic_id))
        return self.request_handler.delete_request(url)
