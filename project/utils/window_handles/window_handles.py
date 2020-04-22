from framework.base_element.frame.frame import Frame
from framework.browser.browser import Browser


class WindowHandles:
    _IFRAME = "//iframe"

    def __init__(self):
        self._browser = Browser.get_instance()

    def switch_to_main_page(self):
        self._browser.switch_to.parent_frame()

    def switch_to_iframe(self):
        self._browser.switch_to.frame(Frame(self._IFRAME).find_frame())
