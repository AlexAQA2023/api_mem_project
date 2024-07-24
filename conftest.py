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

# @pytest.fixture(scope='session')
# def create_token():
#     return PostAuth()
BASE_URL = "http://167.172.172.115:52355"
AUTH_ENDPOINT = "/authorize"


@pytest.fixture
def get_token():
    payload = {
        "name": "string"
    }
    response = requests.post(f"{BASE_URL}{AUTH_ENDPOINT}", json=payload)
    if response.status_code == 200:
        try:
            token = response.json().get('token')
            if token:
                return token
            else:
                pytest.fail(f"Token not found in response: {response.json()}")
        except ValueError:
            pytest.fail(f"Failed to parse JSON response: {response.text}")
    else:
        pytest.fail(f"Authorization failed. Status code: {response.status_code}")


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
def create_default_meme():
    payload = default_meme_payload
    headers = {
        'Authorization': f'Bearer {token}',
    }

    response = requests.post(f'{base_url}/meme', headers=headers, json=payload)

    print(response.json())
    default_meme__id = response.json()['id']
    print(f'Created meme with id {response.json()["id"]}')
    yield default_meme__id
    requests.delete(f'{base_url}/{default_meme__id}')
    print(f'Deleted meme with id {default_meme__id}')


@pytest.fixture()
def delete_default_meme(create_default_meme):
    pass
