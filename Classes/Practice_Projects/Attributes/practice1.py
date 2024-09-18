'''
Basic Attribute Access with getattr()
Write a class Person with attributes name, age, and city. Use getattr() to print the values of each attribute.
'''

class Person:
    def __init__(self,name,age,city):
        self.name = name
        self.age = age
        self.city = city

Per_1 = Person("Satya",39,"Kitchener")
print(getattr(Per_1,'name'))
print(getattr(Per_1,'age'))
print(getattr(Per_1,'city'))