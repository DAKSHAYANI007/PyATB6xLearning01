class Person:
    def say_name(self, name):     # Python says that this is not useful/ignored
        print("Hi", name)

    def say_name(self, name, lastname): # So start using this.
        print("Hi,", name, lastname)


t = Person()
t.say_name(" Dakshayani","Yellappa")