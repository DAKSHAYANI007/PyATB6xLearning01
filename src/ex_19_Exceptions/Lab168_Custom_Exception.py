class InvalidAgeException(Exception):
    pass


def check_zero_div(a):
    if a == 0:
        raise ZeroDivisionError("Can't divide with zero")# Built in error


def can_you_drink(age):
    if age < 18:
        raise InvalidAgeException("Invalid age of drinking")# custom error


can_you_drink(9)
#can_you_drink(25)