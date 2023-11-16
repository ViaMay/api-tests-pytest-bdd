@api
Feature: Check User[DELETE] request

  @only
  Scenario Outline: Delete user by username (successful) request
    Given I send "POST" "user" request with json parameters: "{ "username": "<username>" }"
    And response status should be "200"
    When I send "DELETE" "user/<username>" request
    Then response status should be "200"
    And response body should be equal "{"code":200,"type":"unknown","message":"<username>"}"
    And response body schema should be valid by "successful_default_schema"
    And I send "GET" "user/<username>" request
    And response status should be "404"

    Examples:
      | username             |
      | username_test_delete |


  @negative
  Scenario: Delete user by username (unsuccessful) request
    When I send "DELETE" "user/!@#dfef345345" request
    Then response status should be "404"