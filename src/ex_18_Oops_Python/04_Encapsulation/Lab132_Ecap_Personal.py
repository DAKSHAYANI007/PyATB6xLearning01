class Home:

    def __init__(self):
        self.public_var ="father"  # public variable
        self._protected_var="Brother" # Proted var with one underscore
        self.__private__var__dadsa__dadsa__ = "baby" # private variable


    def mom(self):   # Public function
        print(self.__private__var__dadsa__dadsa__)
        self.__wife() # Mom access private wife


    def __wife(self): # Private function
        print("Private wife")


object_ref = Home()
#print(object_ref.public_var)
#object_ref.__wife() ---> We cant access the wife outside
#object_ref.__private_var # --> We cant access the baby


# Our encapsulated mother can access?

object_ref.mom() # yes she can access baby and wife.This is known as encapsulation.
print(object_ref._protected_var) # yes

# ⚠️ Technically accessible, but not recommended

# Protected we generally dont use.


