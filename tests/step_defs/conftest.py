import json
import pytest
import time

from lib.api.api_client import ApiRequest
from lib.interfaces.interfaces import EXTRA_STRING_TYPES, EXTRA_TYPES, EXTRA_INT_TYPES
from jsonschema import validate
from pytest_bdd import parsers, then, when
from lib.jsonschema.story_inventory_schema import story_inventory_schema


# Hooks
def pytest_bdd_step_error(step):
    print(f'Step failed: {step}')


def pytest_bdd_after_scenario():
    time.sleep(1)


@when(parsers.cfparse('I send "{method}" "{path}" request with parameters: "{text}"',
                      extra_types=EXTRA_STRING_TYPES))
def request(method, path, text):
    pytest.response = ApiRequest(method=method, path=path).request(params=text)
    return pytest.response


@when(parsers.cfparse('I send "{method}" "{path}" request with json parameters: "{text}"',
                      extra_types=EXTRA_STRING_TYPES), target_fixture='user_create_response')
@when(parsers.parse('I send "{method}" "{path}" request with json parameters:\n{text}'))
def user_create(method, path, text):
    params_json = json.loads(text)
    pytest.response = ApiRequest(method=method, path=path).request(params_json=params_json)
    return pytest.response


@when(parsers.parse('I send "{method}" "{path}" request', extra_types=EXTRA_STRING_TYPES))
def user_create(method, path):
    pytest.response = ApiRequest(method=method, path=path).request()
    return pytest.response


@then(parsers.cfparse('response body schema should be valid by "{schema:String}"',
                      extra_types=EXTRA_STRING_TYPES))
def assert_json_schema(schema):
    print(schema)
    match schema:
        case 'story_inventory_schema':
            validate(pytest.response.json(), story_inventory_schema)
        case _:
            print(f"Sorry, I couldn't understand {schema!r}")


@then(parsers.cfparse('response body "{key:String}" should be equal "{value:String}"', extra_types=EXTRA_STRING_TYPES))
def assert_response_body(key, value):
    response_json = json.loads(pytest.response.text)
    assert response_json[key] == value


@then(parsers.cfparse('response body should contain "{error_message:String}"', extra_types=EXTRA_STRING_TYPES))
def response_error(error_message):
    assert error_message in pytest.response.text


@then(parsers.cfparse('response body should be equal "{body:String}"', extra_types=EXTRA_STRING_TYPES))
def response_error(body):
    assert pytest.response.text == f'{body}'


@then(parsers.cfparse('response status should be "{status:Number}" {text:String}', extra_types=EXTRA_TYPES))
def assert_status(status, text):
    assert pytest.response.status_code == status


@then(parsers.cfparse('response status should be "{status:Number}"', extra_types=EXTRA_INT_TYPES))
def assert_status(status):
    assert pytest.response.status_code == status
