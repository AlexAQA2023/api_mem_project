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

    @allure.step('Grab meme id')
    def check_created_meme_by_id(self, token, meme_id):
        self.response = requests.get(f'{base_url}/meme/{meme_id}',
                                     headers={
                                         'Authorization': token,
                                         'Content-Type': 'application/json'
                                     }
                                     )
