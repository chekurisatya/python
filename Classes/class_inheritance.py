'''
Class Inheritance
'''

class Car():

	def __init__(self, brand, make, color = ' '):
		self.color = color
		self.brand = brand
		self.make = make
		print("Car Sold")

	def __str__(self):
		pass

class DomesticCar(Car):

	def __init__(self, brand, color, tier, make, price):
		Car.__init__(self, color, brand, make)
		self.brand = brand
		self.color = color
		self.tier = tier
		self.make = make
		self.price = price

	def __str__(self):
		return f"This is a {self.color} {self.brand} {self.make} {self.tier} tier. Sold for ${self.price}"

class MilitaryCar(Car):

	def __init__(self, brand, make, militaryBranch):
		Car.__init__(self, brand, make)
		self.brand = brand
		self.make = make
		self.militaryBranch = militaryBranch

	def __str__(self):
		return f"The {self.brand} {self.make} has been deployed with {self.militaryBranch}"

my_car = DomesticCar('Hyundai', 'Grey', "Luxury", 'Tuscon', '35000')
print(my_car)

myMiltaryCar = MilitaryCar('Mahindra', 'Raskshak', 'Gorkha Regiment')
print(myMiltaryCar)