@api
Feature: Check User[Post] create request

  @positive
  Scenario Outline: Logout user (successful) request
    When I send "GET" "user/logout" request with parameters: "?username=a&password=a"
    Then response status should be "200"
    And response body should contain "<message>"

    Examples:
      | message                                     |
      | {"code":200,"type":"unknown","message":"ok" |
