from endpoints.base_api import BaseApi, base_url
import requests
import allure


class DeleteMeme(BaseApi):
    @allure.step('Delete meme by id')
    def delete_meme_by_id(self, meme_id, token):
        url = f'{base_url}/meme/{meme_id}'
        print(f"Sending DELETE request to URL: {url} with token: {token}")

        self.response = requests.delete(
            url,
            headers={
                'Authorization': token,
            },
        )
