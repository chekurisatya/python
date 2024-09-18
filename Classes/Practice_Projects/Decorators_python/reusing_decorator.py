from hello_decorator import do_twice, repeat
from python.Classes.Practice_Projects.Decorators_python.hello_decorator import debug
'''
@debug
@do_twice
def say_whee(town, pincode, country = 'India'):
    print("Whee!")
'''
#@debug
#@do_twice
@repeat(times=5)
def greet(name, age = 25):
    print(f"Hello {name}!")
    return f"Returning {name}!"

#say_whee('Nidadavole','533401', 'India')
G = greet("Satya", '25')
print(G)

