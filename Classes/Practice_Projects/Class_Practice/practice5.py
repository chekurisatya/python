'''
Class with Static Methods
Write a class MathOperations with static methods add, subtract, multiply, and divide.
 These methods should take two arguments and perform the corresponding operation.
'''

class MathOperations:
    # Define static methods add, subtract, multiply, and divide
    @staticmethod
    def add(a, b):
        return a + b

    @staticmethod
    def subtract(a, b):
        return a - b

    @staticmethod
    def multiply(a, b):
        return a * b

    @staticmethod
    def divide(a, b):
        return a / b

M1 = MathOperations()
print(M1.add(7,8))
print(M1.subtract(14, 24))
print(M1.multiply(6, 6))
print(M1.divide(1232312, 23423423))
 