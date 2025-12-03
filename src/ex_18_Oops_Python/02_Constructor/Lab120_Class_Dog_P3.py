class Dog:
    # A
    name = None
    breed = None
    height = None
    weight = None
    def __init__(self):
        print("I will be called")

    # B
    def bark(self):
        print("Barking")

    def sleep(self):
        print("Sleep")

    def talk(self):
        pass # Is means its incomplete function ,we will write it later


# Object Ref
chow_ref = Dog()
mow_ref = Dog()

print(chow_ref.name)
print(mow_ref.name)

# Dog().talk() -> object creation without name