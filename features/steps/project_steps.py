
from behave import given, when, then, step
from compare import expect

import logger as logger



from src.core.utils.logger import logger_pivotal
from src.pivotal_services.project_service import ProjectService

@given(u'A connection set up')
def step_connection(context):
    context.logger = logger_pivotal()
    context.project = ProjectService()
    context.logger.set_info(u'STEP: Given A connection set up')

@given("a desirable {name} of new project")
def step_impl(context, name):
    """
    :type context: behave.runner.Context
    :type name: str
    """
    context.name = name
    context.logger.set_info(u'STEP: Given a desirable <name> of new project')
    #print context.name

@when("user makes a post to create the new project")
def step_impl(context):
    """
    :type context: behave.runner.Context
    """
    context.projects_response = context.project.new_project(context.name)
    context.logger.set_info(u'STEP: When user makes a post to create the new project')


@then("the new project is created")
def step_impl(context):
    """
    :type context: behave.runner.Context
    """
    if expect(context.projects_response.status_code) == 200:
        context.logger.set_info("Status code of projects %s" % context.projects_response.status_code)
    else:
        context.logger.set_error("Status code other than 200")
    context.logger.set_info(u'STEP: Then the new project is created')


@step("the new project has the specified project's {name}")
def step_impl(context, name):
    """
    :type context: behave.runner.Context
    :type name: str
    """

    context.list_of_projects = context.projects_response.json()
    if expect(context.list_of_projects.name) == context.name:
        context.logger.set_info("New project's name is %s" % context.list_of_projects.name)
    else:
        context.logger.set_error("No matching name")
    context.logger.set_info(u'STEP: And the new project has the specified project\'s <name>')


@given("newly projects created")
def step_impl(context):
    """
    :type context: behave.runner.Context
    """
    context.logger.set_info(u'STEP: Given newly projects created')


@when("a user wants to get all projects")
def step_impl(context):
    """
    :type context: behave.runner.Context
    """
    context.projects_response = context.project.get_all_projects()

    context.logger.set_info(u'STEP: When a user wants to get all projects')


@then("a list of all projects is retrieved")
def step_impl(context):
    """
    :type context: behave.runner.Context
    """
    context.logger.set_info("Status code of projects %s" % context.projects_response.status_code)
    context.list_of_projects = context.projects_response.json()
    context.logger.set_info("List of projects %s" % context.list_of_projects)
    context.logger.set_info(u'STEP: Then a list of all projects is retrieved')


@given("a specific project named as {name}")
def step_impl(context, name):
    """
    :type context: behave.runner.Context
    :type name: str
    """
    raise NotImplementedError(u'STEP: Given a specific project named as <name>')


@when("the user asked the desired project")
def step_impl(context):
    """
    :type context: behave.runner.Context
    """
    raise NotImplementedError(u'STEP: When the user asked the desired project')


@then("The desired project is retrieved")
def step_impl(context):
    """
    :type context: behave.runner.Context
    """
    raise NotImplementedError(u'STEP: Then The desired project is retrieved')


@step("validate project's {name} is the same")
def step_impl(context, name):
    """
    :type context: behave.runner.Context
    :type name: str
    """
    raise NotImplementedError(u'STEP: And validate project\'s <name> is the same')


@given("a random project named as {name}")
def step_impl(context, name):
    """
    :type context: behave.runner.Context
    :type name: str
    """
    raise NotImplementedError(u'STEP: Given a random project named as <name>')


@when("the user asked that random project")
def step_impl(context):
    """
    :type context: behave.runner.Context
    """
    raise NotImplementedError(u'STEP: When the user asked that random project')


@then("response with status 404")
def step_impl(context):
    """
    :type context: behave.runner.Context
    """
    raise NotImplementedError(u'STEP: Then response with status 404')


@step("a message that the project's {name} was not found")
def step_impl(context, name):
    """
    :type context: behave.runner.Context
    :type name: str
    """
    raise NotImplementedError(u'STEP: And a message that the project\'s <name> was not found')


@given("an attempt to updata a project's {oldname}")
def step_impl(context, oldname):
    """
    :type context: behave.runner.Context
    :type oldname: str
    """
    raise NotImplementedError(u'STEP: Given an attempt to updata a project\'s <oldname>')


@when("User will call the put method")
def step_impl(context):
    """
    :type context: behave.runner.Context
    """
    raise NotImplementedError(u'STEP: When User will call the put method')


@step("a new project's {newname} is specified")
def step_impl(context, newname):
    """
    :type context: behave.runner.Context
    :type newname: str
    """
    raise NotImplementedError(u'STEP: And a new project\'s <newname> is specified')


@then("the project's {oldname} no longer exits")
def step_impl(context, oldname):
    """
    :type context: behave.runner.Context
    :type oldname: str
    """
    raise NotImplementedError(u'STEP: Then the project\'s <oldname> no longer exits')


@step("the project's {newname} exists")
def step_impl(context, newname):
    """
    :type context: behave.runner.Context
    :type newname: str
    """
    raise NotImplementedError(u'STEP: And the project\'s <newname> exists')


@step("validate the same project's {id}")
def step_impl(context, id):
    """
    :type context: behave.runner.Context
    :type id: str
    """
    raise NotImplementedError(u'STEP: And validate the same project\'s <id>')


@given("an attempt to delete a project named {name}")
def step_impl(context, name):
    """
    :type context: behave.runner.Context
    :type name: str
    """
    raise NotImplementedError(u'STEP: Given an attempt to delete a project named <name>')


@when("User will call the delete method")
def step_impl(context):
    """
    :type context: behave.runner.Context
    """
    raise NotImplementedError(u'STEP: When User will call the delete method')


@step("a the project's {name} is specified to be deleted")
def step_impl(context, name):
    """
    :type context: behave.runner.Context
    :type name: str
    """
    raise NotImplementedError(u'STEP: And a the project\'s <name> is specified to be deleted')


@step("validate the project's {id} is no longer valid")
def step_impl(context, id):
    """
    :type context: behave.runner.Context
    :type id: str
    """
    raise NotImplementedError(u'STEP: And validate the project\'s <id> is no longer valid')