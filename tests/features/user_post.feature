@api
Feature: Check User[POST] request

  @positive
  Scenario: Post new user (successful) request
    When I send "POST" "user" request with json parameters:
      """
      {
        "id": 0,
        "username": "username_test",
        "firstName": "firstName_test",
        "lastName": "lastName_test",
        "email": "email@test.com",
        "password": "password_test123",
        "phone": "+7111111111",
        "userStatus": 0
       }
      """
    Then response status should be "200"
    And response body schema should be valid by "successful_default_schema"


  @positive
  Scenario Outline: Post new user (successful) request uncorrected parameters
    When I send "POST" "user" request with json parameters: "<parameters>"
    Then response status should be "200"
    And response body schema should be valid by "successful_default_schema"

    Examples:
      | parameters          |
      | { }                 |
      | { "test": "test" }  |
      | { "error": "error"} |


  @negative
  Scenario Outline: Post new user (unsuccessful) request
    When I send "POST" "user" request
    Then response status should be "405"
    And response body should be equal "<error>"
    And response body schema should be valid by "error_default_schema"

    Examples:
      | error                                             |
      | {"code":405,"type":"unknown","message":"no data"} |