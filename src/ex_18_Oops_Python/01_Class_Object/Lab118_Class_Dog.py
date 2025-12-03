class Dog:
    #A             #attribute
    name = None
    breed = None
    height = None
    weight = None


    #B           # behaviour(whenever we create a method,method are always available in class)

    def bark(self):  #the first argument will b self(referring class)
        print("Barking")
        # print(name) -># Methods cant directly access your attribute in case of Python
        print(self.name)

    def talk(self):
        print("Talking")

print("Outside ?")
chow = Dog()    #Create an object of a class with same name and add brackets, this chow object can access all methods,attributes
# Dog() - Object
# chow -> Object Ref.
rancho = Dog()