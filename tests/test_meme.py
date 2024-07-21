from tests.data import payloads
from tests.data.payloads import create_meme_payload, create_meme_payload_without_text_field, \
    create_meme_payload_with_wrong_format_tag_field


def test_user_authorize_with_mandatory_field(create_token):
    create_token.create_token(payloads.token_payload)
    assert create_token.check_status_code_is_(200)
    assert create_token.check_response_title_is_(payloads.token_payload['name'])


def test_user_authorize_with_invalid_mandatory_field(create_token):
    create_token.create_token(payloads.invalid_mandatory_field_token_payload)
    assert create_token.check_status_code_is_(400)
    assert 'Invalid parameters' in create_token.response.text


def test_user_authorize_with_format_mandatory_field(create_token):
    create_token.create_token(payloads.invalid_mandatory_field_token_payload)
    assert create_token.check_status_code_is_(400)
    assert '400 Bad Request' in create_token.response.text


def test_get_all_meme_with_valid_token(get_meme, extract_token):
    get_meme.get_all_meme(extract_token)
    assert get_meme.check_status_code_is_(200)


def test_get_all_meme_without_valid_token(get_meme, extract_token):
    extract_token = extract_token + 'test'
    get_meme.get_all_meme(extract_token)
    assert get_meme.check_status_code_is_(401)
    assert '401 Unauthorized' in get_meme.response.text


def test_is_token_alive(get_meme, extract_token):
    get_meme.is_token_alive(extract_token)
    assert get_meme.check_status_code_is_(200)
    assert 'Token is alive' in get_meme.response.text


def test_create_meme_with_all_field_filled(create_meme, extract_token):
    if extract_token:
        create_meme.create_meme(payload=create_meme_payload, token=extract_token)
        assert create_meme.check_status_code_is_(200)


def test_create_meme_without_mandatory_text_field(create_meme, extract_token):
    if extract_token:
        create_meme.create_meme(payload=create_meme_payload_without_text_field, token=extract_token)
        assert create_meme.check_status_code_is_(400)
        assert '400 Bad Request' in create_meme.response.text


def test_create_meme_with_wrong_format_tag_field(create_meme, extract_token):
    if extract_token:
        create_meme.create_meme(payload=create_meme_payload_with_wrong_format_tag_field, token=extract_token)
        assert create_meme.check_status_code_is_(400)
        assert '400 Bad Request' in create_meme.response.text


def test_create_meme_with_invalid_token(create_meme, extract_token):
    extract_token = extract_token + 'test'
    create_meme.create_meme(payload=create_meme_payload, token=extract_token)
    assert create_meme.check_status_code_is_(401)
    assert '401 Unauthorized' in create_meme.response.text
