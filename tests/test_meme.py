import random

import allure

from tests.data import payloads
from tests.data.payloads import create_meme_payload, create_meme_payload_without_text_field, \
    create_meme_payload_with_wrong_format_tag_field


@allure.feature('authorization')
@allure.story('pre-steps before main tests')
@allure.description('check user authorize procedure')
@allure.tag("Positive")
@allure.severity('Blocker')
def test_user_authorize_with_mandatory_field(create_user_token):
    create_user_token.create_token(payloads.token_payload)
    assert create_user_token.check_status_code_is_(200)
    assert create_user_token.check_response_title_is_(payloads.token_payload['name'])


@allure.feature('authorization')
@allure.story('pre-steps before main tests')
@allure.description('check user authorize procedure')
@allure.tag("Negative")
@allure.severity('High')
def test_user_authorize_with_invalid_mandatory_field(create_user_token):
    create_user_token.invalid_authorize()
    create_user_token.check_status_code_is_(400)


@allure.feature('meme set')
@allure.story('collect all meme')
@allure.description('check that user is able to get all meme')
@allure.tag("Positive")
@allure.severity('High')
def test_get_all_meme_with_valid_token(get_token, get_overall_meme_set):
    get_overall_meme_set.get_all_meme(get_token)
    assert get_overall_meme_set.check_status_code_is_(200)
    assert get_overall_meme_set.is_meme_data_not_empty


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
    response = get_meme_by_id.find_meme_by_id(get_token, meme_id)
    assert get_meme_by_id.check_status_code_is_(200)
    assert response['id'] == meme_id


@allure.feature('token ')
@allure.story('token creation')
@allure.description('check that system generates user token')
@allure.tag("Blocker")
@allure.severity('Positive')
def test_is_token_alive(get_is_live_token, get_token):
    get_is_live_token.check_token_is_live(get_token)
    assert get_is_live_token.check_status_code_is_(200)
    assert get_is_live_token.check_response_text_is('Token is alive')


@allure.feature('meme creation')
@allure.story('meme creation capability')
@allure.description('check that system creates meme')
@allure.tag("Blocker")
@allure.severity('Positive')
def test_create_meme_with_all_field_filled(create_meme, get_token, get_meme_by_id):
    create_meme.create_meme(create_meme_payload, get_token)
    meme_id = create_meme.response.json()['id']
    assert create_meme.check_status_code_is_(200)
    assert get_meme_by_id.find_meme_by_id(get_token, meme_id)
    assert create_meme.response_json['url'] == create_meme_payload['url']
    assert create_meme.response_json['text'] == create_meme_payload['text']
    assert create_meme.response_json['tags'] == create_meme_payload['tags']
    assert create_meme.response_json['info'] == create_meme_payload['info']


@allure.feature('meme creation')
@allure.story('meme creation capability')
@allure.description('check that system doesnt create  meme without mandatory fields')
@allure.tag("High")
@allure.severity('Negative')
def test_create_meme_without_mandatory_text_field(create_meme, get_token):
    create_meme.create_meme(create_meme_payload_without_text_field, get_token)
    assert create_meme.check_status_code_is_(400)
    assert create_meme.check_response_text_is('400 Bad Request')


@allure.feature('meme creation')
@allure.story('meme creation capability')
@allure.description('check that system doesnt create  meme with wrong format tag field')
@allure.tag("High")
@allure.severity('Negative')
def test_create_meme_with_wrong_format_tag_field(create_meme, get_token):
    create_meme.create_meme(create_meme_payload_with_wrong_format_tag_field, get_token)
    assert create_meme.check_status_code_is_(400)
    assert create_meme.check_response_text_is('400 Bad Request')


@allure.feature('meme creation')
@allure.story('meme creation capability')
@allure.description('check that system doesnt create  meme with invalid token')
@allure.tag("High")
@allure.severity('Negative')
def test_create_meme_with_invalid_token(create_meme, get_token):
    get_token = get_token + 'test'
    create_meme.create_meme(create_meme_payload, get_token)
    assert create_meme.check_status_code_is_(401)
    assert create_meme.check_response_text_is('401 Unauthorized')


