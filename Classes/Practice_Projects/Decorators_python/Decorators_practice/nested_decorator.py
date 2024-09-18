'''
Create two decorators: uppercase that converts the output of a function to uppercase,
and bold that wraps the output in HTML <b> tags. Apply both decorators to a function that returns a string.
'''
def bold(func):
    def bold_wrapper(*args):
        res = '<b>' + func(*args) + '</b>'
        return res
    return bold_wrapper

def uppercase(func):
    def uppercase_wrapper(*args):
        res = '<upper>' + func(*args) + '</upper>'
        return res
    return uppercase_wrapper

@bold
@uppercase
def greet(name):
    return f"Hello, {name}!"

print(greet("Alice"))