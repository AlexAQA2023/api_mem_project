import requests
import allure

from endpoints.base_api import BaseApi, base_url


class PostMeme(BaseApi):
    @allure.step('Create meme')
    def create_meme(self, payload, token):
        self.response = requests.post(
            f'{base_url}/meme',

            headers={
                'Authorization': token,
                'Content-Type': 'application/json'
            },
            json=payload)
        if self.response.status_code == 200:
            try:
                self.response_json = self.response.json()
            except requests.exceptions.JSONDecodeError:
                self.response_json = None
        else:
            self.response_json = None
