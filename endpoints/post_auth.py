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
        token = self.response.json()['token']
        print(self.response.json()['token'])
        return token
