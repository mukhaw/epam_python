from unittest.mock import Mock

from hm_1.tasks.task_02_04 import cache


def func(a, b):
    return (a ** b) ** 2


mock = Mock(side_effect=func)


def test_cache_return_cache_func_cached_value_100_200():
    cache_func = cache(mock)
    some = 100, 2000
    val_1 = cache_func(*some)
    val_2 = cache_func(*some)
    assert val_1 is val_2


def test_cache_return_cache_func_cached_value_0_20():

    cache_func = cache(mock)
    some = 0, 20
    val_1 = cache_func(*some)
    val_2 = cache_func(*some)
    assert val_1 is val_2


def test_cache_return_cache_func_cached_value_0_0():
    cache_func = cache(mock)
    mock.some = 0, 0
    val_1 = cache_func(*mock.some)
    val_2 = cache_func(*mock.some)
    assert val_1 is val_2


def test_cache_return_cache_func_cached_value_1_2():
    cache_func = cache(mock)
    some = 1, 2
    val_1 = cache_func(*some)
    val_2 = cache_func(*some)
    assert val_1 is val_2
