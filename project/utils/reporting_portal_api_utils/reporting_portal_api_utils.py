import requests

from project.utils.config_project.config_project import ConfigProject
from project.utils.response_api.response_api import ResponseApi


class ReportingPortalApiUtils:
    _URL = ConfigProject.get_instance().url_api()
    _TOKEN_GENERATION = "/token/get"
    _GET_JSON = "/test/get/json"

    def get_token(self, variant):
        response = requests.post(url=self._URL + self._TOKEN_GENERATION, params={"variant": variant})
        return ResponseApi(response.status_code, response.text)

    def get_list_project_tests_in_json_format(self, project_id):
        response = requests.post(url=self._URL + self._GET_JSON, params={"projectId": project_id})
        return ResponseApi(response.status_code, response)
