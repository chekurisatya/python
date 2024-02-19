'''
In the class Employee, implement the instance attributes as firstname, lastname and salary.

Create the method from_string() which parses a string containing these attributes and assigns them to the correct properties. 
Properties will be separated by a dash.

How to use a classmethod. And how to use alternate class constructor

Examples
emp1 = Employee("Mary", "Sue", 60000)
emp2 = Employee.from_string("John-Smith-55000")
emp1.firstname ➞ "Mary"

emp1.salary ➞ 60000

emp2.firstname ➞ "John"

emp2.salary ➞ 55000
'''

class Employee():

	def __init__(self, fname, lname, salary):

		self.firstname = fname
		self.lastname = lname
		self.salary = salary

	@classmethod
	def from_string(cls, emp_det):
		firstname, lastname, salary = emp_det.split("-")
		return cls(firstname, lastname, salary)


emp1 = Employee("Mary", "Sue", 60000)
emp2 = Employee.from_string("John-Smith-55000")
emp3 = Employee.from_string("Susan-Walker-70000")
emp4 = Employee.from_string("Michael-Ferry-90000")
emp5 = Employee("Graham", "Derrell", 55000)

print(emp1.firstname)
print(emp1.lastname)
print(emp1.salary)
print(emp2.firstname)
print(emp2.lastname)
print(emp2.salary)
print(emp3.firstname)
print(emp3.lastname)
print(emp3.salary)
print(emp4.firstname)
print(emp4.lastname)
print(emp4.salary)
print(emp5.firstname)
print(emp5.lastname)
print(emp5.salary)