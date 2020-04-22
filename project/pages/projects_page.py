from framework.base_element.button.button import Button
from framework.base_element.label.label import Label
from framework.browser.browser import Browser
from project.forms.iframe import IFrame
from project.forms.list_projects import ListProjects
from project.utils.config_project.config_project import ConfigProject


class ProjectsPage:
    list_projects = ListProjects()
    iframe = IFrame()
    _AVAILABLE_PROJECT = "//div[@class='panel-heading']"
    _VERSION = "//footer[@class='footer']//span"
    _ADD_BUTTON = "//button[contains(@class, 'btn')]"
    _FIELD = "//body[@class='modal-open']//div[@class='modal-content']//input[@type='text']"

    def __init__(self):
        self._browser = Browser.get_instance()

    def open(self):
        self._browser.get(ConfigProject.get_instance().url_web())

    def page_is_opened(self):
        return Label(self._AVAILABLE_PROJECT).is_element_presence()

    def get_number_version(self):
        return Label(self._VERSION).get_text()

    def click_button_add(self):
        Button(self._ADD_BUTTON).click()
