@api
Feature: Check User[PUT] create request

  @only
  Scenario: PUT user by username (successful) request with created username
    Given I send "POST" "user" request with json parameters:
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
    And response status should be "200"
    When I send "PUT" "user/username_test" request with json parameters:
      """
      {
        "id": 0,
        "username": "username_test_2",
        "firstName": "firstName_test_2",
        "lastName": "lastName_test_2",
        "email": "email_2@test.com",
        "password": "password_test123",
        "phone": "+7222222222222",
        "userStatus": 0
       }
      """
    Then response status should be "200"
    And response body schema should be valid by "successful_default_schema"
    And I send "GET" "user/username_test_2" request
    And response body should be equal:
      """
      {
        "username": "username_test_2",
        "firstName": "firstName_test_2",
        "lastName": "lastName_test_2",
        "email": "email@test.com",
        "password": "password_test123",
        "phone": "+7111111111",
        "userStatus": 0
       }
      """

