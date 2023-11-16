@api
Feature: Check Store_order[POST] request

  @positive
  Scenario: Post new story (successful) request
    When I send "POST" "store/order" request with json parameters:
      """
       {
        "id": 0,
        "petId": 1,
        "quantity": 1,
        "shipDate": "2023-11-15T07:34:39.471Z",
        "status": "placed",
        "complete": true
        }
       """
    And I send "POST" "user" request with created json data
    Then response status should be "200"
    And response body should be equal:
      """
      {
        "petId": 1,
        "quantity": 1,
        "shipDate": "2023-11-15T07:34:39.471+0000",
        "status": "placed",
        "complete": true
       }
      """
    And response body schema should be valid by "story_order_post_schema"
