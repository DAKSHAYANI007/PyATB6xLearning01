class Person:    #keyword we need to use here is class, person is name of the class.first letter of the class is always capital.
    # Attributes
    name = None   # In python, you don't need to give any datatype, it can be integer or string i.e why for empty value we mention none.
    id = None      # empty value doesn't contain anything at all.
    age = None
    email = None
    height = None
    gender = None
    phone_no = None
    address = None


    # Behaviour
    def talk(self):  # self - this , self will be first argument in every behaviour.
        print("I can Talk")   # No arg with no return type


    def sleep(self, name):  # Arg with No Return
        print("I am a Method!!")
        print("Sleep", name)

    def sleep2(self, name):  # Arg with Return
        print("I am a Method!!")
        return None

    def walk(self):
        print("I am walking")  #   No arg with no return type

        def method_walk_return(self):  # No Arg with Return
            return "I am walking"

def function_outside():    # this is function outside the class - called function
    print("Outside")
#-----------------------------------------------------------------------


    # Create an Object of the Class
    # ObjectRef = ClassName() -> Object
    geeta = Person() # here Person() is the real object and geeta is the reference
    amit = Person()
    navita = Person()
    print(geeta.name)  # - A
    geeta.sleep("pramod")  # - B


    # By using reference you can access all the attribute and behaviour