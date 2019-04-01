
Feature: Work_Space
# A Workspace is a group of projects that you can view and manage together in one page.

  Background:
    Given A connection set up

  Scenario Outline: Create WorkSpace
    Given a new <name> of workspace
    When user perform a request to create a new workspace.
    Then a new workspace is created

    Examples:
      | name            |
      | MyWorkspace     |
      | Workspace Mc    |


  Scenario: Get All WorkSpaces
    Given a list of workspaces
    When user perform a request a list.
    Then a list of all workspace is retrieved


  Scenario: Get a specific WorkSpace by Id
    Given an Id of workspace
    When user search perform a request by id
    Then workspace is displayed

  Scenario Outline: Edit a specific WorkSpace by Id
    Given an <Id> of workspace
    When user perform a request to edit <name> by <new name>
    Then workspace is edited

      Examples:
        | Id   | name             | new name         |
        | 1    | MyWorkspace      | worksp@ce        |
        | 10   | Workspace Mc     | workspace_Mc     |
        | 100  | worksp@ce        | Workspace Mc     |



  Scenario: Get a specific WorkSpace by Id
    Given an Id of workspace
    When user search perform a request
    Then workspace is displayed


  Scenario: Delete WorkSpace
    Given a <name> of workspace
    When user perform a request to delete a workspace.
    Then a specified workspace is deleted
