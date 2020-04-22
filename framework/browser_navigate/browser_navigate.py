from framework.browser.browser import Browser


class BrowserNavigate:
    def __init__(self):
        self._browser = Browser.get_instance()

    def refresh(self):
        self._browser.refresh()

    def back(self):
        self._browser.back()
