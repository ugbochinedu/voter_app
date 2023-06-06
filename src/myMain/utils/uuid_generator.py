import uuid


class Id_Generator:

    @staticmethod
    def generate_id():
        empty_string = ""
        for i in range(0, len(Id_Generator.generate_random_uuid())):
            if i % 4 == 0:
                empty_string += " "
                empty_string += Id_Generator.generate_random_uuid()[i]

            if Id_Generator.generate_random_uuid() == "-":
                continue

            empty_string += Id_Generator.generate_random_uuid()[i]
        return empty_string.upper()

    @staticmethod
    def generate_random_uuid():
        return str(uuid.uuid4())
