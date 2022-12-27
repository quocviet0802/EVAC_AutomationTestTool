class LogManager:
    def __init__(self):
        self.session_id = ""
        self.log_content = ""

    def set_log_manager_session_id(self, session_id):
        self.session_id = session_id
    
    def set_log_manager_log_content (self, log_content):
        self.log_content = log_content
        