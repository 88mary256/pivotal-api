import json

from behave import given, when, then, step
from compare import expect

from src.core.utils.logger import logger_pivotal
from src.pivotal_services.project_service import ProjectService

ids = {}
logger = logger_pivotal()


@given(u'A connection set up')
def step_connection(context):

    context.project = ProjectService()
    logger.set_info(u'STEP: Given A connection set up')


@given("an attempt to delete all projects")
def step_impl(context):
    """
    :type context: Specify empty workspace.
    """
    logger.set_info(u'STEP: Given an attempt to delete all projects')


@when("a delete all project request")
def step_impl(context):
    """
    :type context: iterate to deleta all projects.
    """
    context.projects_response = context.project.get_all_projects()
    context.list_of_projects = context.projects_response.json()
    for item in context.list_of_projects:
        context.project_response = context.project.delete_project(item["id"])

    logger.set_info(u'STEP: When a delete all project request')


@then("deletion is confirmed")
def step_impl(context):
    """
    :type context: deletion confirmed.
    """
    logger.set_info(u'STEP: Then deletion is confirmed')


@given("a desirable {name} of new project")
def step_impl(context, name):
    """
    :type context: Given a new name.
    :type name: str
    """
    context.name = name
    logger.set_info(u'STEP: Given a desirable <name> of new project')


@when("user makes a post to create the new project")
def step_impl(context):
    """
    :type context: post execution.
    """
    context.projects_response = context.project.new_project(context.name)
    logger.set_info(u'STEP: When user makes a post to create the new project')


@then("the new project is created")
def step_impl(context):
    """
    :type context: validate response.
    """
    if context.projects_response.status_code == 200:
        logger.set_debug("Status code response upon execution is %s" % context.projects_response.status_code)
    else:
        logger.set_error("Non expected status code = %s" % context.projects_response.status_code)
    logger.set_info(u'STEP: Then the new project is created')


@step("the new project has the specified project's {name}")
def step_impl(context, name):
    """
    :type context: Validate name of new project created.
    :type name: str
    """

    context.list_of_projects = context.projects_response.json()
    logger.set_info(context.list_of_projects)
    if context.list_of_projects["name"] == context.name:
        logger.set_debug("New project's name match name is %s" % context.list_of_projects["name"])
    else:
        logger.set_error("No match name Actual = %s Expected = %s" % context.name, context.list_of_projects["name"])
    logger.set_info(u'STEP: And the new project has the specified project\'s <name>')


@given("newly projects created")
def step_impl(context):
    """
    :type context: After the projects created on previous scenario.
    """
    logger.set_info(u'STEP: Given newly projects created')


@when("a user wants to get all projects")
def step_impl(context):
    """
    :type context: User wants to list all projects under its account.
    """
    context.projects_response = context.project.get_all_projects()
    logger.set_info(u'STEP: When a user wants to get all projects')


@then("a list of all projects is retrieved")
def step_impl(context):
    """
    :type context: Validate response.
    """

    if context.projects_response.status_code == 200:
        logger.set_debug("Status code response upon execution is %s" % context.projects_response.status_code)
        context.list_of_projects = context.projects_response.json()
        for item in context.list_of_projects:
            ids[item["name"]] = item["id"]
    else:
        logger.set_error("Non expected status code =  %s" % context.projects_response.status_code)
    logger.set_info(ids)
    logger.set_info(u'STEP: Then a list of all projects is retrieved')


@given("a specific project named as {name}")
def step_impl(context, name):
    """
    :type context: User wants detail about a specific project.
    :type name: str
    """
    context.name = name
    logger.set_info(u'STEP: Given a specific project named as <name>')


@when("the user asked the desired project")
def step_impl(context):
    """
    :type context: User get a project by name.
    """
    context.project_response = context.project.get_project(ids[context.name])
    logger.set_info(u'STEP: When the user asked the desired project %s' % ids[context.name])


@then("The desired project is retrieved")
def step_impl(context):
    """
    :type context: The request responds with success status.
    """
    if context.project_response.status_code == 200:
        logger.set_debug("Status code response upon execution is %s" % context.project_response.status_code)
    else:
        logger.set_error("Non expected status code =  %s" % context.project_response.status_code)
    logger.set_info(u'STEP: Then The desired project is retrieved')


