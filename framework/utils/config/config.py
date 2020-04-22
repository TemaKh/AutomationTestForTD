import json
import os

from framework.utils.constants.jenkins_const import JenkinsConst


class Config:
    _instance = None
    _FILE_PATH = os.path.abspath("framework/resources/config.json")

    def __init__(self):
        with open(self._FILE_PATH) as file:
            self._conf_file = json.load(file)

    @staticmethod
    def get_instance():
        if Config._instance is None:
            Config._instance = Config()
        return Config._instance

    def get_browser(self):
        if JenkinsConst.BROWSER.value in os.environ:
            return os.environ[JenkinsConst.BROWSER.value]
        else:
            return self._conf_file.get("browser")

    def get_localization(self):
        return self._conf_file.get("localization")

    def get_wait(self):
        return self._conf_file.get("wait")

    def get_download_path(self):
        return self._conf_file.get("download_path")

    def get_wait_download(self):
        return self._conf_file.get("wait_download")

    def get_command_executor(self):
        return self._conf_file.get("command_executor")

    def get_how_to_run(self):
        if JenkinsConst.HOW_TO_RUN.value in os.environ:
            return os.environ[JenkinsConst.HOW_TO_RUN.value]
        else:
            return self._conf_file.get("how_to_run")
