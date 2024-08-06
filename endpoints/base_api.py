import allure
import requests

base_url = 'http://167.172.172.115:52355/'


class BaseApi:
    response: requests.Response
    response_json: dict
    token: str

    @allure.step('Check status code')
    def check_status_code_is_(self, code):
        print(self.response.status_code)
        return self.response.status_code == code

    @allure.step('Check user auth name')
    def check_response_title_is_(self, name):
        return self.response.json()['user'] == name

    @allure.step('Check user auth name')
    def check_negative_response_title_is_(self, title):
        return self.response.json()['title'] == title

    def check_response_text_is(self, response_text):
        return response_text in self.response.text

    def check_json_decoder_error(self):
        if self.response.status_code == 200:
            try:
                self.response_json = self.response.json()
            except requests.exceptions.JSONDecodeError:
                self.response_json = None
        else:
            self.response_json = None
