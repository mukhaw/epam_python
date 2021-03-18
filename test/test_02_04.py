from hm_1.tasks.task_02_04 import cache, func


def test_cache_return_cache_func_cached_value_100_200():
    cache_func = cache(func)
    some = 100, 200
    val_1 = cache_func(*some)
    val_2 = cache_func(*some)
    assert val_1 is val_2


def test_cache_return_cache_func_cached_value_0_20():
    cache_func = cache(func)
    some = 0, 20
    val_1 = cache_func(*some)
    val_2 = cache_func(*some)
    assert val_1 is val_2


def test_cache_return_cache_func_cached_value_0_0():
    cache_func = cache(func)
    some = 0, 0
    val_1 = cache_func(*some)
    val_2 = cache_func(*some)
    assert val_1 is val_2
