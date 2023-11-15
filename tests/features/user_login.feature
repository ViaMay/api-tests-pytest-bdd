@api
Feature: Check User[Post] create request

  @positive
  Scenario Outline: Login user (unsuccessful) request
    When I send "GET" "user/login" request with parameters: "?username=a&password=a"
    Then response status should be "200"
    And response body should be equal "<error>"

    Examples:
      | error                                             |
      | {"code":405,"type":"unknown","message":"no data"} |


##    And response body "name" should be equal "<name>"
##    Then response body should contain "<error>"