from src.myMain.data.repositories.PartyRepositoryInterface import PartyRepositoryInterface
from src.myMain.utils.App_utils import App_utils


class PartyRepositoryImpl(PartyRepositoryInterface):
    def __init__(self):
        self._parties = []

    def findById(self, id):
        for party in self._parties:
            if party.get_id() == id:
                return party
        return None

    def findAll(self):
        return self._parties

    def save(self, party):
        party.set_id(App_utils.generateId())
        self._parties.append(party)
        return party

    def deleteById(self, id):
        party = self.findById(id)
        self._parties.remove(party)
