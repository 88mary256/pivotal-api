Feature: Epics

  Scenario: Get All epics of a project
    Given I make a connection to epics
    When I get all epics of project with id 2322921
    Then I validate epic list is retrieved


  Scenario: Get all epics with filter
    Given I make a connection to epics
    When I get all epics of project with id 2322921 and filter {state:unstarted}
    Then I validate epic list is retrieved

  Scenario: Get 1 epic with id from project
    Given I make a connection to epics
    When I get epic with id 164996934 from project 2322921
    Then I validate epic result

  Scenario: Get 1 epic with id
    Given I make a connection to epics
    When I get epic with id 164996934
    Then I validate epic result

  Scenario: Create epic in project
    Given I make a connection to epics
    When I create epic with name "My new epic" in project 2322921
    Then I validate epic result

  Scenario: Modify epic
    Given I make a connection to epics
    When I modify name of epic with id 164996934 in project 2322921 to "Renamed Epic"
    Then I validate epic result

  Scenario: Delete epic
    Given I make a connection to epics
    When I create epic with name "My epic to delete" in project 2322921
    And Delete created epic
    Then Validate delete
