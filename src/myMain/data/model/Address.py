from src.myMain.data.model.UserInformation import UserInformation


class Address:
    def __init__(self):
        self._user_information = UserInformation()
        self._house_number = ""
        self._street = ""
        self._town = ""
        self._state = ""
        self._local_government_area = ""
        self._id = ""

    def set_user_information(self, user_information):
        self._user_information = user_information

    def get_user_information(self):
        return self._user_information

    def set_house_number(self, house_number):
        self._house_number = house_number

    def get_house_number(self):
        return self._house_number

    def set_street(self, street):
        self._street = street

    def get_street(self):
        return self._street

    def set_town(self, town):
        self._town = town

    def get_town(self):
        return self._town

    def set_state(self, state):
        self._state = state

    def get_state(self):
        return self._state

    def set_local_government_area(self, local_government_area):
        self._local_government_area = local_government_area

    def get_local_government_area(self):
        return self._local_government_area

    def set_id(self, id):
        self._id = id

    def get_id(self):
        return self._id

    def __str__(self):
        return f"""
        UserInformation : {self._user_information}
        HouseNumber : {self._house_number}
        Street : {self._street}
        Town :{self._town}
        State : {self._state}
        LocalGovernment : {self._local_government_area}
        Id : {self._id}
        """
