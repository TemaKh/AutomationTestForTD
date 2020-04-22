from selenium import webdriver
from selenium.webdriver import DesiredCapabilities
from webdriver_manager.chrome import ChromeDriverManager
from webdriver_manager.firefox import GeckoDriverManager

from framework.localization_factory.download_options_factory.download_options_factory import DownloadOptionsFactory
from framework.utils.config.config import Config
from framework.utils.constants.browser_name import BrowserName
from framework.utils.constants.jenkins_const import JenkinsConst


class BrowserFactory:
    _browser = None
    _chrome = BrowserName.CHROME.value
    _firefox = BrowserName.FIREFOX.value
    _browser_name = Config.get_instance().get_browser().lower()
    _localization_download = DownloadOptionsFactory().get_download_options()
    _command_executor = Config.get_instance().get_command_executor()
    _how_to_run = Config.get_instance().get_how_to_run()
    _local = JenkinsConst.LOCAL.value
    _remote = JenkinsConst.REMOTE.value

    def get_browser(self):
        if self._chrome == self._browser_name:
            if self._how_to_run == self._remote:
                self._browser = webdriver.Remote(command_executor=self._command_executor,
                                                 desired_capabilities=DesiredCapabilities.CHROME,
                                                 options=self._localization_download)
            elif self._how_to_run == self._local:
                self._browser = webdriver.Chrome(options=self._localization_download,
                                                 executable_path=ChromeDriverManager().install())
        elif self._firefox == self._browser_name:
            if self._how_to_run == self._remote:
                self._browser = webdriver.Remote(command_executor=self._command_executor,
                                                 desired_capabilities=DesiredCapabilities.FIREFOX,
                                                 browser_profile=self._localization_download)
            elif self._how_to_run == self._local:
                self._browser = webdriver.Firefox(firefox_profile=self._localization_download,
                                                  executable_path=GeckoDriverManager().install())
        return self._browser
