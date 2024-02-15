'''
A Program to create a Full Name and Email from Given First name and last name
'''

class Employee():

	def __init__(self, fname, lname):
		self.firstname = fname
		self.lastname = lname
		self.fullname = self.firstname+' '+self.lastname
		self.email = self.firstname.lower()+'.'+self.lastname.lower()+'@company.com'


emp_1 = Employee("John", "Smith")
emp_2 = Employee("Mary",  "Sue")
emp_3 = Employee("Antony", "Walker")
emp_4 = Employee("Joshua", "Senoron")

print(emp_1.firstname)
print(emp_1.lastname)
print(emp_1.fullname)
print(emp_1.email)
print(emp_2.firstname)
print(emp_2.lastname)
print(emp_2.fullname)
print(emp_2.email)
print(emp_3.firstname)
print(emp_3.lastname)
print(emp_3.fullname)
print(emp_3.email)
print(emp_4.firstname)
print(emp_4.lastname)
print(emp_4.fullname)
print(emp_4.email)