from src.myMain.data.repositories.AddressRepositoryInterface import AddressRepositoryInterface
from src.myMain.utils.App_utils import App_utils


class AddressRepositoryImpl(AddressRepositoryInterface):

    def __init__(self):
        self._addresses = []

    def findById(self, id):
        for address in self._addresses:
            if address.get_id() == id:
                return address
        return None

    def findAll(self):
        return self._addresses

    def save(self, address):
        address.set_id(App_utils.generateId())
        self._addresses.append(address)
        return address

    def deleteById(self, id):
        address = self.findById(id)
        if address is not None:
            self._addresses.remove(address)


if __name__ == '__main__':
    add: AddressRepositoryInterface = AddressRepositoryImpl()
    add.findById(1)
