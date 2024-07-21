import requests
import allure

from endpoints.base_api import BaseApi, base_url
from tests.data.headers import headers_template


class PostAuth(BaseApi):
    @allure.step('Create token')
    def create_token(self, payload, header=None):
        headers = header if header else headers_template
        self.response = requests.post(
            url=f'{base_url}/authorize',
            json=payload,
            headers=headers
        )
        try:
            self.response_json = self.response.json()
        except requests.exceptions.JSONDecodeError:
            self.response_json = None
            print(f"Failed to decode JSON response. Status code: {self.response.status_code}")
            print(f"Response text: {self.response.text}")
            print(self.response_json)
