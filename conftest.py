import pytest
import requests

from endpoints.base_api import base_url
from endpoints.delete_meme import DeleteMeme
from endpoints.get_all_meme import GetAllMeme
from endpoints.get_check_is_token_live import GetLiveToken
from endpoints.get_specific_meme import GetSpecificMeme
from endpoints.post_auth import PostAuth
from endpoints.post_meme import PostMeme
from endpoints.put_meme import PutMeme
from tests.data.payloads import default_meme_payload

BASE_URL = "http://167.172.172.115:52355"
AUTH_ENDPOINT = "/authorize"


@pytest.fixture(scope='session')
def get_token():
    post_auth = PostAuth()
    payload = {
        "name": "made_by_fixture"
    }
    response_json_token_inside = post_auth.create_token(payload)
    return response_json_token_inside


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


@pytest.fixture()
def get_is_live_token():
    return GetLiveToken()


@pytest.fixture()
def create_default_meme(get_token):
    payload = default_meme_payload
    headers = {
        'Authorization': get_token
    }

    response = requests.post(f'{base_url}/meme', headers=headers, json=payload)

    default_meme__id = response.json()['id']
    print(f'Created meme with id {response.json()["id"]}')
    yield default_meme__id
    requests.delete(f'{base_url}/{default_meme__id}')
    print(f'Deleted meme with id {default_meme__id}')


@pytest.fixture()
def create_user_token():
    return PostAuth()
