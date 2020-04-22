from selenium.webdriver.common.keys import Keys

from framework.base_element.base_element import BaseElement


class Field(BaseElement):
    def __init__(self, locator):
        super().__init__(locator)

    def clear(self):
        self._wait_for_element_by_xpath()
        self._find_element_by_xpath().clear()

    def enter_text(self, text):
        self._wait_for_element_by_xpath()
        self._find_element_by_xpath().send_keys(text)

    def select_text(self):
        self._wait_for_element_by_xpath()
        self._find_element_by_xpath().send_keys(Keys.CONTROL + "a")
