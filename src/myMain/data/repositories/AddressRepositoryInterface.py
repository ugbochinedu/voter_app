from abc import ABC, abstractmethod


class AddressRepositoryInterface(ABC):
    @abstractmethod
    def findById(self, id):
        pass

    @abstractmethod
    def findAll(self):
        pass

    @abstractmethod
    def save(self, address):
        pass

    @abstractmethod
    def deleteById(self, id):
        pass
