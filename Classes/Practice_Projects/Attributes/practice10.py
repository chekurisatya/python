'''
10. Overriding Attributes Dynamically
Write a class Device with attributes brand, model, and price.
Use setattr() to override these attributes dynamically, even if they already exist.
'''

class Device:
    def __init__(self, brand, model, price):
        self.brand = brand
        self.model = model
        self.price = price

    def update_attributes(self, attribute, value):
        if hasattr(self, attribute):
            setattr(self, attribute, value)
            print(f"Update {attribute} to {value}")
        else:
            print(f"{attribute} is not found")

    def display_info(self):
        print(f"Brand: {self.brand}, Model: {self.model}, Price: {self.price}")

Phone_1 = Device("Apple", "iPhone 14", 1499)

Phone_1.display_info()

Phone_1.update_attributes("brand", "Samsung")
Phone_1.update_attributes("model", "Galaxy ZFold")
Phone_1.update_attributes("price", 2499)

Phone_1.display_info()
