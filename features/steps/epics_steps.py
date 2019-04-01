import json
import pprint
import compare

from src.pivotal_services.epic_service import EpicService
from behave import *


@given("I make a connection to epics")
def step_connection(context):
    context.service = EpicService()


@when("I get all epics of project with id {id}")
def step_get_all_epic_of_project(context, id):
    context.all_epics_response = context.service.get_all_epics(id)


@when("I get filtered epics of project with id {id} and filter {filter}")
def step_get_all_epic_of_project_with_filter(context, id, filter):
    context.all_epics_response = context.service.get_all_epics_with_filter(id, filter)


@then("I validate epic list is retrieved")
def step_validate_epics_list(context):
    compare.expect(context.all_epics_response.status_code) == 200
    epics = context.all_epics_response.json()
    pprint.pprint(epics)
    compare.expect(len(epics)) > 0


@when("I get epic with id {epic_id} from project {project_id}")
def step_get_epic_on_project(context, epic_id, project_id):
    context.epic_response = context.service.get_epic_on_project(project_id, epic_id)


@when("I get epic with id {id}")
def step_get_epic(context, id):
    context.epic_response = context.service.get_epic(id)


@when('I create epic with name "{name}" in project {project_id}')
def step_create_epic(context, name, project_id):
    context.epic_response = context.service.create_epic(name, project_id)


@when('I modify name of epic with id {epic_id} in project {project_id} to "{name}"')
def step_modify_epic(context, epic_id, project_id, name):
    context.epic_response = context.service.modify_epic(project_id, epic_id, "{'name':'" + name + "'}")


@then("I validate epic result")
def step_validate_epic(context):
    compare.expect(context.epic_response.status_code) == 200
    epic = context.epic_response.json()
    pprint.pprint(epic)
    compare.expect(epic) != ""


@step("Delete created epic")
def step_delete_epic(context):
    project_id = context.epic_response.json()["project_id"]
    epic_id = context.epic_response.json()["epic_id"]
    context.epic_delete_response = context.service.modify_epic(project_id, epic_id)


@then("Validate delete")
def step_validate_delete_epic(context):
    pprint(context.epic_delete_response.json())
    compare.expect(context.epic_response.status_code) == 200
