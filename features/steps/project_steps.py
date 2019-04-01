import logger as logger

from behave import given, when, then

from src.pivotal_services.project_service import ProjectService


@given(u'I make a connection')
def step_impl(context):
    logger.info(u'STEP: Given I make a connection')
    context.project = ProjectService()


@when(u'I get all projects')
def step_impl(context):
    context.projects_response = context.project.get_all_projects()
    logger.info("Status code of projects %s" % context.projects_response.status_code)
    context.list_of_projects = context.projects_response.json()
    logger.info("List of projects %s" % context.list_of_projects)


@then(u'I validate project list is retrieved')
def step_impl(context):
    logger.info(u'STEP: Then I validate project list is retrieved')
