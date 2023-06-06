class AdminRegistration:
    def __init__(self):
        self._user_name = ""
        self._password = ""

    def set_user_name(self, user_name):
        self._user_name = user_name

    def get_user_name(self):
        return self._user_name

    def set_password(self, password):
        self._password = password

    def get_password(self):
        return self._password
