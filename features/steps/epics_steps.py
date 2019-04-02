import logger as logger
import json
import compare

from src.pivotal_services.epic_service import EpicService
from src.pivotal_services.project_service import ProjectService
from behave import *

project_name = "My test project88 with epic"
epic_name = "my_epic_test"


@step('Create Project with epic')
def create_default_data(context):
    project_service = ProjectService()
    response = project_service.new_project(project_name)
    # context.project_id = response["id"]
    context.project_id = 2323732
    # epic_response = context.service.create_epic(context.project_id, "{'name':'"+epic_name+"'}")
    # context.epic_id = epic_response["id"]
    context.epic_id = 4278092


@given("I make a connection to epics")
def step_connection(context):
    context.service = EpicService()


@when("I get all epics of test project")
def step_get_all_epic_of_project(context):
    context.all_epics_response = context.service.get_all_epics(context.project_id)


@when("I get filtered epics of project with id {id} and filter {filter}")
def step_get_all_epic_of_project_with_filter(context, id, filter):
    context.all_epics_response = context.service.get_all_epics_with_filter(id, filter)


@then("I validate epic list is retrieved")
def step_validate_epics_list(context):
    compare.expect(context.all_epics_response.status_code) == 200
    epics = context.all_epics_response.json()
    logger.debug(epics)
    compare.expect(len(epics)) > 0


@when("I get epic test from project test")
def step_get_epic_on_project(context):
    context.epic_response = context.service.get_epic_on_project(context.project_id, context.epic_id)


@when("I get test epic")
def step_get_epic(context):
    context.epic_response = context.service.get_epic(context.epic_id)


@when('I create epic with name "{name}" in test project')
def step_create_epic(context, name):
    context.epic_response = context.service.create_epic("{'name':'" + name + "'}", context.project_id)


@when('I modify name of epic with id {epic_id} in project {project_id} to "{name}"')
def step_modify_epic(context, epic_id, project_id, name):
    context.epic_response = context.service.modify_epic(project_id, epic_id, "{'name':'" + name + "'}")


@then("I validate epic result")
def step_validate_epic(context):
    compare.expect(context.epic_response.status_code) == 200
    epic = context.epic_response.json()
    logger.debug(epic)
    compare.expect(epic) != ""


@step("Delete created epic")
def step_delete_epic(context):
    project_id = context.epic_response.json()["project_id"]
    epic_id = context.epic_response.json()["epic_id"]
    context.epic_delete_response = context.service.modify_epic(project_id, epic_id)


@then("Validate delete")
def step_validate_delete_epic(context):
    logger.debug(context.epic_delete_response.json())
    compare.expect(context.epic_response.status_code) == 200
