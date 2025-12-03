print("Outside the class") #--> outside the class
class MobilePhone:
    model = None

    def talk(self):
        print("Hi,talking")

print("Outside the class2") # --> Outside the class


#---------how to call class:-------------#
class MobilePhone: #attri
    model = None

    def talk(self):  # behavi
        print("Hi,talking")

iphone=MobilePhone()
iphone.talk() #Using object reference we call the  function

#-----------Adding constructor---------

print("Outside the class")


class MobilePhone:
    model = None

    def __init__(self):   # Adding a constructor (DC -default constructor i.e one argument)
        print("DC")

    def talk(self):
        print("Hi,talking")


iphone = MobilePhone()
iphone.talk()
print("Outside the class2")

# Note: The moment you call MobilePhone(), constructor will be called automatically.