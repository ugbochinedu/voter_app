from unittest import TestCase

from src.myMain.dtos.request.AdminRegistrationRequest import AdminRegistration
from src.myMain.dtos.response.AdminRegistrationResponse import AdminRegistrationResponse
from src.myMain.exceptions.RegistrationException import RegistrationException
from src.myMain.service.AdminService import AdminServiceImpl
from src.myMain.service.AdminServiceInterface import AdminServiceInterface


class TestAdminServiceImpl(TestCase):

    def test_register(self):
        admin_service: AdminServiceInterface = AdminServiceImpl()
        admin_registration: AdminRegistration = AdminRegistration()
        admin_registration.set_user_name("nggdgd")
        admin_registration.set_password("123yh")

        try:
            admin_registration_response: AdminRegistrationResponse = admin_service.register(admin_registration)
            self.assertIsNotNone(admin_registration_response)
            # raise RegistrationException("This is a custom exception")
        except RegistrationException as e:
            print(e)

