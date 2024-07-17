import pytest
import requests

from endpoints.base_api import base_url
from endpoints.get_meme import GetMeme
from endpoints.post_auth import PostAuth
from tests.data import payloads
from tests.data.headers import headers_template


@pytest.fixture()
def get_token():
    return PostAuth()


@pytest.fixture()
def get_meme():
    return GetMeme()


@pytest.fixture()
def get_fix_token():
    payload = payloads.token_payload
    headers = headers_template
    response = requests.post(
        url=f'{base_url}/authorize',
        json=payload,
        headers=headers
    )
    token_id = response.json()['token']
    return token_id
