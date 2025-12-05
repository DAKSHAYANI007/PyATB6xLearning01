from abc import ABC,abstractmethod

class Father(ABC):
    #@abstractmethod #-> cant create object itself
    def __init__(self, name):
        self.name = name

    @abstractmethod
    def loan(self):
        pass

class Amit(Father):

    def loan(self):
        print("Giving the 50K loan")

amit = Amit("AMIT SHARMA")
amit.loan()