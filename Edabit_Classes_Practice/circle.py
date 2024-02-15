# Program to Create a Circle using OOP

class Circle():

	pi = 3.14

	def __init__(self, rad):
		self.radius = rad

	def getArea(self):
		print(self.pi * (self.radius ** 2))

	def getPermieter(self):
		print(2 * self.pi * self.radius)

circy = Circle(11)
circy.getArea()

circy1 = Circle(4.44)
circy1.getPermieter()