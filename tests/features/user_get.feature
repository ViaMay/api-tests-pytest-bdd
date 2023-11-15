@api
Feature: Check User[Post] create request

#  @positive
#  Scenario: Get user by username (successful) request with created username
#    When I create random user data and remember username
#    Then I get user with this username
#    And I compare data with response


  @positive
  Scenario Outline: Get user by username (successful) request
    When I send "GET" "user/<username>" request
    Then response status should be "200"
    And response body "username" should be equal "<username>"

    Examples:
      | username |
      | test     |
      | a        |

  @negative
  Scenario Outline: Get new user (unsuccessful) request
    When I send "GET" "user/" request
    Then response status should be "405"
    And response body should be equal "<error>"

    Examples:
      | error                         |
      | {"code":405,"type":"unknown"} |

