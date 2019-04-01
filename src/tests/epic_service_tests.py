import pprint
import unittest

from src.pivotal_services.epic_service import EpicService

project_id = 2322921
epic_id=4275384
id_1 = 0
id_2 = 0
service = EpicService()


class TestProject(unittest.TestCase):

    def tearDown(self):
        print "tearDown"
        if (id_1 > 0):
            service.delete_epic(project_id, id_1)
        if (id_2 > 0):
            service.delete_epic(project_id, id_2)

    def test_get_all_epics(self):
        all_epics_response = service.get_all_epics(project_id)
        print(all_epics_response)
        pprint.pprint(all_epics_response.json())
        self.assertEqual(all_epics_response.status_code, 200)

    def test_get_all_epics_with_filter(self):
        all_epics_response = service.get_all_epics_with_filter(project_id,"{'state':'unstarted'}")
        print(all_epics_response)
        pprint.pprint(all_epics_response.json())
        self.assertEqual(all_epics_response.status_code, 200)

    def test_get_epic(self):
        response = service.get_epic(epic_id)
        print(response)
        pprint.pprint(response.json())
        self.assertEqual(response.status_code, 200)

    def test_get_epic_on_project(self):
        response = service.get_epic_on_project(project_id, epic_id)
        print(response)
        pprint.pprint(response.json())
        self.assertEqual(response.status_code, 200)

