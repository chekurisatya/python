from datetime import date
'''
class MyClass:
    class_var = 0

    def __init__(self, value):
        self.instance_var = value

    @classmethod
    def class_method(cls, x):
        cls.class_var += x
        return cls.class_var

myObj1 = MyClass(5)
myObj2 = MyClass(10)

print(myObj1.class_method(6))
print(myObj1.class_method(10))
print(myObj1.class_var)
print(MyClass.class_method(10))
'''

class Employee:
    def __init__(self, name, birth_date):
        self._name = name
        self.birth_date = birth_date

    @property
    def name(self):
        return self._name

    @name.setter
    def name(self,value):
        self._name = value.upper()

    @property
    def birth_date(self):
        return self._birth_date

    @birth_date.setter
    def birth_date(self, value):
        self._birth_date = date.fromisoformat(value)

E1 = Employee("John Doe", "2001-01-01")
print(E1.name)
E1.name = "John Micheal Doe"
print(E1.name)
print(E1.birth_date)
