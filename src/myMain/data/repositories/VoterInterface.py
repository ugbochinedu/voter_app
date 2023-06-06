from abc import ABC, abstractmethod

from src.myMain.data.model.Voter import Voter


class VoterInterface(ABC):
    @abstractmethod
    def findById(self, id) -> Voter | None:
        pass

    @abstractmethod
    def findAll(self) -> dict[str: Voter]:
        pass

    @abstractmethod
    def save(self, voter) -> Voter:
        pass

    @abstractmethod
    def deleteById(self, id) -> bool:
        pass
