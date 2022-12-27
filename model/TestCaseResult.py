class TestCaseResult:
    def __init__(self):
        self.name = ""
        self.test_steps_result = ""
        self.exceptions = ""

    def set_test_case_name(self, name):
        self.test_case_name = name

    def set_test_steps_result(self, test_steps_result):
        self.test_steps_result = test_steps_result

    def set_test_exceptions(self, exceptions):
        self.test_exceptions = exceptions

