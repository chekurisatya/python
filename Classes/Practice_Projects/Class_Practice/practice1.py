'''
Basic Class and Object Creation
Write a class Person with attributes name and age.
Create a method greet that prints "Hello, my name is {name} and I am {age} years old."
Create a few Person objects and call the greet method.
'''

class Person:

    def __init__(self, name, age):
        self.name = name
        self.age = age

    def greet(self):
        return f"Hello, my name is {self.name} and I am {self.age} year old."

Per_1 = Person("Aasritha", 9)
Per_2 = Person("Akshaya", 0.6)
Per_3 = Person("Sravani", 36)

print(Per_1.greet())
print(Per_2.greet())
print(Per_3.greet())