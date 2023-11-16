@api
Feature: Check User_login[GET] create request

  @positive
  Scenario Outline: Login user (successful) request
    When I send "GET" "user/login" request with parameters: "?username=a&password=a"
    Then response status should be "200"
    And response body should contain "<message>"
    And response body schema should be valid by "successful_default_schema"

    Examples:
      | message                                                         |
      | {"code":200,"type":"unknown","message":"logged in user session: |
