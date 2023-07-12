from src.myMain.data.model.Party import Party
from src.myMain.dtos.request.PartyRegistrationRequest import PartyRegistrationRequest
from src.myMain.dtos.response.PartyRegistrationResponse import PartyRegistrationResponse
from src.myMain.service.PartyService import PartyServiceImpl
from src.myMain.service.PartyServiceInterface import PartyServiceInterface


class PartyController:
    party_service: PartyServiceInterface = PartyServiceImpl()

    def register_new_voter(self, register_voter: PartyRegistrationRequest) -> PartyRegistrationResponse:
        return self.party_service.register(register_voter)

    def find_party(self, id: str) -> Party:
        return self.party_service.find_party_by_id(id)

    def