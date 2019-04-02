Feature: Working with Stories on pivotal tracker

  Under this feature is covered all CRUD methods available under pivotaltracker.com API documentation.

Given Set up a connection

Scenario: : Create a project in order to CRUD Stories
  Given I create a project called P39


  Scenario Outline: Create a new story
    Given an story name: <story_name>
    Then the user makes a post to create the new story

    Examples:
      | story_name |
      | S1         |
      | S2         |
      | S3         |

  Scenario Outline: Get a specific Story by name
    Given I asks for the desired story: <story_name>
    Then The desired story is retrieved

     Examples:
      | story_name |
      | S1         |
      | S2         |

  Scenario Outline: Delete a specific Story by name
    Given I asks for the desired story to delete: <story_name>
    Then The desired story is deleted

     Examples:
      | story_name |
      | S1         |
      | S2         |


    Scenario: modify a Story
      Given a history name: s3
      Then: Modify according to the next parameters

      |story_param   | story_value     |
      |current_state | started         |
      |name          | name_modified   |