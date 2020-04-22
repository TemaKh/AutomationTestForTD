import requests
from requests.auth import HTTPBasicAuth

from project.utils.config_project.config_project import ConfigProject


class TestRailAPI:
    config_project = ConfigProject.get_instance()
    _login = config_project.test_rail_login()
    _password = config_project.test_rail_password()
    _HEADERS = {'Content-Type': 'application/json'}
    _SLASH = "/"
    _URL = "https://tr.a1qa.com/"
    _PATH_API = "index.php?/api/v2/"
    _ADD_RESULT_FOR_CASE = "add_result_for_case/"

    def add_result_for_case(self, run_id, case_id, result_fields):
        url = self._URL + self._PATH_API + self._ADD_RESULT_FOR_CASE + str(run_id) + self._SLASH + str(case_id)
        response = requests.post(url=url, headers=self._HEADERS, auth=HTTPBasicAuth(self._login, self._password),
                                 json=result_fields)
        return response.status_code
