from enum import Enum


class Gender(int, Enum):
    MALE = 1
    FEMALE = 2


for i in Gender:
    print(i)


def __str__(self):
    return f"""
    Male : {self.male}
    Female : {self.female}
    """
