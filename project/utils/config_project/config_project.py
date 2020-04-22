import json
import os

from project.utils.constans.jenkins_auth import JenkinsAuth


class ConfigProject:

    _instance = None
    _FILE_PATH = os.path.abspath("project/resources/config_project.json")

    def __init__(self):
        with open(self._FILE_PATH) as file:
            self._conf_file = json.load(file)

    @staticmethod
    def get_instance():
        if ConfigProject._instance is None:
            ConfigProject._instance = ConfigProject()
        return ConfigProject._instance

    def url_web(self):
        return self._conf_file.get("url_web")

    def url_api(self):
        return self._conf_file.get("url_api")

    def url_auth(self):
        return self._conf_file.get("url_auth")

    def web_login(self):
        if JenkinsAuth.WEB_LOGIN.value in os.environ:
            return os.environ[JenkinsAuth.WEB_LOGIN.value]
        else:
            return self._conf_file.get("web_auth").get("login")

    def web_password(self):
        if JenkinsAuth.WEB_PASSWORD.value in os.environ:
            return os.environ[JenkinsAuth.WEB_PASSWORD.value]
        else:
            return self._conf_file.get("web_auth").get("password")

    def db_login(self):
        if JenkinsAuth.DB_LOGIN.value in os.environ:
            return os.environ[JenkinsAuth.DB_LOGIN.value]
        else:
            return self._conf_file.get("db_auth").get("login")

    def db_password(self):
        if JenkinsAuth.DB_PASSWORD.value in os.environ:
            return os.environ[JenkinsAuth.DB_PASSWORD.value]
        else:
            return self._conf_file.get("db_auth").get("password")

    def host(self):
        return self._conf_file.get("db_connect").get("host")

    def port(self):
        return self._conf_file.get("db_connect").get("port")

    def db_name(self):
        return self._conf_file.get("db_connect").get("db_name")

    def name_screen(self):
        return self._conf_file.get("name_screen")

    def cloud_name_cloudinary(self):
        return self._conf_file.get("cloudinary").get("cloud_name")

    def api_key_cloudinary(self):
        return self._conf_file.get("cloudinary").get("api_key")

    def api_secret_cloudinary(self):
        return self._conf_file.get("cloudinary").get("api_secret")

    def test_rail_login(self):
        if JenkinsAuth.TESTRAIL_LOGIN.value in os.environ:
            return os.environ[JenkinsAuth.TESTRAIL_LOGIN.value]
        else:
            return self._conf_file.get("testrail_auth").get("login")

    def test_rail_password(self):
        if JenkinsAuth.TESTRAIL_PASSWORD.value in os.environ:
            return os.environ[JenkinsAuth.TESTRAIL_PASSWORD.value]
        else:
            return self._conf_file.get("testrail_auth").get("password")
