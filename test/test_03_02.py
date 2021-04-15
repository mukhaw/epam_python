from hm_1.tasks.task_03_02 import parallel_load

exepected_result = 1024259


def test_power_of_two_returns_true():
    assert parallel_load() == exepected_result
