from selenium import webdriver

from framework.utils.config.config import Config
from framework.utils.constants.browser_name import BrowserName
from framework.utils.constants.localization_name import LocalizationName


class LocalizationFactory:
    _chrome = BrowserName.CHROME.value
    _firefox = BrowserName.FIREFOX.value
    _browser_name = Config.get_instance().get_browser().lower()
    _ru = LocalizationName.RU.value
    _en = LocalizationName.EN.value
    _local_name = Config.get_instance().get_localization().lower()
    _chrome_options = webdriver.ChromeOptions()
    _firefox_profile = webdriver.FirefoxProfile()

    def set_localization(self):
        if self._browser_name == self._chrome:
            if self._local_name == self._en:
                self._chrome_options.add_argument("--lang=en")
                return self._chrome_options
            elif self._local_name == self._ru:
                self._chrome_options.add_argument("--lang=ru")
                return self._chrome_options
        elif self._browser_name == self._firefox:
            if self._local_name == self._en:
                self._firefox_profile.set_preference('intl.accept_languages', 'en')
                return self._firefox_profile
            elif self._local_name == self._ru:
                self._firefox_profile.set_preference('intl.accept_languages', 'ru')
                return self._firefox_profile
