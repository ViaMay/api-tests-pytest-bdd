@api
Feature: Check User[Post] create request

  @positive
  Scenario Outline: Login user (successful) request
    When I send "GET" "user/login" request with parameters: "?username=a&password=a"
    Then response status should be "200"
    And response body should contain "<message>"

    Examples:
      | message                                                         |
      | {"code":200,"type":"unknown","message":"logged in user session: |
