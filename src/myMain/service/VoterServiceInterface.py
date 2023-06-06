from abc import ABC, abstractmethod
from typing import List

from src.myMain.data.model.Voter import Voter
from src.myMain.dtos.request.VoterRegistrationRequest import VoterRegistrationRequest
from src.myMain.dtos.response import VoterRegistrationResponse
from src.myMain.dtos.response.DeleteVoterResponse import DeleteVoterResponse


class VoterServiceInterface(ABC):
    @abstractmethod
    def register(self,voter_registration_request:VoterRegistrationRequest) -> VoterRegistrationResponse:
        pass

    @abstractmethod
    def find_voter_by_id(self, id:str) -> Voter:
        pass

    @abstractmethod
    def delete_by_id(self, id:str) -> DeleteVoterResponse:
        pass

    @abstractmethod
    def find_all(self) -> List[Voter]:
        pass

