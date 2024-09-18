#1. Basic Function Decorator
#Write a decorator repeat that runs a function twice.

def repeat(item):
    def inner():
        item()
        item()
    return inner

@repeat
def say_hello():
    print("Hello")

say_hello()


