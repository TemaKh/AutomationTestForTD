from framework.base_element.all_elements.all_elements import AllElements
from framework.base_element.label.label import Label


class TestList:
    _TEST_NAME = "//table[@class = 'table']/tbody/tr/td/a[text() = '{}']"
    _ALL_ELEMENTS = "//table[@class = 'table']//tr/td"

    def select_test(self, test_name):
        locator = self._TEST_NAME.format(test_name)
        Label(locator).click()

    def is_test_appeared_on_the_list(self, test_name):
        locator = self._TEST_NAME.format(test_name)
        test = Label(locator)
        test.wait_element_visibility()
        return test.is_element_presence()

    def get_list_test(self):
        return AllElements(self._ALL_ELEMENTS).get_all_elements()
