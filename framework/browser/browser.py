from framework.browser_factory.browser_factory import BrowserFactory


class Browser:
    _instance = None

    @staticmethod
    def get_instance():
        if Browser._instance is None:
            Browser._instance = BrowserFactory().get_browser()
        return Browser._instance
