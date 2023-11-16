import json
import pytest
import time

from lib.api.api_client import ApiRequest
from lib.interfaces.extra_interfaces import I_EXTRA_STRING_TYPES, I_EXTRA_TYPES, I_EXTRA_INT_TYPES
from jsonschema import validate
from pytest_bdd import parsers, then, when, given

from lib.jsonschema.error_default_schema import error_default_schema
from lib.jsonschema.story_inventory_schema import story_inventory_schema
from lib.jsonschema.successful_default_schema import successful_default_schema
from lib.jsonschema.user_get_schema import user_get_schema
from tests.helpers.generators import replace_random_values


# Hooks
def pytest_bdd_step_error(step):
    print(f'Step failed: {step}')


def pytest_bdd_after_scenario():
    time.sleep(1)


@when(parsers.cfparse('I send "{method}" "{path}" request with parameters: "{text}"',
                      extra_types=I_EXTRA_STRING_TYPES))
def request_with_param(method, path, text):
    pytest.response = ApiRequest(method=method, path=path).request(params=text)
    return pytest.response


@given(parsers.cfparse('I send "{method}" "{path}" request with json parameters: "{text}"',
                       extra_types=I_EXTRA_STRING_TYPES))
@when(parsers.cfparse('I send "{method}" "{path}" request with json parameters: "{text}"',
                      extra_types=I_EXTRA_STRING_TYPES))
@given(parsers.parse('I send "{method}" "{path}" request with json parameters:\n{text}'))
@when(parsers.parse('I send "{method}" "{path}" request with json parameters:\n{text}'))
def request_with_json_data(method, path, text):
    params_json = json.loads(text)
    pytest.response = ApiRequest(method=method, path=path).request(params_json=params_json)
    return pytest.response


@when(parsers.parse('I send "{method}" "{path}" request', extra_types=I_EXTRA_STRING_TYPES))
def request(method, path):
    pytest.response = ApiRequest(method=method, path=path).request()
    return pytest.response


@given(parsers.cfparse('I send "{method}" "{path}" request with created json data',
                       extra_types=I_EXTRA_STRING_TYPES))
def request_with_json_saved_data(method, path):
    params_json = json.loads(pytest.json_data)
    pytest.response = ApiRequest(method=method, path=path).request(params_json=params_json)
    return pytest.response


@then(parsers.cfparse('response body schema should be valid by "{schema:String}"',
                      extra_types=I_EXTRA_STRING_TYPES))
@when(parsers.cfparse('response body schema should be valid by "{schema:String}"',
                      extra_types=I_EXTRA_STRING_TYPES))
def assert_json_schema(schema):
    print(schema)
    match schema:
        case 'story_inventory_schema':
            validate(pytest.response.json(), story_inventory_schema)
        case 'user_get_schema':
            validate(pytest.response.json(), user_get_schema)
        case 'successful_default_schema':
            validate(pytest.response.json(), successful_default_schema)
        case 'error_default_schema':
            validate(pytest.response.json(), error_default_schema)
        case _:
            print(f"Sorry, I couldn't understand {schema!r}")


@then(
    parsers.cfparse('response body "{key:String}" should be equal "{value:String}"', extra_types=I_EXTRA_STRING_TYPES))
def assert_response_body(key, value):
    response_json = json.loads(pytest.response.text)
    assert response_json[key] == value


@then(parsers.cfparse('response body should contain "{message:String}"', extra_types=I_EXTRA_STRING_TYPES))
def response_text_contain(message):
    assert message in pytest.response.text


@then(parsers.cfparse('response body should be equal "{body:String}"', extra_types=I_EXTRA_STRING_TYPES))
def response_text_equal(body):
    assert pytest.response.text == f'{body}'


@then(parsers.cfparse('response status should be "{status:Number}"', extra_types=I_EXTRA_INT_TYPES))
@given(parsers.cfparse('response status should be "{status:Number}"', extra_types=I_EXTRA_INT_TYPES))
@when(parsers.cfparse('response status should be "{status:Number}"', extra_types=I_EXTRA_INT_TYPES))
def assert_status(status):
    assert pytest.response.status_code == status


@given(parsers.parse('I create data with random json parameters:\n{text}'))
def data_create(text):
    params_json = json.loads(text)
    pytest.json_data = replace_random_values(params_json)
    return pytest.json_data
