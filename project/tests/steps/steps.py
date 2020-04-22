import json
import os
import random
from http import HTTPStatus

from framework.browser_navigate.browser_navigate import BrowserNavigate
from framework.cookie.cookie import Cookie
from framework.j_s_executor.j_s_executor import JSExecutor
from framework.screenshot.screenshot import ScreenShot
from project.pages.page_project import PageProject
from project.pages.projects_page import ProjectsPage
from project.pages.test_page import TestPage
from project.utils.authorization.authorization import Authorization
from project.utils.cloudinary.cloudinary import Cloudinary
from project.utils.config_project.config_project import ConfigProject
from project.utils.constans.keys_bd import KeysBD
from project.utils.constans.methods_j_s import MethodsJS
from project.utils.database.attachment import Attachment
from project.utils.database.log import Log
from project.utils.database.project import Project
from project.utils.database.session import Session
from project.utils.database.status_db import StatusDB
from project.utils.database.test_db import TestDB
from project.utils.modal_window.modal_window import ModalWindow
from project.utils.reporting_portal_api_utils.reporting_portal_api_utils import ReportingPortalApiUtils
from project.utils.testrail_api.testrail_api import TestRailAPI
from project.utils.window_handles.window_handles import WindowHandles


class Steps:
    config_project = ConfigProject.get_instance()
    projects_page = ProjectsPage()
    modal_window = ModalWindow()
    authorization = Authorization()
    rep_portal = ReportingPortalApiUtils()
    response_api = None
    cookie = Cookie()
    browser_navigate = BrowserNavigate()
    window_handles = WindowHandles()
    j_s_executor = JSExecutor()
    project = Project()
    test_db = TestDB()
    session = Session()
    status_db = StatusDB()
    log = Log()
    attachment = Attachment()
    page_project = PageProject()
    screenshot = ScreenShot()
    test_page = TestPage()
    cloudinary = Cloudinary(config_project.cloud_name_cloudinary(),
                            config_project.api_key_cloudinary(), config_project.api_secret_cloudinary())
    testrail_api = TestRailAPI()

    def open_website(self):
        self.projects_page.open()

    def log_in(self, login, password):
        self.authorization.log_in(login, password)

    def get_token(self, variant):
        self.response_api = self.rep_portal.get_token(variant)
        return self.response_api.get_response()

    def token_is_generated(self):
        self.is_status_code_ok()
        assert self.response_api.get_response(), "Token is empty"

    def is_status_code_ok(self):
        assert self.response_api.get_status_code() == HTTPStatus.OK.value, \
            "Status code: not equal: {}".format(HTTPStatus.OK.value)

    def add_cookie(self, cookies):
        self.cookie.add_cookies(cookies)

    def refresh_page(self):
        self.browser_navigate.refresh()

    def projects_page_is_opened(self):
        assert self.projects_page.page_is_opened(), "Project page did not open"

    def is_in_footer_indicated_correct_number(self, variant):
        version = int(''.join(filter(str.isdigit, self.get_number_version_from_page())))
        assert variant == version, "Variant number is not correct"

    def get_number_version_from_page(self):
        return self.projects_page.get_number_version()

    def go_to_project_page(self, project_name):
        self.projects_page.list_projects.select_item(project_name)

    def go_to_test_page(self, test_name):
        self.page_project.test_list.select_test(test_name)

    def is_project_appeared_on_the_list_projects(self, project_name):
        assert self.projects_page.list_projects.is_project_appeared_on_the_list(project_name), \
            "Project did not appear on the list"

    def is_test_appeared_on_the_list_tests(self, test_name):
        assert self.page_project.test_list.is_test_appeared_on_the_list(test_name), "Test did not appear on the list"

    def return_to_previous_page(self):
        self.browser_navigate.back()

    def get_list_tests_from_first_page_ui(self):
        return self.page_project.test_list.get_list_test()

    def list_test_start_time(self, list_tests_from_page_ui):
        list_start_time = []
        for index in range(3, len(list_tests_from_page_ui), 7):
            list_start_time.append(list_tests_from_page_ui[index].text)
        return list_start_time

    def list_test_name(self, list_tests_from_page_ui):
        list_name = []
        for index in range(3, len(list_tests_from_page_ui), 7):
            list_name.append(list_tests_from_page_ui[index].text)
        return list_name

    def is_tests_on_the_first_page_are_sorted_by_date(self, list_tests_from_page_ui):
        is_sorted = True
        list_start_time = self.list_test_start_time(list_tests_from_page_ui)
        time_test = list_start_time[0]
        for time in list_start_time:
            if time_test < time:
                is_sorted = False
            time_test = time
        assert is_sorted, "Tests on the first page not sorted by date"

    def is_tests_on_first_page_correspond_to_those_that_returned_request_for_api(self, list_tests_from_page_ui,
                                                                                 list_of_tests_on_request_api):
        is_math = True
        str_list_of_tests_on_request_api = str(list_of_tests_on_request_api.json())
        list_name = self.list_test_name(list_tests_from_page_ui)
        for test_name in list_name:
            if test_name not in str_list_of_tests_on_request_api:
                is_math = False
        assert is_math, "Tests on the first page do not match those returned by the api request"

    def get_list_of_tests_on_request_api(self, project_id):
        self.response_api = self.rep_portal.get_list_project_tests_in_json_format(project_id)
        self.is_status_code_ok()
        return self.response_api.get_response()

    def is_list_of_tests_on_request_api_in_format_json(self, list_of_tests_on_request_api):
        try:
            list_of_tests_on_request_api.json()
            assert True
        except json.decoder.JSONDecodeError:
            assert False, "List of tests on request api not in json format"

    def click_button_add(self):
        self.projects_page.click_button_add()

    def enter_project_name(self, text):
        self.projects_page.iframe.enter_text(text)

    def is_message_about_successful_save_appeared(self):
        assert self.projects_page.iframe.is_message_about_successful_save_appeared(), \
            "Message_about not_successful_save_appeared"

    def switch_to_iframe(self):
        self.window_handles.switch_to_iframe()

    def switch_to_window(self):
        self.window_handles.switch_to_main_page()

    def click_button_submit(self):
        self.projects_page.iframe.click_button_submit()

    def close_add_project_window(self):
        self.j_s_executor.execute_script(MethodsJS.CLOSE_WIN_ADD_PROJECT.value)

    def get_project_id_by_name_project_from_db(self, cursor, project_name):
        cursor_method = cursor.execute_query_select(self.project.select_id_by_name(project_name))
        project_id = cursor_method.fetchone()
        cursor_method.close()
        return project_id[KeysBD.ID.value]

    def add_test_via_db(self, cursor, project_id, name, method_name, status_id, session_id, env):
        cursor.execute_query_insert(self.test_db.insert(project_id, name, method_name, status_id, session_id, env))

    def get_test_id_by_test_name_from_db(self, cursor, test_name):
        cursor_method = cursor.execute_query_select(self.test_db.select_id_by_name(test_name))
        test_id = cursor_method.fetchone()
        cursor_method.close()
        return test_id[KeysBD.ID.value]

    def get_list_all_session_id_from_db(self, cursor):
        list_session_id = cursor.execute_query_select(self.session.select_id()).fetchall()
        return list_session_id

    def get_random_session_id(self, list_session_id):
        session_id = random.choice(list_session_id)
        return session_id[KeysBD.ID.value]

    def get_status_id_by_status_name_from_db(self, cursor, status_name):
        status_id = cursor.execute_query_select(self.status_db.select_id_by_name(status_name)).fetchone()
        return status_id[KeysBD.ID.value]

    def get_list_all_status_id_from_db(self, cursor):
        list_status_id = cursor.execute_query_select(self.status_db.select_id()).fetchall()
        return list_status_id

    def get_random_status_id(self, list_status_id):
        status_id = random.choice(list_status_id)
        return status_id[KeysBD.ID.value]

    def get_name_status_by_id(self, cursor, status_id):
        name = cursor.execute_query_select(self.status_db.select_name_by_id(status_id)).fetchone()
        return name[KeysBD.NAME.value]

    def add_log_in_db(self, cursor, content, is_exception, test_id):
        cursor.execute_query_insert(self.log.insert(content, is_exception, test_id))

    def add_attachment_in_db(self, cursor, content_type, test_id, image):
        cursor.execute_query_insert_image(self.attachment.insert(content_type, test_id), image)

    def get_content_from_attachment_db(self, cursor, test_id):
        content = cursor.execute_query_select(self.attachment.select_content(test_id)).fetchone()
        return content[KeysBD.CONTENT.value]

    def take_screenshot(self):
        self.screenshot.take_screenshot(self.config_project.name_screen())

    def get_screenshot_as_png(self):
        return self.screenshot.get_screenshot_as_png()

    def upload_screenshot_to_the_cloudinary_service(self):
        self.cloudinary.upload_image(self.config_project.name_screen())

    def get_url_uploaded_image_from_cloudinary_service(self):
        return self.cloudinary.get_url_uploaded_image()

    def download_image(self, image_name):
        download = open(image_name, "rb").read()
        return download

    def get_project_name_from_test_page(self):
        return self.test_page.get_project_name()

    def get_test_name_from_test_page(self):
        return self.test_page.get_test_name()

    def get_test_method_name_from_test_page(self):
        return self.test_page.get_test_method_name()

    def get_status_from_test_page(self):
        return self.test_page.get_status()

    def get_env_from_test_page(self):
        return self.test_page.get_env()

    def get_log_from_test_page(self):
        return self.test_page.get_log()

    def get_attachment_type_from_test_page(self):
        return self.test_page.get_attachment_type()

    def get_all_field_test_page_write_to_test_model(self, test_model):
        test_model.set_project_name(self.get_project_name_from_test_page())
        test_model.set_test_name(self.get_test_name_from_test_page())
        test_model.set_test_method_name(self.get_test_method_name_from_test_page())
        test_model.set_status(self.get_status_from_test_page())
        test_model.set_environment(self.get_env_from_test_page())
        test_model.set_log(self.get_log_from_test_page())
        test_model.set_attachment_type(self.get_attachment_type_from_test_page())

    def image_is_download_to_the_page(self):
        assert self.test_page.get_attachment_type(), "No image per page"

    def check_information_is_correct_from_test_page(self, test_model_1, test_model_2):
        assert test_model_1 == test_model_2, "Information is not correct from test page"

    def is_screenshot_corresponds_to_the_sent(self, image1, image2):
        self.image_is_download_to_the_page()
        assert image1 == image2, "Screenshot does not match sent"

    def clear_dir(self, image):
        os.remove(image)

    def put_results_of_the_test_case(self, run_id, case_id, result_fields):
        return self.testrail_api.add_result_for_case(run_id, case_id, result_fields)

    def is_page_project_open(self, project_name):
        assert self.page_project.page_project_is_open(project_name), "Project page is not open"

    def is_add_project_form_open(self):
        assert self.projects_page.iframe.is_iframe_open(), "Project form not open"

    def is_add_project_form_closed(self):
        assert not self.projects_page.iframe.is_iframe_closed(), "Project form not closed"
