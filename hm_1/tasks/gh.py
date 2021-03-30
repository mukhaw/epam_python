"""
In previous homework task 4, you wrote a cache function that remembers other function output value. Modify it to be a parametrized decorator, so that the following code:

@cache(times=3)
def some_function():
    pass
Would give out cached value up to times number only. Example:

@cache(times=2)
def f():
    return input('? ')   # careful with input() in python2, use raw_input() instead

>>> f()
? 1
'1'
>>> f()     # will remember previous value
'1'
>>> f()     # but use it up to two times only
'1'
>>> f()
? 2
'2'
"""
"""
from typing import Callable
def func(a):
    print('Function set up')
    return a+1
def cache(times = 1) -> Callable:
    caching = {}
    def cache_func(*args):
        time = 0
        print(args)
        if args not in caching:
            time += 1
            caching[args] = func(*args),time
        return caching[args]
    print(caching)
    return cache_func
a,b = 100,200
@cache(times = 3)
def func(a,b):
    print('Function set up')
    return a+b
func(a,b)
"""


def func(a, b):
    return a + b


def decorator(func, *args, **kwargs):
    caching = {}

    def inner(function):
        time = 0
        times = kwargs["times"] * kwargs["times"]
        function = func(*args)
        if args not in caching:
            caching[args] = function
        while time != times:
            func(*args)
            time += 1

    return inner


some = 1, 2
count = 0


@decorator(func, *some, times=3)
def my_func():
    ...
