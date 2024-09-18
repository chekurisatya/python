'''
 Timing Function Execution
Create a decorator timeit that calculates and prints the execution time of a function.
'''

import functools
import time

def timeit(func):
    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        start = time.perf_counter()
        result = func(*args, **kwargs)
        end = time.perf_counter()
        runTime = end - start
        print(f"The Functions {func.__name__}() took {runTime:.4f} secs to execute")
        return result
    return wrapper
'''
@timeit
def some_function():
    res = 0
    for _ in range(100000):
        res = res + _
    return res

print(some_function())
'''