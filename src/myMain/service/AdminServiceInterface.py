from abc import ABC, abstractmethod
from typing import List

from src.myMain.data.model.Admin import Admin
from src.myMain.dtos.request import AdminRegistrationRequest
from src.myMain.dtos.response.AdminRegistrationResponse import AdminRegistrationResponse
from src.myMain.dtos.response.DeleteAdminResponse import DeleteAdminResponse


class AdminServiceInterface(ABC):
    @abstractmethod
    def register(self, admin_registration_request: AdminRegistrationRequest) -> AdminRegistrationResponse:
        pass

    @abstractmethod
    def find_admin_by_id(self, id: str) -> Admin:
        pass

    @abstractmethod
    def delete_by_id(self, id: str) -> DeleteAdminResponse:
        pass

    @abstractmethod
    def find_all_admins(self) -> List[Admin]:
        pass
