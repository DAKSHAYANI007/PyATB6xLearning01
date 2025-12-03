class Dog:
    # Attributes - Instance variables | Data variables
    name = None
    breed = None
    height = None
    weight = None
    race = None

    def __init__(self,nameGiven,breedGiven): #now this is not default c ,it is parameterised constructor.
        print("Param C")
        self.name = nameGiven  #( self.name -> variable name)
        self.breed = breedGiven


    # B
    def bark(self):
        print("Barking")

    def sleep(self):
        print("Who is sleep -> " + self.name)

    def talk(self):
        pass



chow = Dog("chow", "mastiff") # here while creating an object, we are setting values.
rancho = Dog("rancho","desi")

chow.sleep()
rancho.sleep()