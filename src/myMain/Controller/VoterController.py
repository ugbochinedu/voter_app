from src.myMain.data.model.Voter import Voter
from src.myMain.dtos.request.VoterRegistrationRequest import VoterRegistrationRequest
from src.myMain.dtos.response.DeleteVoterResponse import DeleteVoterResponse
from src.myMain.dtos.response.VoterRegistrationResponse import VoterRegistrationResponse
from src.myMain.service.VoterService import VoterServiceImpl
from src.myMain.service.VoterServiceInterface import VoterServiceInterface


class VoterController:
    voter_service: VoterServiceInterface = VoterServiceImpl()

    def register_new_voter(self, register_voter: VoterRegistrationRequest) -> VoterRegistrationResponse:
        return self.voter_service.register(register_voter)

    def find_registered_voter(self, id: str) -> Voter:
        return self.voter_service.find_voter_by_id(id)

    def delete_voter(self, id: str) -> DeleteVoterResponse:
        return self.voter_service.delete_by_id(id)