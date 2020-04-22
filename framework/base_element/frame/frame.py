from framework.base_element.base_element import BaseElement


class Frame(BaseElement):
    def __init__(self, locator):
        super().__init__(locator)

    def find_frame(self):
        self._wait_for_element_by_xpath()
        return self._find_element_by_xpath()
