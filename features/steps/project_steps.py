import pprint

from behave import given, when, then
from pip import logger

#rrch
from src.pivotal_services.project_serviice import ProjectService


@given(u'I make a connection')
def step_impl(context):
    print(u'STEP: Given I make a connection')
    context.project = ProjectService()


@when(u'I get all projects')
def step_impl(context):
    print(u'STEP: When I get all projects')
    list_of_projects = context.project.get_all_projects()
    print("Create Project status code: %s" % list_of_projects.status_code)
    print("Response:")
    res_json = list_of_projects.json()
    pprint.pprint(res_json)

    logger.info("List of projects %s" % list_of_projects)


@then(u'I validate project list is retrieved')
def step_impl(context):
    print(u'STEP: Then I validate project list is retrieved')

