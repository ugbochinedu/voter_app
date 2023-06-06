from email import utils
from typing import List

from src.myMain.data.model.Voter import Voter
from src.myMain.data.repositories.VoterInterface import VoterInterface
from src.myMain.data.repositories.VoterRepoImpl import VoterRepoImpl
from src.myMain.dtos.request.VoterRegistrationRequest import VoterRegistrationRequest
from src.myMain.dtos.response.VoterRegistrationResponse import VoterRegistrationResponse
from src.myMain.dtos.response.DeleteVoterResponse import DeleteVoterResponse
from src.myMain.exceptions.RegistrationException import RegistrationException
from src.myMain.service.VoterServiceInterface import VoterServiceInterface
from src.myMain.utils.App_utils import App_utils


class VoterServiceImpl(VoterServiceInterface):
    voter_repo: VoterInterface = VoterRepoImpl()

    def register(self, voter_registration_request: VoterRegistrationRequest) -> VoterRegistrationResponse:
        voter: Voter = App_utils.map_voter(voter_registration_request)
        saved_voter: Voter = self.voter_repo.save(voter)
        if saved_voter is None: raise RegistrationException("Voter registration failed")
        voter_registration_response: VoterRegistrationResponse = VoterRegistrationResponse()
        voter_registration_response.set_message("Voter registration was successful")
        return voter_registration_response

    def find_voter_by_id(self, id: str) -> Voter:
        return self.voter_repo.findById(id)

    def delete_by_id(self, id: str) -> DeleteVoterResponse:
        self.voter_repo.deleteById(id)
        return DeleteVoterResponse.set_message("Voter deleted successful")

    def find_all(self) -> List[Voter]:
        return self.voter_repo.findAll()
