from framework.base_element.project_list_item.project_list_item import ProjectListItem


class ListProjects:
    _project_list_item = "//div[@class = 'list-group']/a[text() = '{}']"

    def select_item(self, item_name):
        locator = self._project_list_item.format(item_name)
        ProjectListItem(locator).click()

    def is_project_appeared_on_the_list(self, item_name):
        locator = self._project_list_item.format(item_name)
        project = ProjectListItem(locator)
        project.wait_element_visibility()
        return project.is_element_presence()
