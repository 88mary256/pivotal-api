Feature: Project

  Scenario: Get all Projects
    Given I make a connection
    When I get all projects
    Then I validate project list is retrieved

  Scenario: Get specific Project
    Given I make a connection
    When I get the desired project
    Then I validate the project is retrieved

  Scenario: Create new project
    Given I make a connection
    When I post to create a new project
    Then I validate the new project is created
    And the new project has the specified project's name

  Scenario: Update a project
    Given I make a connection
    When I put to edit a project's name
    Then I validate the new project is updated
    And The project changed its name with the specified one

  Scenario: Delete a project
    Given I make a connection
    When I delete a specified project
    Then I recieved a confirmation on deletion
    And THe project no longer exist