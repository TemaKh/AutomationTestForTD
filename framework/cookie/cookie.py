from framework.browser.browser import Browser
from framework.utils.constants.cookie_const import CookieConst


class Cookie:
    def __init__(self):
        self._browser = Browser.get_instance()

    def add_cookies(self, cookies):
        for key, value in cookies.items():
            self._browser.add_cookie({CookieConst.NAME.value: key, CookieConst.VALUE.value: value})
