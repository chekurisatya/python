from hello_decorator import debug
from timing_function import timeit
@timeit
class Timewaster:

    #@debug
    def __init__(self, num):
        self.num = num

    #@timeit
    def waste_time(self, number):
        for _ in range(number):
            sum([number**2 for number in range(self.num)])

tw = Timewaster(1000)
tw.waste_time(5000)