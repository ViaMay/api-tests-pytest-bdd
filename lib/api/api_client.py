import requests
from lib.config.api_config import ApiConfig

default_headers = {'Content-type': 'application/json', 'accept': 'application/json'}


class ApiRequest:
    def __init__(self, path: str, method: str, headers=None):
        if headers is None:
            headers = default_headers
        self._base_url = ApiConfig.base_url
        self._path = path
        self._method = method
        self._headers = headers

    def request(self, params=None, params_json=None):
        url = self._base_url + self._path
        headers = self._headers
        print('url: ' + url)
        print('method: ' + self._method)
        if params:
            print('params: ' + params)
        if params_json:
            print('params:')
            print(params_json)
        response = requests.request(
            method=self._method,
            url=url,
            json=params_json,
            params=params,
            headers=headers,
        )
        print('Response Code:', response.status_code)
        print('Response Body:', response.text)
        return response
