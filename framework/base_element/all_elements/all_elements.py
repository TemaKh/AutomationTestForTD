from framework.base_element.base_element import BaseElement


class AllElements(BaseElement):
    def __init__(self, locator):
        super().__init__(locator)

    def get_all_elements(self):
        self._wait_for_element_by_xpath()
        return self._find_elements_by_xpath()
