from enum import Enum


class JenkinsAuth(Enum):
    WEB_LOGIN = "web_login"
    WEB_PASSWORD = "web_password"
    DB_LOGIN = "db_login"
    DB_PASSWORD = "db_password"
    TESTRAIL_LOGIN = "testrail_login"
    TESTRAIL_PASSWORD = "testrail_password"
