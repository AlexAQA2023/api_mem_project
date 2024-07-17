import requests
import allure

from endpoints.base_api import BaseApi, base_url


class GetMeme(BaseApi):

    def get_all_meme(self):
        self.response = requests.get(f'{base_url}/meme')
        self.response_json = self.response.json()

    @allure.step('Check whether if token is still alive')
    def is_token_alive(self, token):
        self.response = requests.get(f'{base_url}/authorize/{token}')
        text = self.response.text
        return text
