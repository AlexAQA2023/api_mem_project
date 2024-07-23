import requests
import allure

from endpoints.base_api import BaseApi, base_url


class GetAllMeme(BaseApi):

    @allure.step('get all memes')
    def get_all_meme(self, token):
        self.response = requests.get(f'{base_url}/meme',
                                     headers={
                                         'Authorization': f'Bearer {token}',
                                         'Content-Type': 'application/json'
                                     })
        try:
            self.response_json = self.response.json()
        except requests.exceptions.JSONDecodeError:
            print(f"Failed to decode JSON response. Status code: {self.response.status_code}")
            print(f"Response text: {self.response.text}")
            self.response_json = {}
        print(self.response_json)

@allure.step('Check whether if token is still alive')
def is_token_alive(self, token):
    self.response = requests.get(f'{base_url}/authorize/{token}')
    text = self.response.text
    return text
