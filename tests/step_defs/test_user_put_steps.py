import json

import pytest
from pytest_bdd import scenarios, given, parsers, then, when

from tests.step_defs.conftest import request_with_json_data
from tests.step_defs.conftest import request

scenarios('../features/user_put.feature')


@when('I send "PUT" "user/" request with created "username" with created json data')
def send_put_request_with_json_data():
    params_json = pytest.json_data
    username = pytest.username
    pytest.response = request_with_json_data("PUT", "user/" + username, params_json)
    return pytest.response


@given('I remember created username')
def send_get_request():
    params_json = json.loads(pytest.json_data)
    pytest.username = params_json['username']


@then('I send "GET" "user/" request with created "username"')
def send_get_request():
    params_json = json.loads(pytest.json_data)
    pytest.response = request("GET", "user/" + params_json['username'])
    return pytest.response
