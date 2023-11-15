@api
Feature: Check User[Post] create request

  @negative
  Scenario Outline: Create new user (unsuccessful) request
    When I send "POST" "user" request
    Then response status should be "405"
    And response body should be equal "<error>"

    Examples:
      | error                                             |
      | {"code":405,"type":"unknown","message":"no data"} |


  @positive
  Scenario Outline: Create new user (successful) request uncorrected parameters
    When I send "POST" "user" request with json parameters: "<parameters>"
    Then response status should be "200"
    And response body schema should be valid by "user_create_schema"

    Examples:
      | parameters          |
      | { }                 |
      | { "test": "test" }  |
      | { "error": "error"} |


  @positive
  Scenario: Create new user (successful) request
    When I send "POST" "user" request with json parameters:
      """
      {
        "id": 0,
        "username": "username_test",
        "firstName": "firstName_test",
        "lastName": "lastName_test",
        "email": "email@test.ru",
        "password": "password_test123",
        "phone": "+7111111111",
        "userStatus": 0
       }
      """
    Then response status should be "200"
    And response body schema should be valid by "user_create_schema"
