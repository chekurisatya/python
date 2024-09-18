'''
 Setting Attributes Dynamically with setattr()
Create a class Car with attributes make, model, and year. Use setattr() to dynamically set an attribute color for an instance of Car.
'''

class Car:
    def __init__(self, make,model,year):
        self.make = make
        self.model = model
        self.year = year

Car_1 = Car("Hyundai","Tuscon",2021)
setattr(Car_1, 'color','Grey')
print(getattr(Car_1,'color'))