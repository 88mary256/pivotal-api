Feature: Project



  #noinspection CucumberUndefinedStep
  Scenario: Get All Project
    Given I make a connection
    When I get all projects
    Then I validate project list is retrieved

  #noinspection CucumberUndefinedStep
  Scenario: create Project
    Given I make a connection to pivotal Tracker page
    When I create a project called: HolaTest
