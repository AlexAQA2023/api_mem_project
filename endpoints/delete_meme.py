from endpoints.base_api import BaseApi, base_url
import requests
import allure


class DeleteMeme(BaseApi):
    @allure.step('Delete meme by id')
    def delete_meme_by_id(self, meme_id, token):
        self.response = requests.delete(
            f'{base_url}/meme/{meme_id}',

            headers={
                'Authorization': {token},
                'Content-Type': 'application/json'
            },
        )
        response_text = self.response.text
        print(response_text)
        return response_text
