import pprint

from behave import *

from src.core.utils.logger import logger_pivotal
from src.pivotal_services.project_service import ProjectService
from src.pivotal_services.story_service import StoryService

project_id = ""


@given(u'Set up a connection')
def step_impl(context):
    context.story = StoryService()
    context.logger = logger_pivotal()
    context.project = ProjectService()

@given(u'I create a project called {project_name}')
def step_impl(context, project_name):
    global project_id

    context.project = ProjectService()
    context.project_name = project_name
    body = {'name': context.project_name}
    context.project_response = context.project.new_project(body)
    context.logger.set_info("GET Story status code: %s" % context.project_response.status_code)
    res_json = context.project_response.json()
    context.logger.set_info(res_json)
    context.id_proj = res_json["id"]
    context.logger.set_info("id of the project: %s" % context.id_proj)
    project_id = context.id_proj


@given(u'an story name: {story_name}')
def step_impl(context, story_name):
    context.story_name = story_name


@then(u'the user makes a post to create the new story')
def step_impl(context):
    context.story_add = context.story.post_story(context.story_name, str(project_id))
    context.logger.set_info("POST Story status code: %s" % context.story_add.status_code)
    res_json2 = context.story_add.json()
    context.logger.set_info(res_json2)


@given(u'I asks for the desired story: {story_name}')
def step_impl(context, story_name):
    context.story_name = story_name

    context.story_response = context.story.get_all_stories(str(project_id))
    context.logger.set_info("GET ALL Story status code: %s" % context.story_response.status_code)
    context.res_json = context.story_response.json()


@then(u'The desired story is retrieved')
def step_impl(context):
    for i in range(len(context.res_json)):
        pprint.pprint(context.res_json[i])
        if context.res_json[i]["name"] == str(context.story_name):
            print context.res_json[i]["name"]
            story_id = context.res_json[i]["id"]
            context.story_response2 = context.story.get_story(str(story_id), str(project_id))
            context.logger.set_info("GET Story status code: %s" % context.story_response2.status_code)
            res_json2 = context.story_response2.json()
            context.logger.set_info(res_json2)


@given(u'I asks for the desired story to delete: {story_name}')
def step_impl(context, story_name):
    context.story_name = story_name
    context.story_response = context.story.get_all_stories(str(project_id))
    context.logger.set_info("GET ALL Story status code: %s" % context.story_response.status_code)
    context.res_json = context.story_response.json()


@then(u'The desired story is deleted')
def step_impl(context):
    for i in range(len(context.res_json)):
        # pprint.pprint(res_json[i])
        if context.res_json[i]["name"] == str(context.story_name):
            story_id = context.res_json[i]["id"]
            context.story_response2 = context.story.delete_story(str(story_id), str(project_id))
            context.logger.set_info("DEL Story status code: %s" % context.story_response2.status_code)


# @given(u'a history name: {story_name}')
# def step_impl(context, story_name):
#     context.story_name = story_name
#     context.story_response = context.story.get_all_stories(str(project_id))
#     #context.logger.set_info("GET ALL Story status code: %s" % context.story_response.status_code)
#     context.res_json = context.story_response.json()
#
#     body = {"name": "cambiaso"}
#     for i in range(len(context.res_json)):
#         # pprint.pprint(res_json[i])
#         if context.res_json[i]["name"] == str(context.story_name):
#             story_id = context.res_json[i]["id"]
#             context.logger.set_info(story_id)
#             # for row in context.table:
#             #   body[row['story_param']] = row['story_value']
#
#             context.story_response2 = context.story.put_story(str(story_id), str(project_id), body)
#             context.logger.set_info("PUT Story status code: %s" % context.story_response2.status_code)
#
# #@then(u'Modify according to the next parameters')
# #def step_impl(context):

