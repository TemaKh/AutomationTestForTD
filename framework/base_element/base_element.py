from selenium.common.exceptions import TimeoutException
from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from framework.browser.browser import Browser
from framework.utils.config.config import Config


class BaseElement:

    def __init__(self, locator):
        self.__locator = locator
        self.__browser = Browser.get_instance()
        self.__wait = Config.get_instance().get_wait()
        self.__actions = ActionChains(self.__browser)

    def click(self, args_text_element=None):
        if args_text_element is not None:
            self.__wait_for_element_by_text(args_text_element)
            self.__find_element_by_text(args_text_element).click()
        else:
            self._wait_for_element_by_xpath()
            self._find_element_by_xpath().click()

    def get_text(self):
        self._wait_for_element_by_xpath()
        return self._find_element_by_xpath().text

    def move_to_element(self, text_element):
        self.__wait_for_element_by_text(text_element)
        element = self.__find_element_by_text(text_element)
        self.__actions.move_to_element(element)
        self.__actions.perform()

    def get_actions(self):
        return self.__actions

    def get_attribute(self, attribute):
        self._wait_for_element_by_xpath()
        return self._find_element_by_xpath().get_attribute(attribute)

    def is_element_presence(self):
        elements = self._find_elements_by_xpath()
        if not elements:
            return False
        return True

    def wait_element_presence(self):
        try:
            self._wait_for_element_by_xpath()
        except TimeoutException:
            return False
        return True

    def wait_element_visibility(self):
        try:
            WebDriverWait(self.__browser, self.__wait).until(
                EC.visibility_of_element_located((By.XPATH, self.__locator)))
        except TimeoutException:
            return False
        return True

    def _find_element_by_xpath(self):
        return self.__browser.find_element(By.XPATH, self.__locator)

    def __find_element_by_text(self, *args_text):
        return self.__browser.find_element(By.XPATH, self.__locator.format(*args_text))

    def _find_elements_by_xpath(self):
        return self.__browser.find_elements(By.XPATH, self.__locator)

    def _wait_for_element_by_xpath(self):
        WebDriverWait(self.__browser, self.__wait).until(EC.presence_of_element_located((By.XPATH, self.__locator)))

    def __wait_for_element_by_text(self, *args_text):
        locator = self.__locator.format(*args_text)
        WebDriverWait(self.__browser, self.__wait).until(EC.presence_of_element_located((By.XPATH, locator)))
