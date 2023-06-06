from abc import ABC, abstractmethod
from typing import List

from src.myMain.data.model.Admin import Admin
from src.myMain.data.model.Party import Party
from src.myMain.dtos.request.PartyRegistrationRequest import PartyRegistrationRequest
from src.myMain.dtos.response.DeletePartyResponse import DeletePartyResponse
from src.myMain.dtos.response.PartyRegistrationResponse import PartyRegistrationResponse


class PartyServiceInterface(ABC):
    @abstractmethod
    def register(self, party_registration_request: PartyRegistrationRequest)-> PartyRegistrationResponse:
        pass

    @abstractmethod
    def find_party_by_id(self, id: str) -> Admin:
        pass

    @abstractmethod
    def delete_by_id(self, id: str) -> DeletePartyResponse:
        pass

    @abstractmethod
    def find_all_parties(self) -> List[Party]:
        pass
