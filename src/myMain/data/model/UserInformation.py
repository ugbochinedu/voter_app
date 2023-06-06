class UserInformation:
    def __init__(self):
        self._user_name = ""
        self._password = ""
        self._id = ""

    def set_user_name(self, user_name):
        self._user_name = user_name

    def get_user_name(self):
        return self._user_name

    def set_password(self, password):
        self._password = password

    def get_password(self):
        return self._password

    def set_id(self, id):
        self._id = id

    def get_id(self):
        return self._id

    def __str__(self):
        return f"""
        UserName: {self._user_name}
        PassWord: {self._password}
        Id : {self._id}
        """
