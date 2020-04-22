from framework.base_element.button.button import Button
from framework.base_element.field.field import Field
from framework.base_element.label.label import Label


class IFrame:
    _FIELD_IFRAME = "//input[@id='projectName']"
    _BUTTON_SUBMIT = "//button[contains(@type, 'submit')]"
    _SUCCESS_MESSAGE = "//div[contains(@class, 'success')]"
    _ADD_PROJECT_FORM = "//iframe[@id='addProjectFrame']"
    _FORM_GROUP = "//div[contains(@class, 'form-group')]"

    def clear_field(self):
        Field(self._FIELD_IFRAME).clear()

    def enter_text(self, text):
        field = Field(self._FIELD_IFRAME)
        field.wait_element_visibility()
        field.enter_text(text)

    def select_text(self):
        Field(self._FIELD_IFRAME).select_text()

    def click_button_submit(self):
        button = Button(self._BUTTON_SUBMIT)
        button.wait_element_visibility()
        button.click()

    def is_message_about_successful_save_appeared(self):
        label = Label(self._SUCCESS_MESSAGE)
        label.wait_element_visibility()
        return label.is_element_presence()

    def is_iframe_open(self):
        return Label(self._ADD_PROJECT_FORM).is_element_presence()

    def is_iframe_closed(self):
        return Label(self._FORM_GROUP).is_element_presence()
