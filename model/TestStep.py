class TestStep:
    def __init__(self):
        self.test_step_name = ""
        self.test_step_type = ""
        self.test_step_action = ""
        self.test_step_log = ""
        self.test_step_exceptions = ""

    def set_test_step_name(self, name):
        self.test_step_name = name

    def set_test_step_type(self, type):
        self.test_step_type = type

    def set_test_step_action(self, action):
        self.test_step_action = action

    def set_test_step_log(self, log):
        self.test_step_log = log

    def set_test_step_exceptions(self, exceptions):
        self.test_exceptions = exceptions

