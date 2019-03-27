Feature: Project



  Scenario: Get Project
    Given I make a connection
    When I get all projects
    Then I validate project list is retrieved