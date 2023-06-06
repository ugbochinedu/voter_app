from src.myMain.dtos.request import AdminRegistrationRequest
from src.myMain.dtos.response.AdminRegistrationResponse import AdminRegistrationResponse
from src.myMain.service.AdminService import AdminServiceImpl
from src.myMain.service.AdminServiceInterface import AdminServiceInterface


class VoterController:
    admin_service: AdminServiceInterface = AdminServiceImpl()

    def register_new_voter(self, register_voter: AdminRegistrationRequest) -> AdminRegistrationResponse:
        return self.admin_service.register(register_voter)
