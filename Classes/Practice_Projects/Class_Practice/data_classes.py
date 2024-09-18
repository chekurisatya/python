#Program to practice Data Classes

from dataclasses import dataclass,field

@dataclass(order = True)
class Book:

    title: str
    author: str
    price: int
    published_year: int = 2024 #Default Value

b1 = Book("The Da Vinci Code", 'Dan Brown', 35)
b2 = Book("The Fellowship Of The Ring", "J.R.R. Tolkien", 50)
print(b1)
print(b2)
print(b1 > b2)

@dataclass(frozen=True)
class Rectangle:
    width: int
    height: int

R1 = Rectangle(5,6)
# R1.width = 20
# R1.height = 10

@dataclass
class Inventory:
    items: list = field(default_factory= list)

    def add_items(self,extra_items):
        self.items.extend(extra_items)

I1 = Inventory(["Tables","Chairs", "Beds"])
print(I1)
I1.add_items(["Nuts","Bolts","Screw Drivers"])
print(I1)

@dataclass(order=True)
class Employee:
    name: str
    salary: int

E1 = Employee("Jason", 25000)
E2 = Employee("Mason", 25001)
print("Employee Dataclass")
print(E1 > E2) #Should Result False
print(E1 < E2) #Should Result True
print(E1 == E2) #Should Result False
print(E1 != E2) #Should Result True

