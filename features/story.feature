Feature: Working with Stories on pivotal tracker

  Under this feature is covered all CRUD methods available under pivotaltracker.com API documentation.

Background: Connection to Pivotal Tracker
    Given Set up a connection

 Scenario Outline: Get a specific Story by ID
    Given a specific story with ID: <story_id> that belongs to a <project_id>
    When the user asks for the desired story
    Then The desired story is retrieved

    Examples:
      | project_id | story_id  |
      | 2323178    | 165010347 |
      | 2323178    | 165010348 |


  Scenario Outline: DELETE a specific Story by ID
    Given a story with ID: <story_id> to delete  that belongs to a <project_id>
    When the user deletes the desired story
    Then The selected story was deleted

    Examples:
      | project_id | story_id  |
      | 2323178    | 165013839|

  Scenario Outline: Create a new story
    Given a  <project_id> of the project
    And a  <story_name> of new Story
    When user makes a post to create the new project and story
    Then the new project and story is created

     Examples:
      | project_id | story_name  |
      | 2323178    | test new    |
      | 2323178    | again test  |

