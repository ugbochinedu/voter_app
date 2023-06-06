from src.myMain.dtos.request.PartyRegistrationRequest import PartyRegistrationRequest
from src.myMain.dtos.response.PartyRegistrationResponse import PartyRegistrationResponse
from src.myMain.service.PartyService import PartyServiceImpl
from src.myMain.service.PartyServiceInterface import PartyServiceInterface


class PartyController:
    party_service: PartyServiceInterface = PartyServiceImpl()

    def register_new_voter(self, register_voter: PartyRegistrationRequest) -> PartyRegistrationResponse:
        return self.party_service.register(register_voter)
