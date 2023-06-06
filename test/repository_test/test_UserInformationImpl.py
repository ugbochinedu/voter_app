from unittest import TestCase

from src.myMain.data.model.UserInformation import UserInformation
from src.myMain.data.repositories.UserInformationImpl import UserInformationImpl
from src.myMain.data.repositories.UserInformationInterface import UserInformationInterface


class TestUserInformationImpl(TestCase):
    def test_user_information_can_save(self):
        user_info_repo: UserInformationInterface = UserInformationImpl()
        user_info: UserInformation = UserInformation()
        saved_user_info: UserInformation = user_info_repo.save(user_info)
        self.assertIsNotNone(saved_user_info)

    def test_find_all(self):
        user_info_repo: UserInformationInterface = UserInformationImpl()
        user_info: UserInformation = UserInformation()
        user_info1: UserInformation = UserInformation()
        saved_user_info1: UserInformation = user_info_repo.save(user_info1)
        saved_user_info: UserInformation = user_info_repo.save(user_info)
        self.assertEqual(2,len(user_info_repo.findAll()))

    def test_find_by_id(self):
        user_info_repo : UserInformationInterface = UserInformationImpl()
        user_info: UserInformation = UserInformation()
        saved_user_info: UserInformation = user_info_repo.save(user_info)
        self.assertIsNotNone(user_info_repo.findById(saved_user_info.get_id()))

    def test_delete_by_id(self):
        user_info_repo: UserInformationInterface = UserInformationImpl()
        user_info: UserInformation = UserInformation()
        saved_user_info: UserInformation = user_info_repo.save(user_info)
        user_info_repo.deleteById(saved_user_info.get_id())
        self.assertEqual(0,len(user_info_repo.findAll()))