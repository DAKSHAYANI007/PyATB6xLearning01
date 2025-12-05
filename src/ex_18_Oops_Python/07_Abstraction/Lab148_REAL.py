from abc import ABC, abstractmethod

class GearBox(ABC):
    @abstractmethod  # Hidden
    def setGear(self):
        pass

class Engine:
    @abstractmethod # Hidden
    def start(self):
        pass

    @abstractmethod # Hidden
    def stop(self):
        pass

class Car(Engine,GearBox):  # I need to complete all the function.

    def start(self):
        print("Starting")

    def stop(self):
        print("Stop")

    def setGear(self):
        print("Gearbox is ready")

    def drive(self):
        self.start()
        self.setGear()
        self.stop()
























tesla = Car()  #""" only this part is shown""" ,Gearbox class,engine are hidden
tesla.drive()