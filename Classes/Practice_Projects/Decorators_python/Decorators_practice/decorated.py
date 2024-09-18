import functools

def decorated_function(original_function):
    print("First")
    print(original_function)
    @functools.wraps(original_function)
    def wrapper():
        print(original_function)
        print("inside")
        return original_function()
    print(wrapper)
    print(3)
    return wrapper

def original():
    print("Achieved Decoration")

decorated_display = decorated_function(original)
print(decorated_display)
print(1)
print(original)
print("End")
decorated_display()