@allure.feature('meme update')
@allure.story('meme update capability')
@allure.description('check that system is able to update a mem')
@allure.tag("High")
@allure.severity('Positive')
def test_update_meme_with_valid_data(create_default_meme, update_meme, get_token, get_meme_by_id):
    token = get_token
    payload_upd = payloads.update_meme_payload
    payload_upd['id'] = create_default_meme
    update_meme.update_mem(payload_upd, token, payload_upd['id'])
    assert update_meme.check_status_code_is_(200)
    assert get_meme_by_id.find_meme_by_id(get_token, payload_upd['id'])
    assert update_meme.response_json['url'] == payloads.update_meme_payload['url']
    assert update_meme.response_json['tags'] == payloads.update_meme_payload['tags']
    assert update_meme.response_json['text'] == payloads.update_meme_payload['text']
    assert update_meme.response_json['info'] == payloads.update_meme_payload['info']


@allure.feature('meme update')
@allure.story('meme update capability')
@allure.description('check that system isnt able to update a mem with wrong format id field')
@allure.tag("High")
@allure.severity('Negative')
def test_update_meme_with_wrong_format_id_field(create_default_meme, update_meme, get_token):
    token = get_token
    payload_upd = payloads.update_meme_payload_with_invalid_id
    payload_upd['id'] = "test"
    update_meme.update_mem(payload_upd, token, payload_upd['id'])
    assert update_meme.check_status_code_is_(404)
    assert update_meme.check_response_text_is('Not Found')


@allure.feature('meme delete')
@allure.story('meme delete capability')
@allure.description('check that system is able to delete a meme')
@allure.tag("High")
@allure.severity('Positive')
def test_delete_meme(create_meme, get_token, delete_meme, get_meme_by_id):
    token = get_token
    create_meme.create_meme(create_meme_payload, token)
    meme_id = create_meme.response.json()['id']
    delete_meme.delete_meme_by_id(meme_id, token)
    assert delete_meme.check_status_code_is_(200)
    assert delete_meme.check_response_text_is(f'Meme with id {meme_id} successfully deleted')
    get_meme_by_id.find_deleted_meme_by_id(meme_id)
    assert delete_meme.check_status_code_is_(404)




@allure.feature('meme delete')
@allure.story('meme delete capability')
@allure.description('check that system isnt to able delete already deleted meme')
@allure.tag("High")
@allure.severity('Negative')
def test_delete_already_deleted_meme_by_id(create_meme, get_token, delete_meme):
    token = get_token
    create_meme.create_meme(create_meme_payload, token)
    meme_id = create_meme.response.json()['id']
    delete_meme.delete_meme_by_id(meme_id, token)
    delete_meme.delete_meme_by_id(meme_id, token)
    assert delete_meme.check_status_code_is_(404)
    assert delete_meme.check_response_text_is('Not Found')


@allure.feature('meme delete')
@allure.story('meme delete capability')
@allure.description('check that system isnt to able delete your colleagues meme')
@allure.tag("High")
@allure.severity('Negative')
def test_delete_alien_meme(create_meme, get_token, delete_meme):
    not_my_meme_id = 1231
    obsolete_token = "T0vW7i7YAmXgTXL"
    create_meme.create_meme(create_meme_payload, get_token)
    delete_meme.delete_meme_by_id(not_my_meme_id, obsolete_token)
    assert delete_meme.check_status_code_is_(403)
    assert delete_meme.check_response_text_is('You are not the meme owner')


@allure.feature('meme delete')
@allure.story('meme delete capability')
@allure.description('check that system isnt to able delete non-existed meme')
@allure.tag("High")
@allure.severity('Negative')
def test_delete_meme_by_non_existed_id(create_meme, get_token, delete_meme):
    meme_id = random.randrange(9000, 99999)
    delete_meme.delete_meme_by_id(meme_id, get_token)
    assert delete_meme.check_status_code_is_(404)
    delete_meme.check_response_text_is('Not Found')
