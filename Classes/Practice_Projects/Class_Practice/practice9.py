'''
Class Composition
Create two classes: Engine with attributes horsepower and type, and Car with attributes make, model, and an Engine object.
The Car class should have a method car_info that prints information about the car and its engine.
'''
class Engine:
    # Define __init__ method for Engine class
    def __init__(self, horsepower, type):
        self.horsepower = horsepower
        self.type = type

class Car:
    # Define __init__ method and car_info for Car class
    def __init__(self, make, model, engine):
        self.make = make
        self.model = model
        self.engine = engine

    def car_info(self):
        return f"Car Make: {self.make}, Model: {self.model}, Horsepower: {self.engine.horsepower}, Type: {self.engine.type}"

E1 = Engine(7800, "Electric")
C1 = Car("Mustang", "mach-E", E1)
print(C1.car_info())
