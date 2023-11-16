@api
Feature: Check Store_inventory[GET] request

  @positive
  Scenario: Send GET store inventory request (successful)
    When I send "GET" "store/inventory" request
    Then response status should be "200"
    And response body schema should be valid by "story_inventory_schema"
