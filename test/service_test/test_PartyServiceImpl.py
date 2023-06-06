from unittest import TestCase

from src.myMain.dtos.request.PartyRegistrationRequest import PartyRegistrationRequest
from src.myMain.dtos.response.PartyRegistrationResponse import PartyRegistrationResponse
from src.myMain.exceptions.RegistrationException import RegistrationException
from src.myMain.service.PartyService import PartyServiceImpl
from src.myMain.service.PartyServiceInterface import PartyServiceInterface


class TestPartyServiceImpl(TestCase):
    def test_register(self):
        party_service: PartyServiceInterface = PartyServiceImpl()
        party_registration: PartyRegistrationRequest = PartyRegistrationRequest()
        party_registration.set_user_name("nggdgd")
        party_registration.set_password("123yh")

        try:
            party_registration_response: PartyRegistrationResponse = party_service.register(party_registration)
            self.assertIsNotNone(party_registration_response)
            # raise RegistrationException("This is a custom exception")
        except RegistrationException as e:
            print(e)
