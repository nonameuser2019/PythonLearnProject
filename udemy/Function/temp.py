import time
from functools import wraps
from timeit import default_timer as timer
import math


def measure_time(func):
    def inner(*args, **kwargs):
        start = timer()
        func(*args, **kwargs)
        end = timer()

        print(f'Function: {func.__name__} took {end - start} for execution')
    return inner


@measure_time
def factorial(num):
    time.sleep(3)
    return math.factorial(num)


fact = factorial(1000)
