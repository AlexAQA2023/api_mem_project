from endpoints.base_api import BaseApi, base_url
import requests
import allure


class PutMeme(BaseApi):
    @allure.step('update created meme')
    def update_mem(self, payload, token, meme_id):
        self.response = requests.put(
            f'{base_url}/meme',

            headers={
                'Authorization': token,
                'Content-Type': 'application/json'
            },
            json=payload)
        self.check_json_decoder_error()
