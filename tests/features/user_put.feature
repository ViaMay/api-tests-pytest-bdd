@api
Feature: Check User[PUT] request

  @positive
  Scenario: PUT user by username (successful) request with created username
    Given I create data with random json parameters:
      """
      {
        "id": 0,
        "username": "RANDOM_USERNAME",
        "firstName": "firstName_test_put",
        "lastName": "lastName_test_put",
        "email": "email_put@test.com",
        "password": "password_test_put",
        "phone": "+71111111111",
        "userStatus": 0
       }
      """
    And I send "POST" "user" request with created json data
    And response status should be "200"
    And I remember created username
    And I create data with random json parameters:
      """
      {
        "id": 0,
        "username": "RANDOM_USERNAME",
        "firstName": "firstName_test_put_2",
        "lastName": "lastName_test_put_2",
        "email": "email_put_2@test.com",
        "password": "password_test_put_2",
        "phone": "+72222222222",
        "userStatus": 0
       }
      """
    When I send "PUT" "user/" request with created "username" with created json data
    Then response status should be "200"
    And response body schema should be valid by "successful_default_schema"
    And I send "GET" "user/" request with created "username"
    And response body "firstName" should be equal "firstName_test_put_2"
    And response body "lastName" should be equal "lastName_test_put_2"
    And response body "email" should be equal "email_put_2@test.com"
    And response body "password" should be equal "password_test_put_2"
    And response body "phone" should be equal "+72222222222"



  @negative
  Scenario Outline: PUT user by username (unsuccessful) request
    Given I send "POST" "user" request with json parameters: "{ "username": "<username>" }"
    When I send "PUT" "user/<username>" request
    Then response status should be "405"
    And response body should be equal "<error>"
    And response body schema should be valid by "error_default_schema"

    Examples:
      | username            | error                                             |
      | username_test_error | {"code":405,"type":"unknown","message":"no data"} |