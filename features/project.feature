Feature: Working with Projects on pivotal tracker

  Under this feature is covered all CRUD methods available under pivotaltracker.com API documentation.

  Each scenario will have a starting context the Given, a description of an action the When and finally
  the checked outcome with assertion.

  Background: Connection
    Given A connection set up

#  Scenario Outline: Create new project
#    Given a desirable <name> of new project
#    When user makes a post to create the new project
#    Then the new project is created
#      And the new project has the specified project's <name>
#    Examples:
#      | name            |
#      | David           |
#      | David Mc        |
#      | d@vid           |
#      | David_Mc        |
#      | David.Mc        |
#      | David/Mc        |
#      | David's project |
#
#  Scenario: Get all Projects
#    Given newly projects created
#    When a user wants to get all projects
#    Then a list of all projects is retrieved
#
#  Scenario Outline: Get a specific valid Project by name
#    Given a specific project named as <name>
#    When the user asked the desired project
#    Then The desired project is retrieved
#      And validate project's <name> is the same
#    Examples:
#      | name            |
#      | David           |
#      | David Mc        |
#      | d@vid           |
#      | David_Mc        |
#      | David.Mc        |
#      | David/Mc        |
#      | David's project |
#
#  Scenario Outline: Get a invalid specific Project
#    Given a random project named as <name>
#    When the user asked that random project
#    Then response with status 404
#      And a message that the project's <name> was not found
#    Examples:
#      | name             |
#      | D avid           |
#      | DaVid Mc         |
#      | D@vid            |
#      | David_MC         |
#      | David.MC         |
#      | David/MC         |
#      | David''s project |

  Scenario Outline: Update a project
    Given an attempt to updata a project's <oldname>
    When User will call the put method
      And a new project's <newname> is specified
    Then the project's <oldname> no longer exits
      And the project's <newname> exists
      And validate the same project's <id>
    Examples:
      | id     | oldname     | newname     |
      | 123456 | David       | Dav1d       |
      | 123456 | David Mc    | David MC    |
      | 123456 | d@vid       | David       |
      | 123456 | David_Mc    | David_MC    |
      | 123456 | David.Mc    | David.MC    |
      | 123456 | David/Mc    | David/MC    |
      | 123456 | David's pro | David's PRO |

#  Scenario Outline: Delete a project
#    Given an attempt to delete a project named <name>
#    When User will call the delete method
#      And a the project's <name> is specified to be deleted
#    Then the project's <name> no longer exits
#      And validate the project's <id> is no longer valid
#    Examples:
#      | id     | name        |
#      | 123456 | David       |
#      | 123456 | David MC    |
#      | 123456 | david       |
#      | 123456 | David_MC    |
#      | 123456 | David.MC    |
#      | 123456 | David/MC    |
#      | 123456 | David's PRO |