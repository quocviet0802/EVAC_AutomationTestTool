class TestStepResult:
    def __init__(self):
        self.name = ""
        self.type = ""
        self.action = ""
        self.step_result = [("",0)]
        self.exceptions = ""

    def set_test_result_name(self, name):
        self.name = name

    def set_test_result_type(self, type):
        self.type = type

    def set_test_result_action(self, action):
        self.action = action

    def set_test_result_log(self, log):
        self.step_result = log

    def set_test_result_exceptions(self, exceptions):
        self.exceptions = exceptions
