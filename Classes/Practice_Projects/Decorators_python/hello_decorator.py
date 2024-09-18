import functools
import time
'''
def decorator(func):

    def wrapper():
        print("Something is happening before the function is called.")
        func()
        print("Something is happening after the function is called")
    return wrapper

@decorator
def say_whee():
    print("Whee!")
'''
def do_twice(func):
    @functools.wraps(func)
    def wrapper_do_twice(*args, **kwargs):
        #func(*args, **kwargs)
        return func(*args, **kwargs)
    return wrapper_do_twice

#say_whee()

def debug(func):
    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        args_repr = [repr(a) for a in args]
        kwargs_repr = [f"{k} = {repr(v)}" for k,v in kwargs.items()]
        signature = ",".join(args_repr + kwargs_repr)
        print(f"Calling {func.__name__} with arguments {signature}")
        value = func(*args, **kwargs)
        print(f"Returning {func.__name__} with value {repr(value)}")
        return value
    return wrapper

def repeat(times):
    def decorator_repeat(func):
        @functools.wraps(func)
        def repeat_wrapper(*args, **kwargs):
            for _ in range(times):
                value = func(*args, **kwargs)
            return value
        return repeat_wrapper
    return decorator_repeat


'''
def slow_down(func):
    @functools.wraps(func)
    def wrapper_slow(*args):
        time.sleep(5)
        return func(*args)
    return wrapper_slow

@slow_down
def countdown(num):
    if num < 1:
        print("ListOff!")
    else:
        print(num)
        countdown(num - 1)

countdown(3)
'''