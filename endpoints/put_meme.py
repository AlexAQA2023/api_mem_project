from endpoints.base_api import BaseApi, base_url
import requests
import allure


class PutMeme(BaseApi):
    @allure.step('update created meme')
    def update_mem(self, payload, token, meme_id):
        headers = {
            'Authorization': token,
        }
        self.response = requests.put(
            url=f'{base_url}/meme/{meme_id}',
            json=payload,
            headers=headers
        )
        try:
            self.response_json = self.response.json()
        except requests.exceptions.JSONDecodeError:
            print(f"Failed to decode JSON response. Status code: {self.response.status_code}")
            print(f"Response text: {self.response.text}")
            self.response_json = {}

        print(f"Response status code: {self.response.status_code}")
        print(f"Response JSON: {self.response_json}")
