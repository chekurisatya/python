'''
7. Using namedtuple for Structured Data
Write a program that defines a namedtuple called Student with fields name, age, and grade.
Create a list of students and print their information.
'''

from collections import namedtuple

Student = namedtuple('Student', ['name', 'age', 'grade'])

# Create a list of students
students = [
    Student(name='Alice', age=20, grade='A'),
    Student(name='Bob', age=21, grade='B'),
    Student(name='Charlie', age=19, grade='C')
]
S1 = Student('Satya','38','B')
a,b,c = S1
print(f"{a}, {b}, {c}")
print(f"{S1[0]}, {S1[1]}, {S1[2]}")
# Print information for each student
for student in students:
    print(f"{student.name} is {student.age} years old and got a grade of {student.grade}")
