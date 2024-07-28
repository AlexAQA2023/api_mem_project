import requests
import random

from locust import task, HttpUser


class Meme(HttpUser):
    token: str

    def grab_token(self):
        self.response = self.client.post(
            url='http://167.172.172.115:52355/authorize',
            json={"name": "alex_aqa"}
        ).json()

        token = self.response['token']
        return token

    @task(1)
    def get_all_memes(self):
        token = self.grab_token()
        self.response = self.client.get('http://167.172.172.115:52355/meme',
                                        headers={
                                            'Authorization': token,
                                        })

    @task(3)
    def create_meme(self):
        token = self.grab_token()
        payload = {
            "info": {"sasha_aqa": "locust_try"},
            "tags": [
                "memes_it",
                "boo ga ga "
            ],
            "text": "sarcastic",
            "url": "https://images.app.goo.gl/oFezVzUcwTwmBx5j7"
        }
        self.response = self.client.post(
            f'http://167.172.172.115:52355/meme',

            headers={
                'Authorization': token,
            },
            json=payload)
