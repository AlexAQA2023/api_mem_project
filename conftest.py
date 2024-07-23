import pytest
import requests

from endpoints.base_api import base_url
from endpoints.delete_meme import DeleteMeme
from endpoints.get_all_meme import GetAllMeme
from endpoints.get_specific_meme import GetSpecificMeme
from endpoints.post_auth import PostAuth
from endpoints.post_meme import PostMeme
from endpoints.put_meme import PutMeme
from tests.data.payloads import default_meme_payload, token_payload


@pytest.fixture(scope='session')
def create_token():
    return PostAuth()


@pytest.fixture()
def get_overall_meme_set():
    return GetAllMeme()


@pytest.fixture()
def get_meme_by_id():
    return GetSpecificMeme()


@pytest.fixture()
def delete_meme():
    return DeleteMeme()


@pytest.fixture()
def update_meme():
    return PutMeme()


@pytest.fixture()
def create_meme():
    return PostMeme()


# @pytest.fixture(scope='session')
# def extract_token(create_token):
#     return create_token


@pytest.fixture()
def create_default_meme(extract_token):
    if extract_token:
        payload = default_meme_payload
        headers = {
            'Authorization': f'Bearer {extract_token}',
            'Content-Type': 'application/json'
        }

        response = requests.post(f'{base_url}/meme', headers=headers, json=payload)

        if response.status_code == 200:
            default_meme_id = response.json()['id']
            yield default_meme_id
        else:
            print(f"Failed to DEFAULT MEME Status code: {response.status_code}")
            print(f"Response text: {response.text}")
            yield None


@pytest.fixture()
def delete_default_meme(create_default_meme):
    pass
