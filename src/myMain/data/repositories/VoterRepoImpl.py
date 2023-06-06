from typing import List

from src.myMain.data.model.Voter import Voter
from src.myMain.data.repositories.VoterInterface import VoterInterface
from src.myMain.utils.uuid_generator import Id_Generator


class VoterRepoImpl(VoterInterface):

    def __init__(self):
        self._list_of_voters: List[Voter] = []

    def findById(self, id) -> Voter | None:
        for voter in self._list_of_voters:
            if voter.get_id() == id:
                return voter
        return None

    def findAll(self) -> List[Voter]:
        return self._list_of_voters

    def save(self, voter) -> Voter:
        if self.voter_does_not_exist(voter):
            self.save_new_voter(voter)
        return voter

    def deleteById(self, id) -> bool:
        found_voter = self.findById(id)
        if found_voter is not None:
            self._list_of_voters.remove(found_voter)
            return True

    def voter_does_not_exist(self, voter: Voter) -> bool:
        if voter not in self._list_of_voters and voter.get_id() == "":
            return True
        return False

    def save_new_voter(self, voter: Voter):
        voter.set_id(Id_Generator.generate_id())
        # print(voter.get_id())
        self._list_of_voters.append(voter)


