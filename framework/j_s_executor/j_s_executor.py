from framework.browser.browser import Browser


class JSExecutor:
    def __init__(self):
        self._browser = Browser.get_instance()

    def execute_script(self, script):
        self._browser.execute_script(script)
