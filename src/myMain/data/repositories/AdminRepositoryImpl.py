from src.myMain.data.repositories.AdminRepositoryInterface import AdminRepositoryInterface
from src.myMain.utils.App_utils import App_utils


class AdminRepositoryImpl(AdminRepositoryInterface):
    def __init__(self):
        self._admins = []

    def findById(self, id):
        for admin in self._admins:
            if admin.get_id() == id:
                return admin
        return None

    def findAll(self):
        return self._admins

    def save(self, admin):
        admin.set_id(App_utils.generateId())
        self._admins.append(admin)
        return admin

    def deleteById(self, id):
        admin = self.findById(id)
        if admin is not None:
            self._admins.remove(admin)
