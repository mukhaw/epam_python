from unittest.mock import Mock

from hm_1.tasks.task_02_04 import cache


def func(a, b):
    return (a ** b) ** 2


def test_cache_return_cache_func_cached_value_100_200():
    mock = Mock(side_effect=func)
    cache_func = cache(mock)
    val_1 = cache_func(100, 200)
    val_2 = cache_func(100, 200)
    assert val_1 is val_2
    mock.assert_called_once()


def test_cache_return_cache_func_cached_value_0_20():
    mock = Mock(side_effect=func)
    cache_func = cache(mock)
    some = 0, 20
    val_1 = cache_func(*some)
    val_2 = cache_func(*some)
    assert val_1 is val_2
    mock.assert_called_once()


def test_cache_return_cache_func_cached_value_1_2():
    mock = Mock(side_effect=func)
    cache_func = cache(mock)
    val_1 = cache_func(1, 2)
    val_2 = cache_func(1, 2)
    assert val_1 is val_2
    mock.assert_called_once()
