import pytest
import requests

from endpoints.base_api import base_url
from endpoints.delete_meme import DeleteMeme
from endpoints.get_meme import GetMeme
from endpoints.post_auth import PostAuth
from endpoints.post_meme import PostMeme
from endpoints.put_meme import PutMeme
from tests.data import payloads
from tests.data.headers import headers_template


@pytest.fixture()
def create_token():
    return PostAuth()


@pytest.fixture()
def get_meme():
    return GetMeme()

@pytest.fixture()
def delete_meme():
    return DeleteMeme()

@pytest.fixture()
def update_meme():
    return PutMeme()


@pytest.fixture()
def create_meme():
    return PostMeme()


@pytest.fixture()
def extract_token(create_token):
    payload = payloads.token_payload
    headers = headers_template

    response = requests.post(f'{base_url}/authorize', json=payload, headers=headers)

    if response.status_code == 200:
        token_id = response.json().get('token')
        return token_id
