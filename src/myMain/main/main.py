from src.myMain.Controller.VoterController import VoterController
from src.myMain.dtos.request.VoterRegistrationRequest import VoterRegistrationRequest
from src.myMain.utils.Validate import validate_password, validate_username, validate_house_number, \
    validate_street, validate_state, validate_lga, validate_age, validate_gender


class Main:
    voter_controller: VoterController = VoterController()

    def collect_details(self, message):
        return input(message)

    def register_voter(self):
        user_name = validate_username()
        password = validate_password()
        house_number = validate_house_number()
        street = validate_street()
        state = validate_state()
        l_g_a = validate_lga()
        age = validate_age()
        gender = validate_gender()

        register_voter: VoterRegistrationRequest = VoterRegistrationRequest()
        register_voter.set_user_name(user_name)
        register_voter.set_password(password)
        register_voter.set_house_number(house_number)
        register_voter.set_street(street)
        register_voter.set_state(state)
        register_voter.set_local_government_area(l_g_a)
        register_voter.set_age(age)
        register_voter.set_gender(gender)
        print(self.voter_controller.register_new_voter(register_voter))

    def find_registered_voter(self, id):
        pass

    def delete_voter(self, id):
        pass

    def register_party(self):
        pass

    def find_party(self, id):
        pass

    def delete_party(self, id):
        pass

    def find_all_parties(self):
        pass

    def add_admin(self):
        pass


if __name__ == '__main__':
    MainMenu = """
    Hi, select your preferred option
    1-> Register a voter
    2-> Find Registered Voter
    3-> Delete voter
    4-> Register party
    5-> Find Party
    6-> Delete party
    7-> Find all parties
    8-> Add Admin
    
    """
    main = Main()
    # main.collect_details(MainMenu)
    choice = main.collect_details(MainMenu)
    if choice == "1":
        main.register_voter()
    elif choice == "2":
        main.find_registered_voter(id)
    elif choice == "3":
        main.delete_voter(id)
    elif choice == "4":
        main.register_party()
    elif choice == "5":
        main.find_party(id)
    elif choice == "6":
        main.delete_party(id)
    elif choice == "7":
        main.find_all_parties()
    elif choice == "8":
        main.add_admin()
