import pprint

from behave import *
from pip import logger

from src.pivotal_services.project_serviice import ProjectService

@given("I make a connection to pivotal Tracker page")
def step_impl(context):
    print (u'STEP: Given I make a connection to pivotal')
    context.project = ProjectService()

@when(u'I create a project called: {name}')
def step_impl(context,name):
    print (u'STEP: When I create a project called: {name}')
    new_project = context.project.create_project(name)
    print("Create Project status code: %s" % new_project.status_code)
    print("Response:")
    res_json = new_project.json()
    pprint.pprint(res_json)
