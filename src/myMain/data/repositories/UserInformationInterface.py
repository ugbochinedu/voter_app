from abc import ABC, abstractmethod


class UserInformationInterface(ABC):
    @abstractmethod
    def findById(self, id):
        pass

    @abstractmethod
    def findAll(self):
        pass

    @abstractmethod
    def save(self, userInformation):
        pass

    @abstractmethod
    def deleteById(self, id):
        pass

