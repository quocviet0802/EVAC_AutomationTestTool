class TestCase:
    def __init__(self):
        self.test_case_name = ""
        self.test_steps = ""
        self.test_exceptions = ""

    def set_test_case_name(self, name):
        self.test_case_name = name

    def set_test_steps(self, test_step):
        self.test_steps = test_step

    def set_test_exceptions(self, exceptions):
        self.test_exceptions = exceptions

