#3. Logging Function Calls
#Write a decorator log_calls that logs every time a function is called with its arguments and return value.

import functools

def log_calls(addition):
    @functools.wraps(addition)
    def wrapper(*args):
        print(f"Function {addition.__name__} called with arguments {args}")
        res = addition(*args)
        print(f"Function {addition.__name__} returned {res}")
        return res
    return wrapper

@log_calls
def add(a,b):
    return a + b

add(0,1)
add(4,5)
add(10000, 20000)
