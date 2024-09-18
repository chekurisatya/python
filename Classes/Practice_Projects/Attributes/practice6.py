'''
6. Object Manipulation Based on Attribute Presence
Create a class Student with attributes name and grade. Write a function that checks if a
grade attribute exists using hasattr(). If it does, print the grade; if not, assign a default grade using setattr().
'''

class Student:
    def __init__(self, name):
        self.name = name

def student_grade():
    St = Student("Satya")

    if hasattr(St,'grade'):
        print(St.grade)
    else:
        setattr(St,'grade','Fifth')
        print(St.grade)

student_grade()