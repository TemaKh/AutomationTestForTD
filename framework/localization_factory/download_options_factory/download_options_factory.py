import os

from framework.localization_factory.localization_factory import LocalizationFactory
from framework.utils.config.config import Config
from framework.utils.constants.browser_name import BrowserName


class DownloadOptionsFactory:
    _chrome = BrowserName.CHROME.value
    _firefox = BrowserName.FIREFOX.value
    _browser_name = Config.get_instance().get_browser().lower()
    _download_path = os.path.abspath(Config.get_instance().get_download_path())
    _localization = LocalizationFactory().set_localization()

    def get_download_options(self):
        if self._browser_name == self._chrome:
            preferences = {"download.default_directory": self._download_path,
                           "directory_upgrade": True,
                           "safebrowsing.enabled": True}
            self._localization.add_experimental_option("prefs", preferences)
            return self._localization
        elif self._browser_name == self._firefox:
            self._localization.set_preference("browser.download.folderList", 2)
            self._localization.set_preference("browser.download.manager.showWhenStarting", False)
            self._localization.set_preference("browser.download.dir", self._download_path)
            self._localization.set_preference("browser.helperApps.neverAsk.saveToDisk",
                                              "application/octet-stream,application/vnd.ms-excel")
            return self._localization
