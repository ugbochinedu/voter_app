from abc import ABC, abstractmethod


class PartyRepositoryInterface(ABC):
    @abstractmethod
    def findById(self, id):
        pass

    @abstractmethod
    def findAll(self):
        pass

    @abstractmethod
    def save(self, party):
        pass

    @abstractmethod
    def deleteById(self, id):
        pass
