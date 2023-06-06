from abc import ABC, abstractmethod


class AdminRepositoryInterface(ABC):
    @abstractmethod
    def findById(self, id):
        pass

    @abstractmethod
    def findAll(self):
        pass

    @abstractmethod
    def save(self, admin):
        pass

    @abstractmethod
    def deleteById(self, id):
        pass
