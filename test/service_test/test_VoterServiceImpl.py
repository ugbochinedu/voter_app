from unittest import TestCase

from src.myMain.dtos.request.VoterRegistrationRequest import VoterRegistrationRequest
from src.myMain.dtos.response.VoterRegistrationResponse import VoterRegistrationResponse
from src.myMain.exceptions.RegistrationException import RegistrationException
from src.myMain.service.VoterService import VoterServiceImpl
from src.myMain.service.VoterServiceInterface import VoterServiceInterface


class TestVoterServiceImpl(TestCase):
    def test_register(self):
        voter_service: VoterServiceInterface = VoterServiceImpl()
        voter_registration: VoterRegistrationRequest = VoterRegistrationRequest()
        voter_registration.set_user_name("nggdgd")
        voter_registration.set_password("123yh")

        try:
            voter_registration_response: VoterRegistrationResponse = voter_service.register(voter_registration)
            self.assertIsNotNone(voter_registration_response)
            # raise RegistrationException("This is a custom exception")
        except RegistrationException as e:
            print(e)
