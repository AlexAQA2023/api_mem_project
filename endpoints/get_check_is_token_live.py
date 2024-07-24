import requests
import allure

from endpoints.base_api import BaseApi, base_url


class GetLiveToken(BaseApi):
    @allure.step('Check whether if token is still alive')
    def check_token_is_live(self, token):
        self.response = requests.get(f'{base_url}/authorize/{token}')
        try:
            self.response_json = self.response.json()
        except requests.exceptions.JSONDecodeError:
            print(f"Failed to decode JSON response. Status code: {self.response.status_code}")
            print(f"Response text: {self.response.text}")
            self.response_json = {}
        print(self.response_json)
