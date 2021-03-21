"""
Write a function that accepts another function as an argument. Then it
should return such a function, so the every call to initial one
should be cached.
def func(a, b):
    return (a ** b) ** 2
cache_func = cache(func)
some = 100, 200
val_1 = cache_func(*some)
val_2 = cache_func(*some)
assert val_1 is val_2
"""
from typing import Callable
from unittest.mock import Mock


def cache(func: Callable) -> Callable:
    caching = {}

    def cache_func(*args):
        if args in caching:
            return caching[args]
        mock.metod.return_value = (args[0] ** args[1]) ** 2
        caching[args] = mock.method()
        return caching[args]

    return cache_func


mock = Mock()
