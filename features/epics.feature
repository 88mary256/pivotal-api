Feature: Epics

  Background: Create default data
    Given I make a connection to epics
    Then Create Project with epic

  Scenario: Get All epics of test project
    When I get all epics of test project
    Then I validate epic list is retrieved

  Scenario: Get test epic from test project
    When I get epic test from project test
    Then I validate epic result

  Scenario: Get test epic
    When I get test epic
    Then I validate epic result

  Scenario: Create epic in project
    Given I make a connection to epics
    When I create epic with name "My new epic" in test project
    Then I validate epic result