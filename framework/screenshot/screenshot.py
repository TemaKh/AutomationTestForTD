from framework.browser.browser import Browser


class ScreenShot:
    def __init__(self):
        self._browser = Browser.get_instance()

    def take_screenshot(self, name_screen):
        path = name_screen
        self._browser.get_screenshot_as_file(path)

    def get_screenshot_as_png(self):
        return self._browser.get_screenshot_as_png()
