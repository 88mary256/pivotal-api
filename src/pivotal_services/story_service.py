from src.core.utils.json_validator import JsonValidator
from src.pivotal_services.base_service import BaseService
from src.core.utils.logger import logger_pivotal
import json


class StoryService(BaseService):
    def __init__(self):
        BaseService.__init__(self)
        self.story_url = "/projects"

    def get_story(self, id_story, id_project):
        return self.request_handler.get_request(
            self.config.get_base_url() + self.story_url + "/" + id_project + "/stories/" + id_story)

    def delete_story(self, id_story, id_project):
        return self.request_handler.delete_request(
            self.config.get_base_url() + self.story_url + "/" + id_project + "/stories/" + id_story)

    def post_story(self, story_name, id_project):
        return self.request_handler.post_request(
            self.config.get_base_url() + self.story_url + "/" + id_project + "/stories",story_name)


    def validate_get_story_schema(self, project_response):

        try:

            with open('schema/get_story_schema.json') as json_file:
                data = json.load(json_file)
                JsonValidator.json_validator(project_response, data)
                return True, None

        except Exception as e:
            logger = logger_pivotal()
            logger.set_info("Schema Validation Failed with: %s" % e.message)
            return False, e.message


# inst = {
#     "created_at": "2019-03-26T12:00:00Z",
#     "current_state": "unstarted",
#     "description": "ignore the droids",
#     "estimate": 2,
#     "id": 555,
#     "kind": "story",
#     "labels":
#         [
#         ],
#     "name": "Bring me the passengers",
#     "owner_ids":
#         [
#         ],
#     "project_id": 99,
#     "requested_by_id": 101,
#     "story_type": "feature",
#     "updated_at": "2019-03-26T12:00:00Z",
#     "url": "http://localhost/story/show/555"
# }
#
# print StoryService.validate_get_story_schema(inst)
