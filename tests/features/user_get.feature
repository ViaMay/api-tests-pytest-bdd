@api
Feature: Check User[Post] create request

  @positive
  Scenario: Get user by username (successful) request with created username
    Given I create data with random json parameters:
      """
      {
        "id": "RANDOM_ID",
        "username": "RANDOM_USERNAME",
        "firstName": "firstName_test",
        "lastName": "lastName_test",
        "email": "RANDOM_EMAIL",
        "password": "password",
        "phone": "RANDOM_PHONE",
        "userStatus": 0
       }
      """
    And I send "POST" "user" request with created json data
    And response status should be "200"
    When I send "GET" "user/" request with created "username"
    And response status should be "200"
    And response id should be equal created "id"
    And response body schema should be valid by "user_get_schema"


  @positive
  Scenario Outline: Get user by username (successful) request
    Given I send "POST" "user" request with json parameters: "{ "username": "<username>" }"
    And response status should be "200"
    When I send "GET" "user/<username>" request
    Then response status should be "200"
    And response body "username" should be equal "<username>"
    And response body schema should be valid by "user_get_schema"

    Examples:
      | username |
      | test     |
      | a        |

  @negative
  Scenario Outline: Get new user (unsuccessful) request
    When I send "GET" "user/" request
    Then response status should be "405"
    And response body should be equal "<error>"
    And response body schema should be valid by "error_default_schema"

    Examples:
      | error                         |
      | {"code":405,"type":"unknown"} |


  @negative
  Scenario Outline: Get new user (unsuccessful) request
    When I send "GET" "user/!@#dfef345345" request
    Then response status should be "404"
    And response body should be equal "<error>"
    And response body schema should be valid by "error_default_schema"

    Examples:
      | error                                                |
      | {"code":1,"type":"error","message":"User not found"} |

