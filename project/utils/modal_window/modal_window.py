from selenium.webdriver.common.actions.interaction import KEY

from framework.browser.browser import Browser


class ModalWindow:
    def __init__(self):
        self._browser = Browser.get_instance()

    def click_button_accept(self):
        alert = self._browser.switch_to.alert
        alert.accept()

    def enter_text_in_the_input_field(self, text):
        alert = self._browser.switch_to.alert
        alert.send_keys(text)

    def get_text(self):
        alert = self._browser.switch_to.alert
        return alert.text

    def switching_between_input_fields(self):
        alert = self._browser.switch_to.alert
        alert.send_keys(KEY.TAB)
