import allure
import requests

base_url = 'http://167.172.172.115:52355/'


class BaseApi:
    response: requests.Response
    response_json: dict

    @allure.step('Check status code')
    def check_status_code_is_(self, code):
        return self.response.status_code == code

    @allure.step('Check user auth name')
    def check_response_title_is_(self, name):
        return self.response.json()['user'] == name
