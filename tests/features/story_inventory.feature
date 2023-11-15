@api
Feature: Check Store_invetory[GET] request

  @positive
  Scenario: Send GET store invetory request (successful)
    When I send "GET" "store/invetory" request
    Then response status should be "200" OK
    And response body schema should be valid by "story_inventory_schema"
