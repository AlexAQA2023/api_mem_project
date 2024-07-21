from endpoints.base_api import BaseApi, base_url
import requests
import allure


class PutMeme(BaseApi):
    @allure.step('update created meme')
    def update_mem(self, payload, token):
        self.response = requests.put(
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
