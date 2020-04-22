from framework.browser.browser import Browser
from project.utils.config_project.config_project import ConfigProject


class Authorization:

    def __init__(self):
        self._browser = Browser.get_instance()

    def log_in(self, login, password):
        self._browser.get(ConfigProject.get_instance().url_auth().format(login, password))
