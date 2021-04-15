from hm_1.tasks.task_03_02 import parallel_load


def test_parallel_load_works_less_than_a_minute():
    expected_result = 1025932
    assert parallel_load() == expected_result
