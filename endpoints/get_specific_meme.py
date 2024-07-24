import requests
import allure
from endpoints.base_api import BaseApi, base_url


class GetSpecificMeme(BaseApi):

    @allure.step('Find specific meme by id')
    def find_meme_by_id(self, token, meme_id):
        self.response = requests.get(f'{base_url}/meme/{meme_id}',
                                     headers={
                                         'Authorization': token,
                                         'Content-Type': 'application/json'
                                     }
                                     )
        try:
            self.response_json = self.response.json()['id']
        except requests.exceptions.JSONDecodeError:
            print(f"Failed to decode JSON response. Status code: {self.response.status_code}")
            print(f"Response text: {self.response.text}")
            self.response_json = {}
        print(self.response_json)
