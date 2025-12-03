class Car:
    name:None
    make:None
    model:None

    def __init__(self,name,make,model):
        self.name=name
        self.make=make
        self.model=model

    def start_engine(self):
        print("Starting a car with the name " + self.name)
        print("Starting a car with the make " + self.make)
        print("Starting a car with the model " + self.model)


lambo = Car("lambo","V6",model="2023")
lambo.start_engine()

print("#=================================================================#")
#one more ex

mg_hector = Car("Hector","1.5+ Turbo","2024")
mg_hector.start_engine()

