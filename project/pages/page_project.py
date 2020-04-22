from framework.base_element.label.label import Label
from project.forms.test_list import TestList


class PageProject:
    test_list = TestList()
    _page_project = "//ol[@class = 'breadcrumb']/li[text() = '{}']"

    def page_project_is_open(self, project_name):
        locator = self._page_project.format(project_name)
        return Label(locator).is_element_presence()
