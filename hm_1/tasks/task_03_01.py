"""
In previous homework task 4, you wrote a cache function that remembers other function output value. Modify it to be a parametrized decorator, so that the following code:

@cache(times=3)
def some_function():
    pass
Would give out cached value up to times number only. Example:

@cache(times=2)
def f():
    return input('? ')   # careful with input() in python2, use raw_input() instead

 f()
? 1
'1'
f()     # will remember previous value
'1'
f()     # but use it up to two times only
'1'
 f()
? 2
'2'
"""


def func(a, b):
    return a + b


def decorator_maker_with_arguments(time=1):
    def my_decorator(func):
        caching = {}

        def wrapped(*args):
            if args not in caching:
                caching[args] = (func(*args), time)
            else:
                value, count = caching[args]
                if count - 1 == 0:
                    return func(*args)
                else:
                    caching[args] = value, count - 1
            return func(*args)

        return wrapped

    return my_decorator


@decorator_maker_with_arguments(time=3)
def decorated_function_with_arguments(a, b):
    return func(a, b)
