import allure
import pytest

from framework.utils.text_generator.text_generator import TextGenerator
from project.models.test_model import TestModel
from project.tests.steps.steps import Steps
from project.utils.config_project.config_project import ConfigProject
from project.utils.constans.const_test_case import ConstTestCase
from project.utils.constans.is_exception import IsException
from project.utils.constans.variant import Variant


@pytest.mark.usefixtures("adding_result_in_test_rail")
@pytest.mark.usefixtures("start_browser")
class Test:
    step = Steps()
    conf_project = ConfigProject.get_instance()
    text_gen = TextGenerator()

    @allure.title("Variant - 1")
    @pytest.mark.parametrize("variant, cookie, existing_project_name, new_project_name, "
                             "test_name, test_method, env, content_log, is_exception",
                             [
                                 (Variant.ONE.value, {ConstTestCase.TOKEN.value: ""}, "Nexage", text_gen.generate(),
                                  text_gen.generate(), text_gen.generate(), text_gen.generate(), text_gen.generate(),
                                  IsException.NO.value)
                             ])
    def test_variant_1(self, cursor, variant, cookie, existing_project_name, new_project_name,
                       test_name, test_method, env, content_log, is_exception):
        with allure.step("Step 1. By request to api, get a token according to the option number"):
            token = self.step.get_token(variant)
            self.step.token_is_generated()

        with allure.step("Step 2. Go to the site. Pass the necessary authorization. Using a cookie, "
                         "pass the token generated in step 1 (token parameter). Refresh the page."):
            self.step.open_website()
            self.step.log_in(self.conf_project.web_login(), self.conf_project.web_password())
            self.step.projects_page_is_opened()
            cookie.update({ConstTestCase.TOKEN.value: token})
            self.step.add_cookie(cookie)
            self.step.refresh_page()
            self.step.is_in_footer_indicated_correct_number(variant)

        with allure.step("Step 3. Go to the Nexage project page. "
                         "A request to api to get a list of tests in JSON format."):
            self.step.go_to_project_page(existing_project_name)
            self.step.is_page_project_open(existing_project_name)
            list_tests_from_first_page_ui = self.step.get_list_tests_from_first_page_ui()
            id_existing_project = self.step.get_project_id_by_name_project_from_db(cursor, existing_project_name)
            list_of_tests_on_request_api = self.step.get_list_of_tests_on_request_api(id_existing_project)
            self.step.is_list_of_tests_on_request_api_in_format_json(list_of_tests_on_request_api)
            self.step.is_tests_on_the_first_page_are_sorted_by_date(list_tests_from_first_page_ui)
            self.step.is_tests_on_first_page_correspond_to_those_that_returned_request_for_api(
                list_tests_from_first_page_ui, list_of_tests_on_request_api)

        with allure.step("Step 4. Return to the previous page in the browser (project page). "
                         "Click on + Add. Enter the name of the project, and save. "
                         "To close the add project window, call the closePopUp () js method. Refresh the page"):
            self.step.return_to_previous_page()
            self.step.click_button_add()
            self.step.is_add_project_form_open()
            self.step.switch_to_iframe()
            self.step.enter_project_name(new_project_name)
            self.step.click_button_submit()
            self.step.is_message_about_successful_save_appeared()
            self.step.switch_to_window()
            self.step.close_add_project_window()
            self.step.is_add_project_form_closed()
            self.step.refresh_page()
            self.step.is_project_appeared_on_the_list_projects(new_project_name)

        with allure.step("Step 5. Go to the page of the created project. Add a test through the database "
                         "(along with the log and screenshot of the current page)."):
            self.step.go_to_project_page(new_project_name)
            content_image = self.step.get_screenshot_as_png()
            id_new_project = self.step.get_project_id_by_name_project_from_db(cursor,
                                                                              new_project_name)
            list_status_id = self.step.get_list_all_status_id_from_db(cursor)
            status_id = self.step.get_random_status_id(list_status_id)
            status_name = self.step.get_name_status_by_id(cursor, status_id)
            list_session_id = self.step.get_list_all_session_id_from_db(cursor)
            session_id = self.step.get_random_session_id(list_session_id)
            self.step.add_test_via_db(cursor, id_new_project, test_name, test_method, status_id, session_id, env)
            test_id = self.step.get_test_id_by_test_name_from_db(cursor, test_name)
            self.step.add_log_in_db(cursor, content_log, is_exception, test_id)
            self.step.add_attachment_in_db(cursor, self.conf_project.name_screen(), test_id, content_image)
            self.step.is_test_appeared_on_the_list_tests(test_name)
            test_data = TestModel(new_project_name, test_name, test_method, status_name, env,
                                  self.conf_project.name_screen(), content_log)

        with allure.step("Step 6. Go to the page of the created test. Check the information is correct."):
            self.step.go_to_test_page(test_name)
            test_data_from_page = TestModel()
            self.step.get_all_field_test_page_write_to_test_model(test_data_from_page)
            self.step.check_information_is_correct_from_test_page(test_data, test_data_from_page)
            download_image = self.step.get_content_from_attachment_db(cursor, test_id)
            self.step.is_screenshot_corresponds_to_the_sent(content_image, download_image)
            self.step.take_screenshot()
