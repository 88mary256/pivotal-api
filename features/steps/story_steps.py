import pprint

from behave import *
from compare import expect

from src.core.utils.logger import logger_pivotal

from src.pivotal_services.story_service import StoryService
@given(u'Set up a connection')
def step_impl(context):
    context.story = StoryService()
    context.logger = logger_pivotal()
    context.logger.set_info(u'Set up a connection')


@given(u'a specific story with ID: {story_id} that belongs to a {project_id}')
def step_impl(context, story_id, project_id):
    context.story_id = story_id
    context.project_id = project_id
    context.logger.set_info(u'STEP: Given a specific story with ID: {story_id} that belongs to a {project_id}')


@when(u'the user asks for the desired story')
def step_impl(context):
    context.story_response = context.story.get_story(context.story_id, context.project_id)
    context.logger.set_info("GET Story status code: %s" % context.story_response.status_code)


@then(u'The desired story is retrieved')
def step_impl(context):

    res_json = context.story_response.json()
    context.logger.set_info(res_json)
    project_schema, error = context.story.validate_get_story_schema(res_json)
    print project_schema
    print error
    assert project_schema, "Failed validating json schema %s"+ error



@given(u'a story with ID: {story_id} to delete  that belongs to a {project_id}')
def step_impl(context, story_id, project_id):
    context.story_id = story_id
    context.project_id = project_id
    context.logger.set_info(u'STEP: Given a specific story with ID: {story_id} that belongs to a {project_id}')

@when(u'the user deletes the desired story')
def step_impl(context):
    context.story_response = context.story.delete_story(context.story_id, context.project_id)
    context.logger.set_info("DELETE Story status code: %s" % context.story_response.status_code)

@then(u'The selected story was deleted')
def step_impl(context):
    print u'The selected story was deleted'



@given(u'a {project_id} of the project and {story_name}')
def step_impl(context,project_id,story_name):
    context.project_id = project_id
    context.story_name = story_name
    context.logger.set_info(u'STEP: Given a name story: {story_name} that will belong to a {project_id}')

@when(u'user makes a post to create the new project and story')
def step_impl(context):
    context.story_add = context.story.post_story(context.story_name, context.project_id)
    context.logger.set_info("POST Story status code: %s" % context.story_add.status_code)
    res_json = context.story_add.json()
    context.logger.set_info(res_json)



