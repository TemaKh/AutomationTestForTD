from framework.base_element.label.label import Label


class TestPage:
    _PROJECT_NAME = "//h4[text()='Project name']/following-sibling::p"
    _TEST_NAME = "//h4[text()='Test name']/following-sibling::p"
    _TEST_METHOD_NAME = "//h4[text()='Test method name']/following-sibling::p"
    _STATUS = "//h4[text()='Status']/following-sibling::p/span"
    _ENV = "//h4[text()='Environment']/following-sibling::p"
    _LOG = "//div[@class ='panel-heading'][text()='Logs']/following-sibling::table//td"
    _ATTACHMENT_TYPE = "//div[@class ='panel-heading'][text()='Attachments']" \
                       "/following-sibling::table//td/following-sibling::td"
    _ATTACHMENT = "//div[@class ='panel-heading'][text()='Attachments']/following-sibling::table//td/a"

    def get_project_name(self):
        return Label(self._PROJECT_NAME).get_text()

    def get_test_name(self):
        return Label(self._TEST_NAME).get_text()

    def get_test_method_name(self):
        return Label(self._TEST_METHOD_NAME).get_text()

    def get_status(self):
        return Label(self._STATUS).get_text().upper()

    def get_env(self):
        return Label(self._ENV).get_text()

    def get_log(self):
        return Label(self._LOG).get_text()

    def get_attachment_type(self):
        return Label(self._ATTACHMENT_TYPE).get_text()

    def get_attachment(self):
        return Label(self._ATTACHMENT).is_element_presence()
