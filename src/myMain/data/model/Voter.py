from src.myMain.data.model.Address import Address
from src.myMain.data.model.UserInformation import UserInformation


class Voter:
    def __init__(self):
        self._user_information = UserInformation()
        self._voter_identification_number = ""
        self._address = Address()
        self._age = ""
        self._gender = ""
        self._id = ""

    def set_user_information(self, user_information):
        self._user_information = user_information

    def get_user_information(self):
        return self._user_information

    def set_voter_identification_number(self, voter_identification):
        self._voter_identification_number = voter_identification

    def get_voter_identification(self):
        return self._voter_identification_number

    def set_address(self, address):
        self._address = address

    def get_address(self):
        return self._address

    def set_age(self, age):
        self._age = age

    def get_age(self):
        return self._age

    def set_gender(self, gender):
        self._gender = gender

    def get_gender(self):
        return self._gender

    def set_id(self, id):
        self._id = id

    def get_id(self):
        return self._id

    def __str__(self):
        return f"""
        UserInformation : {self._user_information}
        VoteIdentificationNumber : {self._voter_identification_number}
        Address : {self._address}
        Age: {self._age}
        Gender : {self._gender}
        Id : {self._id}
        """
