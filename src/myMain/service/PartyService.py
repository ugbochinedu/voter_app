from typing import List

from src.myMain.data.model.Admin import Admin
from src.myMain.data.model.Party import Party
from src.myMain.data.repositories.PartyRepositoryImpl import PartyRepositoryImpl
from src.myMain.data.repositories.PartyRepositoryInterface import PartyRepositoryInterface
from src.myMain.dtos.request.PartyRegistrationRequest import PartyRegistrationRequest
from src.myMain.dtos.response.DeletePartyResponse import DeletePartyResponse
from src.myMain.dtos.response.PartyRegistrationResponse import PartyRegistrationResponse
from src.myMain.exceptions.RegistrationException import RegistrationException
from src.myMain.service.PartyServiceInterface import PartyServiceInterface
from src.myMain.utils.App_utils import App_utils


class PartyServiceImpl(PartyServiceInterface):
    party_repository_impl: PartyRepositoryInterface = PartyRepositoryImpl()

    def register(self, party_registration_request: PartyRegistrationRequest) -> PartyRegistrationResponse:
        party: Party = App_utils.map_party(party_registration_request)
        saved_party: Party = self.party_repository_impl.save(party)
        if saved_party is None: raise RegistrationException("Party registration failed")
        party_registration_response: PartyRegistrationResponse = PartyRegistrationResponse()
        party_registration_response.set_message("Party registration was successful")
        return party_registration_response

    def find_party_by_id(self, id: str) -> Party:
        return self.party_repository_impl.findById(id)

    def delete_by_id(self, id: str) -> DeletePartyResponse:
        self.party_repository_impl.deleteById(id)
        return DeletePartyResponse.set_message("Party Deleted")

    def find_all_parties(self) -> List[Party]:
        return self.party_repository_impl.findAll()
