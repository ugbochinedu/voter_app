from src.myMain.data.repositories.UserInformationInterface import UserInformationInterface
from src.myMain.utils.App_utils import App_utils


class UserInformationImpl(UserInformationInterface):
    def __init__(self):
        self._user_information_list = []

    def findById(self, id):
        for user_information in self._user_information_list:
            if user_information.get_id() == id:
                return user_information
        return None

    def findAll(self):
        return self._user_information_list

    def save(self, userInformation):
        user_information_id = App_utils.generateId()
        userInformation.set_id(user_information_id)
        self._user_information_list.append(userInformation)
        return userInformation

    def deleteById(self, id):
        found_user_information = self.findById(id)
        self._user_information_list.remove(found_user_information)
