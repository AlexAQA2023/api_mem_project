import pytest
import requests

from endpoints.post_auth import PostAuth
from tests.data import payloads


def test_get_token(get_token):
    get_token.create_token(payloads.token_payload)
    assert get_token.check_status_code_is_(200)
    assert get_token.check_response_title_is_(payloads.token_payload['name'])


def test_get_all_meme(get_meme):
    get_meme.get_all_meme()
    assert get_meme.check_status_code_is_(200)


def test_is_token_alive(get_meme, get_fix_token):
    get_meme.is_token_alive(get_fix_token)
    assert get_meme.check_status_code_is_(200)
    assert 'Token is alive' in get_meme.response.text
