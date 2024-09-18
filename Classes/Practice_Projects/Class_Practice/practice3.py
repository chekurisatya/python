'''
3. Class with a Method and Attributes
Create a class Rectangle with attributes length and width.
Add a method area that returns the area of the rectangle and a method perimeter that returns the perimeter.
'''

class Rectangle:

    def __init__(self, length, width):
        self.length = length
        self.width = width

    def area(self):
        rec_area = self.length * self.width
        return f"The Area of the Rectangle is {rec_area}"

    def perimeter(self):
        rec_peri = 2*self.length + 2*self.width
        return f"The Perimeter of the Rectable is {rec_peri}"

R1 = Rectangle(10,20)
R2 = Rectangle(40,50)
print(R1.area())
print(R2.perimeter())