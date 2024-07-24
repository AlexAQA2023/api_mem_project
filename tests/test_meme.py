import allure

from tests.data import payloads
from tests.data.payloads import create_meme_payload, create_meme_payload_without_text_field, \
    create_meme_payload_with_wrong_format_tag_field


@allure.feature('authorization')
@allure.story('pre-steps before main tests')
@allure.description('check user authorize procedure')
@allure.tag("Positive")
@allure.severity('Blocker')
def test_user_authorize_with_mandatory_field(create_token):
    create_token.create_token(payloads.token_payload)
    assert create_token.check_status_code_is_(200)
    assert create_token.check_response_title_is_(payloads.token_payload['name'])


@allure.feature('authorization')
@allure.story('pre-steps before main tests')
@allure.description('check user authorize procedure')
@allure.tag("Negative")
@allure.severity('High')
def test_user_authorize_with_invalid_mandatory_field(create_token):
    create_token.create_token(payloads.invalid_mandatory_field_token_payload)
    assert create_token.check_status_code_is_(400)
    assert 'Invalid parameters' in create_token.response.text


@allure.feature('authorization')
@allure.story('pre-steps before main tests')
@allure.description('check user authorize procedure')
@allure.tag("Positive")
@allure.severity('High')
def test_user_authorize_with_format_mandatory_field(create_token):
    create_token.create_token(payloads.invalid_mandatory_field_token_payload)
    assert create_token.check_status_code_is_(400)
    assert '400 Bad Request' in create_token.response.text


@allure.feature('meme set')
@allure.story('collect all meme')
@allure.description('check that user is able to get all meme')
@allure.tag("Positive")
@allure.severity('High')
def test_get_all_meme_with_valid_token(get_token, get_overall_meme_set):
    get_overall_meme_set.get_all_meme(get_token)
    assert get_overall_meme_set.check_status_code_is_(200)


@allure.feature('meme set')
@allure.story('collect all meme')
@allure.description('check that user is not able to get all meme')
@allure.tag("Negative")
@allure.severity('High')
def test_get_all_meme_without_valid_token(get_overall_meme_set, get_token):
    get_token = get_token + 'test'
    get_overall_meme_set.get_all_meme(get_token)
    assert get_overall_meme_set.check_status_code_is_(401)
    assert '401 Unauthorized' in get_overall_meme_set.response.text


@allure.feature('meme set')
@allure.story('collect all meme')
@allure.description('check that user is able to get specific meme')
@allure.tag("Negative")
@allure.severity('Positive')
def test_get_specific_meme_by_id(get_meme_by_id, create_default_meme, get_token):
    meme_id = create_default_meme
    get_meme_by_id.find_meme_by_id(get_token, 345)
    assert get_meme_by_id.check_status_code_is_(200)
    # assert get_meme_by_id.find_meme_by_id['id'] == meme_id


@allure.feature('token ')
@allure.story('token creation')
@allure.description('check that system generates user token')
@allure.tag("Blocker")
@allure.severity('Positive')
def test_is_token_alive(get_is_live_token, get_token):
    get_is_live_token.check_token_is_live(get_token)
    assert get_is_live_token.check_status_code_is_(200)
    assert 'Token is alive' in get_is_live_token.response.text


@allure.feature('meme creation')
@allure.story('meme creation capability')
@allure.description('check that system creates meme')
@allure.tag("Blocker")
@allure.severity('Positive')
def test_create_meme_with_all_field_filled(create_meme, get_token):
    create_meme.create_meme(create_meme_payload, get_token)
    assert create_meme.check_status_code_is_(200)
    assert create_meme.response_json['url'] == create_meme_payload['url']


@allure.feature('meme creation')
@allure.story('meme creation capability')
@allure.description('check that system doesnt create  meme without mandatory fields')
@allure.tag("High")
@allure.severity('Negative')
def test_create_meme_without_mandatory_text_field(create_meme, get_token):
    create_meme.create_meme(create_meme_payload_without_text_field, get_token)
    assert create_meme.check_status_code_is_(400)
    assert '400 Bad Request' in create_meme.response.text


def test_create_meme_with_wrong_format_tag_field(create_meme, get_token):
    create_meme.create_meme(create_meme_payload_with_wrong_format_tag_field, get_token)
    assert create_meme.check_status_code_is_(400)
    assert '400 Bad Request' in create_meme.response.text


def test_create_meme_with_invalid_token(create_meme, get_token):
    get_token = get_token + 'test'
    create_meme.create_meme(create_meme_payload, get_token)
    assert create_meme.check_status_code_is_(401)
    assert '401 Unauthorized' in create_meme.response.text


def test_update_meme_with_valid_data(create_default_meme, update_meme, get_token):
    token = get_token
    payload_upd = payloads.update_meme_payload
    payload_upd['id'] = create_default_meme
    update_meme.update_mem(payload_upd, token, payload_upd['id'])
    assert update_meme.check_status_code_is_(200)
    assert update_meme.response_json['text'] == payloads.update_meme_payload['text']


def test_update_meme_with_wrong_format_id_field(create_default_meme, update_meme, get_token):
    token = get_token
    payload_upd = payloads.update_meme_payload_with_invalid_id
    payload_upd['id'] = "test"
    update_meme.update_mem(payload_upd, token, payload_upd['id'])
    assert update_meme.check_status_code_is_(404)
    assert 'Not Found' in update_meme.response.text


# def test_delete_meme(create_meme, get_token, delete_meme):
#     create_meme.create_meme(create_meme_payload, get_token)
#
#
#
# def test_delete_already_deleted_meme_by_id(create_default_meme, get_token, delete_meme):
#     delete_meme.delete_meme_by_id(create_default_meme, get_token)
#     assert delete_meme.check_status_code_is_(200)
#
#
# def test_delete_alien_meme(create_meme, get_token, delete_meme):
#     not_my_meme_id = 1231
#     obsolete_token = "T0vW7i7YAmXgTXL"
#     create_meme.create_meme(create_meme_payload, get_token)
#     delete_meme.delete_meme_by_id(not_my_meme_id, obsolete_token)
#     assert delete_meme.check_status_code_is_(403)
#
#
# def test_delete_meme_by_non_existed_id(create_default_meme, get_token, delete_meme):
#     delete_meme.delete_meme_by_id(create_default_meme, get_token)
#     assert delete_meme.check_status_code_is_(404)
