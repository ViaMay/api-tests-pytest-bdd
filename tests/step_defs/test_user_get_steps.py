import json

import pytest
from pytest_bdd import scenarios, given, parsers, then, when

from tests.step_defs.conftest import request

scenarios('../features/user_get.feature')


@when(parsers.parse('I send "GET" "user/" request with created "username"'))
def send_get_request():
    params_json = json.loads(pytest.json_data)
    pytest.response = request("GET", "user/" + params_json['username'])
    return pytest.response


@when(parsers.parse('response id should be equal created "id"'))
def response_compare():
    params_json = json.loads(pytest.json_data)
    assert pytest.response.json()['id'] == params_json['id']
