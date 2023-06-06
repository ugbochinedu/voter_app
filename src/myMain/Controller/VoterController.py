from src.myMain.dtos.request.VoterRegistrationRequest import VoterRegistrationRequest
from src.myMain.dtos.response.VoterRegistrationResponse import VoterRegistrationResponse
from src.myMain.service.VoterService import VoterServiceImpl
from src.myMain.service.VoterServiceInterface import VoterServiceInterface


class VoterController:
    voter_service: VoterServiceInterface = VoterServiceImpl()

    def register_new_voter(self, register_voter: VoterRegistrationRequest) -> VoterRegistrationResponse:
        return self.voter_service.register(register_voter)
