# Encapsulation -
# Hide the data members(class variables, instance variables)
# by using only the methods.


class Car:
    def __init__(self):
        self.public_pramod = "pramod"  # Public variable,so available everywhere.

        self.__private_baby = "pass123" # "__" means private variable.

    # How to access my private variable?, creating a separate function.
    def nany(self):
        self.__password_yogesh_private = "345"

object_ref = Car()

print(object_ref.public_pramod)
# print(object_ref.__private_baby)

object_ref.nany() # only this can use/change my private variable
