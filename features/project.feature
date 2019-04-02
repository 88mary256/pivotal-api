Feature: Working with Projects on pivotal tracker

  Under this feature is covered all CRUD methods available under pivotaltracker.com API documentation.

  Each scenario will have a starting context the Given, a description of an action the When and finally
  the checked outcome with assertion.

  Background: Connection
    Given A connection set up

  Scenario: Empty existing projects
    Given an attempt to delete all projects
    When a delete all project request
    Then deletion is confirmed

  Scenario Outline: Create new project
    Given a desirable <name> of new project
    When user makes a post to create the new project
    Then the new project is created
      And the new project has the specified project's <name>
    Examples:
      | name            |
      | David           |
      | David Mc        |
      | d@vid           |
      | David_Mc        |
      | David.Mc        |
      | David/Mc        |
      | David's pro     |

  Scenario: Get all Projects
    Given newly projects created
    When a user wants to get all projects
    Then a list of all projects is retrieved

  Scenario Outline: Get a specific valid Project by name
    Given a specific project named as <name>
    When the user asked the desired project
    Then The desired project is retrieved
      And validate project's <name> is the same
    Examples:
      | name            |
      | David           |
      | David Mc        |
      | d@vid           |
      | David_Mc        |
      | David.Mc        |
      | David/Mc        |
      | David's pro     |

  Scenario Outline: Update a project
    Given an attempt to update a project's <oldname>
    When a new project's <newname> is specified
      And User will call the put method
    Then a success message is displayed
      And the project's <oldname> no longer exits
      And the project's <newname> exists
      And validate the same project's id
    Examples:
      | oldname     | newname     |
      | David       | Dav1d       |
      | David Mc    | David MC    |
      | d@vid       | David       |
      | David_Mc    | David_MC    |
      | David.Mc    | David.MC    |
      | David/Mc    | David/MC    |
      | David's pro | David's PRO |

  Scenario Outline: Delete a project
    Given an attempt to delete a project named <name>
    When User will call the delete method
    Then A success message confirm deletion
      And validate the project's id no longer valid
    Examples:
     | name        |
     | Dav1d       |
     | David MC    |
     | David       |
     | David_MC    |
     | David.MC    |
     | David/MC    |
     | David's PRO |

