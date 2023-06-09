from typing import List

from src.myMain.data.model.Admin import Admin
from src.myMain.data.repositories.AdminRepositoryImpl import AdminRepositoryImpl
from src.myMain.data.repositories.AdminRepositoryInterface import AdminRepositoryInterface
from src.myMain.dtos.request.AdminRegistrationRequest import AdminRegistration
from src.myMain.dtos.response.AdminRegistrationResponse import AdminRegistrationResponse
from src.myMain.dtos.response.DeleteAdminResponse import DeleteAdminResponse
from src.myMain.exceptions.RegistrationException import RegistrationException
from src.myMain.utils.App_utils import App_utils
from src.myMain.service.AdminServiceInterface import AdminServiceInterface


class AdminServiceImpl(AdminServiceInterface):
    admin_repo: AdminRepositoryInterface = AdminRepositoryImpl()

    def register(self, admin_registration_request: AdminRegistration) -> AdminRegistrationResponse:
        admin: Admin = App_utils.map_admin(admin_registration_request)
        saved_admin: Admin = self.admin_repo.save(admin)

        return App_utils.map_admin_response(saved_admin)

    def find_admin_by_id(self, id: str) -> Admin:
        return self.admin_repo.findById(id)

    def delete_by_id(self, id: str) -> DeleteAdminResponse:
        self.admin_repo.deleteById(id)
        return DeleteAdminResponse.set_message("Admin Deleted")

    def find_all_admins(self) -> List[Admin]:
        return self.admin_repo.findAll()
