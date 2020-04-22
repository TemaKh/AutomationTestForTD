class TestModel:
    def __init__(self, project_name=None, test_name=None, test_method_name=None, status=None,
                 environment=None, attachment_type=None, log=None):
        self.project_name = project_name
        self.test_name = test_name
        self.test_method_name = test_method_name
        self.status = status
        self.environment = environment
        self.attachment_type = attachment_type
        self.log = log

    def set_project_name(self, project_name):
        self.project_name = project_name

    def set_test_name(self, test_name):
        self.test_name = test_name

    def set_test_method_name(self, test_method_name):
        self.test_method_name = test_method_name

    def set_status(self, status):
        self.status = status

    def set_environment(self, environment):
        self.environment = environment

    def set_attachment_type(self, attachment_type):
        self.attachment_type = attachment_type

    def set_log(self, log):
        self.log = log

    def __eq__(self, other):
        return self.project_name == other.project_name and self.test_name == other.test_name \
               and self.test_method_name == other.test_method_name and self.status == other.status \
               and self.environment == other.environment and self.attachment_type == other.attachment_type\
               and self.log == other.log
