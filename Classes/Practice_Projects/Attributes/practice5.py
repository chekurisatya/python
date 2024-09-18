'''
 Using getattr() with Methods
Write a class Calculator with methods add, subtract, multiply, and divide.
Use getattr() to dynamically call one of these methods based on user input.
'''
class Calculator:
    def add(self, a, b):
        return a + b
    def subtract(self, a, b):
        return a - b
    def multiply(self, a, b):
        return a * b
    def divide(self, a, b):
        return a / b

cal_1 = Calculator()
add_cal = getattr(cal_1, 'add')
sub_cal = getattr(cal_1, 'subtract')
mul_cal = getattr(cal_1, 'multiply')
div_cal = getattr(cal_1, 'divide')

print(add_cal(7,8))
print(sub_cal(20,10))
print(mul_cal(7,8))
print(div_cal(49,7))