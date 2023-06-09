class VoterRegistrationResponse:
    def __init__(self):
        self.user_name = ""
        self._message = ""

    def set_message(self, message):
        self._message = message

    def get_message(self):
        return self._message

    def set_user_name(self, user_name):
        self.user_name = user_name

    def get_user_name(self):
        return self.user_name

    def __str__(self):
        return f"""
        Username is: {self.user_name}
        message: {self._message}
        """

    def __repr__(self):
        return f"""
        Username is: {self.user_name}
        message: {self._message}
        """
