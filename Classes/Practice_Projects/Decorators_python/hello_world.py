
# def decorator(func):
#
#     def wrapper():
#         print("Something is happening before the function is called.")
#         func()
#         print("Something is happening after the function is called")
#     return wrapper
#
# def say_whee():
#     print("Whee!")
#
# say_whee = decorator(say_whee)
# print(say_whee)
# print(say_whee())

from datetime import datetime

def stay_quiet_during_night(func):
    def wrapper():
        if 7 < datetime.now().hour < 21:
            func()
        else:
            print("Hush! the neighbors are asleep")
    return wrapper

def say_whee():
    print("Whee!")

say_whee = stay_quiet_during_night(say_whee)
say_whee()
