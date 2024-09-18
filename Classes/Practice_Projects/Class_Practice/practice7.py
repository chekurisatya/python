'''
Overriding Methods in a Subclass
Extend the previous Vehicle class.
Create a new subclass Truck that overrides the method car_info to include the cargo_capacity attribute.
Test method overriding by calling the method on both Car and Truck.
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

class Truck(Vehicle):

    def __init__(self, make, model, cargo_capacity):
        super().__init__(make, model)
        self.cargo_capacity = cargo_capacity

    def car_info(self):
        return f"Make: {self.make}, Model: {self.model}, Cargo Capacity: {self.cargo_capacity} litres"

C1 = Car("Hyundai", "Tuscon", 4)
print(C1.car_info())
T1 = Truck("Ford", "F-150", 4500)
print(T1.car_info())