from behave import given, when, then

from src.pivotal_services.project_service import ProjectService

@given(u'A connection set up')
def step_connection(context):
    context.logger = logger_pivotal()
    context.workspace = workspace_service()
    context.logger.set_info(u'STEP: Given A connection set up')

@given(u'a new {name} of workspace')
def step_setName(context, name):
    context.name = name
    print NotImplementedError(u'STEP: Given a new MyWorkspace of workspace')


@when(u'user perform a request to create a new workspace.')
def step_post(context,name,workspace_id):
    context.work_space_response = context.work_space.new_work_space(context.name.project_ids)
    context.logger.set_info(u'STEP: When user makes a post to create the new workspace')
    print NotImplementedError(u'STEP: When user perform a request to create a new workspace.')


@then(u'a new workspace is created')
def step_create(context):
    if expect(context.work_space_response.status_code) == 200:
        context.logger.set_info("Status code of work space %s" % context.work_space_response.status_code)
    else:
        context.logger.set_error("Status code other than 200")
    context.logger.set_info(u'STEP: Then the new work space is created')

print NotImplementedError(u'STEP: Then a new workspace is created')

------------------------


@given(u'a list of workspaces')
def step_impl(context):
    context.work_space_response = context.work_space.get_all_work_space()
    logger.info("Status code of work space %s" % context.work_space_response.status_code)

    context.logger.set_info(u'STEP: When user perform a request a list ')
    print NotImplementedError(u'STEP: Given a list of workspaces')


@when(u'user perform a request a list.')
def step_list_work_space(context):
    context.work_space_response = context.work_space.get_all_projects()
    logger.info("Status code of work_space %s" % context.work_space_response.status_code)

    context.logger.set_info(u'STEP: When a user wants to get all projects')
    print NotImplementedError(u'STEP: When user perform a request a list.')


@then(u'a list of all workspace is retrieved')
def step_impl(context):
    context.logger.set_info("Status code of work_space %s" % context.work_space_response.status_code)
    context.list_of_work_space = context.work_space_response.json()
    context.logger.set_info("List of work_space %s" % context.list_of_work_space)
    context.logger.set_info(u'STEP: Then a list of all workspace is retrieved')
    print NotImplementedError(u'STEP: Then a list of all workspace is retrieved')


-----------------------------

@given(u'an Id of workspace')
def step_workid(context,workspace_id):
    context.workspace_id = workspace_id
    print NotImplementedError(u'STEP: Given an Id of workspace')


@when(u'user search perform a request by id')
def step_impl(context):
    raise NotImplementedError(u'STEP: When user search perform a request by id')


@then(u'workspace is displayed')
def step_impl(context):
    raise NotImplementedError(u'STEP: Then workspace is displayed')


@given(u'an 1 of workspace')
def step_impl(context):
    raise NotImplementedError(u'STEP: Given an 1 of workspace')


@when(u'user perform a request to edit MyWorkspace by worksp@ce')
def step_impl(context):
    raise NotImplementedError(u'STEP: When user perform a request to edit MyWorkspace by worksp@ce')


@then(u'workspace is edited')
def step_impl(context):
    raise NotImplementedError(u'STEP: Then workspace is edited')


@given(u'an 10 of workspace')
def step_impl(context):
    raise NotImplementedError(u'STEP: Given an 10 of workspace')


@when(u'user perform a request to edit Workspace Mc by workspace_Mc')
def step_impl(context):
    raise NotImplementedError(u'STEP: When user perform a request to edit Workspace Mc by workspace_Mc')


@given(u'an 100 of workspace')
def step_impl(context):
    raise NotImplementedError(u'STEP: Given an 100 of workspace')


@when(u'user perform a request to edit worksp@ce by Workspace Mc')
def step_impl(context):
    raise NotImplementedError(u'STEP: When user perform a request to edit worksp@ce by Workspace Mc')


@given(u'an 1000 of workspace')
def step_impl(context):
    raise NotImplementedError(u'STEP: Given an 1000 of workspace')


@when(u'user perform a request to edit workspace_Mc by Workspace/Mc')
def step_impl(context):
    raise NotImplementedError(u'STEP: When user perform a request to edit workspace_Mc by Workspace/Mc')


@given(u'an 34 of workspace')
def step_impl(context):
    raise NotImplementedError(u'STEP: Given an 34 of workspace')


@when(u'user perform a request to edit Workspace.Mc by Workspace\'s team')
def step_impl(context):
    raise NotImplementedError(u'STEP: When user perform a request to edit Workspace.Mc by Workspace\'s team')


@given(u'an 123 of workspace')
def step_impl(context):
    raise NotImplementedError(u'STEP: Given an 123 of workspace')


@when(u'user perform a request to edit Workspace/Mc by worksp@ce')
def step_impl(context):
    raise NotImplementedError(u'STEP: When user perform a request to edit Workspace/Mc by worksp@ce')


@given(u'an 234 of workspace')
def step_impl(context):
    raise NotImplementedError(u'STEP: Given an 234 of workspace')


@when(u'user perform a request to edit Workspace\'s team by MyWorkspace')
def step_impl(context):
    raise NotImplementedError(u'STEP: When user perform a request to edit Workspace\'s team by MyWorkspace')


@when(u'user search perform a request')
def step_impl(context):
    raise NotImplementedError(u'STEP: When user search perform a request')


@given(u'a <name> of workspace')
def step_impl(context):
    raise NotImplementedError(u'STEP: Given a <name> of workspace')


@when(u'user perform a request to delete a workspace.')
def step_impl(context):
    raise NotImplementedError(u'STEP: When user perform a request to delete a workspace.')


@then(u'a specified workspace is deleted')
def step_impl(context):
    raise NotImplementedError(u'STEP: Then a specified workspace is deleted')
