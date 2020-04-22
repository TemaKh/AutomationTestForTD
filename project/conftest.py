import allure
import pytest

from framework.browser.browser import Browser
from framework.cursor.cursor import Cursor
from framework.database_connect.database_connect import DatabaseConnect
from project.tests.steps.steps import Steps
from project.utils.config_project.config_project import ConfigProject
from project.utils.constans.keys_test_rail import KeysTestRail
from project.utils.constans.status_test import StatusTest
from project.utils.constans.test_rail import TestRail


@pytest.fixture(scope="function")
def start_browser():
    browser = Browser.get_instance()
    browser.maximize_window()
    yield browser
    browser.quit()


@pytest.fixture(scope="function")
def database_connect():
    conf_project = ConfigProject.get_instance()
    database = DatabaseConnect(conf_project.host(), conf_project.port(),
                               conf_project.db_login(), conf_project.db_password(), conf_project.db_name())
    yield database.get_connect()
    database.close_connect()


@pytest.fixture(scope="function")
def cursor(database_connect):
    cursor = Cursor(database_connect)
    return cursor


@pytest.fixture(scope="function")
def adding_result_in_test_rail():
    yield
    step = Steps()
    test_status = StatusTest.PASSED.value
    url_image = None
    try:
        with allure.step("Uploading a picture for Testail to a remote resource"):
            step.upload_screenshot_to_the_cloudinary_service()
            url_image = step.get_url_uploaded_image_from_cloudinary_service()
    except FileNotFoundError:
        with allure.step("Change test status to 'Failed'. Takes screenshot "
                         "and uploading a picture for Testail to a remote resource"):
            step.take_screenshot()
            test_status = StatusTest.FAILED.value
            step.upload_screenshot_to_the_cloudinary_service()
            url_image = step.get_url_uploaded_image_from_cloudinary_service()
    finally:
        with allure.step("Sending test result to Testrail and clear work dir"):
            result_fields = {KeysTestRail.STATUS_ID.value: test_status, KeysTestRail.COMMENT.value: url_image}
            step.put_results_of_the_test_case(TestRail.RUN_ID.value, TestRail.CASE_ID.value, result_fields)
            step.clear_dir(ConfigProject.get_instance().name_screen())
