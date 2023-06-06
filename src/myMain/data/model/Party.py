from src.myMain.data.model.UserInformation import UserInformation


class Party:
    def __init__(self):
        self._user_information = UserInformation()
        self._name = ""
        self._id = " "

    def set_user_information(self, user_information):
        self._user_information = user_information

    def get_user_information(self):
        return self._user_information

    def set_name(self, name):
        self._name = name

    def get_name(self):
        return self._name

    def set_id(self, id):
        self._user_information = id

    def get_id(self):
        return self._id

    def __repr__(self):
        return f"""
        Party Name: {self._name} 
        UserInformation : {self._user_information}
        Id : {self._id}
        """