@step("validate project's {name} is the same")
def step_impl(context, name):
    """
    :type context: Validate response with desire project by name.
    :type name: str
    """
    context.project = context.project_response.json()
    if context.project['name'] == context.name:
        logger.set_debug("New project's name match name is %s" % context.project['name'])
    else:
        logger.set_error("Non expected status code =  %s" % context.projects_response.status_code)
    logger.set_info(u'STEP: And validate project\'s <name> is the same')


@given("an attempt to update a project's {oldname}")
def step_impl(context, oldname):
    """
    :type context: Given a name of a project.
    :type oldname: str
    """
    context.oldname = oldname
    logger.set_info(u'STEP: Given an attempt to update a project\'s <oldname>')


@step("a new project's {newname} is specified")
def step_impl(context, newname):
    """
    :type context: to change its name.
    :type newname: str
    """
    context.newname = newname
    logger.set_info(u'STEP: And a new project\'s <newname> is specified')


@when("User will call the put method")
def step_impl(context):
    """
    :type context: User request to change the project's name.
    """
    context.idproject = ids[context.oldname]
    context.project_response = context.project.update_project(context.idproject, context.newname)
    logger.set_info(u'STEP: When User will call the put method')


@then("a success message is displayed")
def step_impl(context):
    """
    :type context: Validate status code to be success.
    """
    ids[context.newname] = ids.pop(context.oldname)

    if context.project_response.status_code == 200:
        logger.set_debug("Status code response upon execution is %s" % context.project_response.status_code)
    else:
        logger.set_error("Non expected status code =  %s" % context.project_response.status_code)
    logger.set_info(u'STEP: Then a success message is displayed')


@step("the project's {oldname} no longer exits")
def step_impl(context, oldname):
    """
    :type context: Check if oldname no longer exits.
    :type oldname: str
    """
    context.actualproject = context.project.get_project(context.idproject)
    context.project = context.actualproject.json()
    if context.project['name'] != context.oldname:
        logger.set_debug("Old project's name was changed to %s" % context.project['name'])
    else:
        logger.set_error("Non existing project =  %s" % context.oldname)
    logger.set_info(u'STEP: Then the project\'s <oldname> no longer exits')


@step("the project's {newname} exists")
def step_impl(context, newname):
    """
    :type context: Validate project's name changed.
    :type newname: str
    """
    if context.project['name'] == context.newname:
        logger.set_debug("New project's name is %s" % context.project['name'])
    else:
        logger.set_error("Non expected name =  %s" % context.project['name'])
    logger.set_info(u'STEP: And the project\'s <newname> exists')


@step("validate the same project's id")
def step_impl(context):
    """
    :type context: Changed made upon same project's id.
    """
    if context.project['id'] == context.idproject:
        logger.set_debug("The specified project's id = %s was changed" % context.project['id'])
    else:
        logger.set_error("Non expected id =  %s" % context.project['id'])
    logger.set_info(u'STEP: And validate the same project\'s id')


@given("an attempt to delete a project named {name}")
def step_impl(context, name):
    """
    :type context: User delete a project by name.
    :type name: str
    """
    context.name = name
    logger.set_info(u'STEP: Given an attempt to delete a project named <name>')


@when("User will call the delete method")
def step_impl(context):
    """
    :type context: delete request.
    """
    context.idproject = ids[context.name]
    context.project_response = context.project.delete_project(context.idproject)
    logger.set_info(u'STEP: When User will call the delete method')


@then("A success message confirm deletion")
def step_impl(context):
    """
    :type context: Confirm deletion on response.
    """
    if context.project_response.status_code == 204:
        logger.set_debug("Status code response upon execution is %s" % context.project_response.status_code)
    else:
        logger.set_error("Non expected status code =  %s" % context.project_response.status_code)
    logger.set_info(u'STEP: Then A success message confirm deletion')


@step("validate the project's id no longer valid")
def step_impl(context):
    """
    :type context: behave.runner.Context
    :type id: str
    """
    context.project_deleted = context.project.get_project(context.idproject)
    if context.project_deleted.status_code == 404:
        del ids[context.name]
        logger.set_debug("Status code response upon execution is %s" % context.project_response.status_code)
    else:
        logger.set_error("Non expected status code =  %s" % context.project_response.status_code)
    logger.set_info(u'STEP: validate the project\'s id no longer valid')
