import re


def collect_details(details):
    return input(details)


def validate_username():
    user_name = collect_details("Enter your firstname: ")
    match = re.match(r'^[a-zA-Z ''-]*$', user_name)
    if match:
        return True
    else:
        print('invalid, username should not contain numbers, put in letters only')
        validate_username()
    return user_name


def validate_password():
    password = collect_details("Enter your password: ")
    match = re.match(r'^(?=.*[A-Z])(?=.*[a-z])(?=.*\d)[A-Za-z0-9]{8,}$', password)
    if match:
        return True
    else:
        print("Invalid word combination. Enter at least one Capital letter, one small letter, one number and 8 "
              "characters")
        validate_password()
    return password


def validate_house_number():
    house_number = collect_details("Enter your house number: ")
    match = re.match(r'^\d+', house_number)
    if match:
        return True
    else:
        print("Enter valid number")
        validate_house_number()
    return house_number


def validate_street():
    street = collect_details("Enter your Street: ")
    match = re.match(r'^[a-zA-Z ''-]*$', street)
    if match:
        return True
    else:
        print('invalid, Your street should not contain numbers, put in letters only')
        validate_street()
    return street


def validate_state():
    state = collect_details("Enter your State: ")
    match = re.match(r'^[a-zA-Z ''-]*$', state)
    if match:
        return True
    else:
        print('invalid, Your state should not contain numbers, put in letters only')
        validate_state()
    return state


def validate_lga():
    lga = collect_details("Enter your local government: ")
    match = re.match(r'^[a-zA-Z ''-]*$', lga)
    if match:
        return True
    else:
        print('invalid, Your lga should not contain numbers, put in letters only')
        validate_lga()
    return lga


def validate_age():
    age = collect_details("Enter your age: ")
    match = re.match(r'^\d+', age)
    if match:
        return True
    else:
        print("Enter valid number")
        validate_age()
    return age


def validate_gender():
    gender = collect_details("Enter your gender. male or female: ")
    match = re.match(r'^[a-zA-Z]*$', gender)
    if match:
        return True
    else:
        print("invalid, Your gender should not contain numbers, put in letters only")
        validate_gender()