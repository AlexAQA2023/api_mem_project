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
            },
            json=payload)
        self.check_json_decoder_error()
