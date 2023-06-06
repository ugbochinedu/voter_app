class VoterRegistrationRequest:
    def __init__(self):
        self._age = ""
        self._gender = ""
        self._user_name = ""
        self._password = ""
        self._house_number = ""
        self._street = ""
        self._town = ""
        self._state = ""
        self._local_government_area = ""

    def set_age(self, age):
        self._age = age

    def get_age(self):
        return self._age

    def set_gender(self, gender):
        self._gender = gender

    def get_gender(self):
        return self._gender

    def set_user_name(self, user_name):
        self._user_name = user_name

    def get_user_name(self):
        return self._user_name

    def set_password(self, password):
        self._password = password

    def get_password(self):
        return self._password

    def set_house_number(self, house_number):
        self._house_number = house_number

    def get_house_number(self):
        return self._house_number

    def set_street(self, street):
        self._street = street

    def get_street(self):
        return self._street

    def set_state(self, state):
        self._state = state

    def get_state(self):
        return self._state

    def set_town(self, town):
        self._town = town

    def get_town(self):
        return self._town

    def set_local_government_area(self, local_government_area):
        self._local_government_area = local_government_area

    def get_local_government_area(self):
        return self._local_government_area


