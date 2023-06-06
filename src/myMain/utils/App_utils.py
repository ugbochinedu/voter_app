from src.myMain.data.model.Address import Address
from src.myMain.data.model.Admin import Admin
from src.myMain.data.model.Party import Party
from src.myMain.data.model.UserInformation import UserInformation
from src.myMain.data.model.Voter import Voter
from src.myMain.dtos.request.AdminRegistrationRequest import AdminRegistration
from src.myMain.dtos.request.PartyRegistrationRequest import PartyRegistrationRequest
from src.myMain.dtos.request.VoterRegistrationRequest import VoterRegistrationRequest


class App_utils:

    @staticmethod
    def generateId():
        currentId = 0
        currentId = currentId + 1
        return currentId

    @staticmethod
    def map_admin(admin_registration_request: AdminRegistration) -> Admin:
        admin: Admin = Admin()
        user_information: UserInformation = UserInformation()
        user_information.set_user_name(admin_registration_request.get_password())
        user_information.set_password(admin_registration_request.get_password())
        admin.set_user_information(user_information)
        return admin

    @staticmethod
    def map_party(party_registration_request: PartyRegistrationRequest) -> Party:
        party: Party = Party()
        user_information: UserInformation = UserInformation()
        user_information.set_user_name(party_registration_request.get_user_name())
        user_information.set_password(party_registration_request.get_password())
        party.set_user_information(user_information)
        return party

    @staticmethod
    def map_voter(voter_registration_request: VoterRegistrationRequest) -> Voter:
        voter: Voter = Voter()
        address: Address = Address()
        user_information: UserInformation = UserInformation()
        voter.set_age(voter_registration_request.get_age())
        voter.set_gender(voter_registration_request.get_gender())
        address.set_house_number(voter_registration_request.get_house_number())
        address.set_street(voter_registration_request.get_street())
        address.set_town(voter_registration_request.get_town())
        address.set_state(voter_registration_request.get_state())
        address.set_local_government_area(voter_registration_request.get_local_government_area())
        user_information.set_user_name(voter_registration_request.get_user_name())
        user_information.set_password(voter_registration_request.get_password())
        voter.set_user_information(user_information)
        voter.set_address(address)
        return voter

