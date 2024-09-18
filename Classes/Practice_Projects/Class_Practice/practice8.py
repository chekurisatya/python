'''
Class with a Class Method
Write a class Employee with a class attribute num_employees that counts the number of Employee objects created.
Add a class method employee_count to return the number of employees created so far.
'''

class Employee:
    # Define num_employees class attribute and methods
    num_employees = 0

    def __init__(self, name):
        self.name = name
        Employee.num_employees += 1

    @classmethod
    def employee_count(cls):
        return cls.num_employees

E1 = Employee("Satya")
E2 = Employee("Sravani")
E3 = Employee("Aasritha")
E4 = Employee("Akshaya")
print(Employee.employee_count())
print(E4.employee_count())