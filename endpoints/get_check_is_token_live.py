import requests
import allure

from endpoints.base_api import BaseApi, base_url


class GetLiveToken(BaseApi):
    @allure.step('Check whether if token is still alive')
    def check_token_is_live(self, token):
        self.response = requests.get(f'{base_url}/authorize/{token}')
        self.response_json = self.response.json()
