class LogContent:
    def __init__(self):
        self.line = ""
        self.date = ""
        self.time = ""
        self.log_level = ""
        self.pid = ""
        self.tid = ""
        self.tag = ""
        self.message = ""

    def set_log_content_line(self, line):
        self.line = line

    def set_log_content_date(self, date):
        self.date = date

    def set_log_content_time(self, time):
        self.time = time

    def set_log_content_log_level(self, log_level):
        self.log_level = log_level

    def set_log_content_pid(self, pid):
        self.pid = pid

    def set_log_content_tid(self, tid):
        self.tid = tid

    def set_log_content_tag(self, tag):
        self.tag = tag

    def set_log_content_message(self, message):
        self.message = message
