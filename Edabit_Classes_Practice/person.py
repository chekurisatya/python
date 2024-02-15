'''
A Class program to find an older person than me.
'''

class Person():

	def __init__(self, name, age):
		self.name = name
		self.age = age

	def compare_age(self, obj):
		if self.age < obj.age:
			print ("{} is older than me.".format(obj.name))
		elif self.age > obj.age:
			print ("{} is younger than me.".format(obj.name))
		else:
			print ("{} is the same age as me.".format(obj.name))

p1 = Person("Samuel", 24)
p2 = Person("Joel", 36)
p3 = Person("Lily", 24)

p1.compare_age(p2)

p2.compare_age(p1)

p1.compare_age(p3) 