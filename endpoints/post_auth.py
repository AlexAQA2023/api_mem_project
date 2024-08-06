import requests
import allure

from endpoints.base_api import BaseApi, base_url
from tests.data.headers import headers_template


class PostAuth(BaseApi):
    @allure.step('Create token')
    def create_token(self, payload, header=None):
        # headers = header if header else headers_template
        # self.response = requests.post(
        #     url=f'{base_url}/authorize',
        #     json=payload,
        #     headers=headers
        # )
        # token = self.response.json()['token']
        # return token

        self.response = requests.post(
            f'{base_url}/authorize',
            json=payload,
            headers={
                'Content-Type': 'application/json'
            }
        )
        try:
            self.response_json = self.response.json()
        except requests.exceptions.JSONDecodeError:
            print(f"Failed to decode JSON response. Status code: {self.response.status_code}")
            print(f"Response text: {self.response.text}")
            self.response_json = {}

        if self.response.status_code == 200:
            self.token = self.response.json()['token']
        else:
            self.token = None

        return self.response.json()['token']

    @allure.step('Create token w/o json payload')
    def invalid_authorize(self):
        self.response = requests.post(base_url, json='')
        print(self.response.status_code)
