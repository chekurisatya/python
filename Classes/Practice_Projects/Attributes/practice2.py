'''
 Default Value with getattr()
Modify the Person class from the previous exercise. Use getattr() to access an attribute that doesn't exist, providing a default value if the attribute is missing.
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
print(getattr(Per_1,"Job","Enginner"))
