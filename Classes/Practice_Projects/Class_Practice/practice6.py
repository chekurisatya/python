'''
Class Inheritance
Create a base class Vehicle with attributes make and model.
Create a derived class Car that inherits from Vehicle and adds an attribute num_doors.
Add a method car_info that prints information about the car, including the number of doors.
'''

class Vehicle:

    def __init__(self, make , model):
        self.make = make
        self.model = model

class Car(Vehicle):

    def __init__(self, make, model, num_doors):
        super().__init__(make, model)
        self.num_doors = num_doors

    def car_info(self):
        return f"Make: {self.make}, Model: {self.model}, Doors: {self.num_doors}"

C1 = Car("Hyundai", "Tuscon", 4)
print(C1.car_info())