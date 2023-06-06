from src.myMain.data.model.UserInformation import UserInformation


class Admin:
    def __init__(self):
        self._user_information = UserInformation()
        self._id = ""

    def set_user_information(self,user_information):
        self._user_information = user_information

    def get_user_information(self):
        return self._user_information

    def set_id(self, id):
        self._id = id

    def get_id(self):
        return self._id

    def __str__(self):
        return f"""
        UserInformation : {self._user_information}
        Id : {self._id}
        """