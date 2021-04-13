import time

import pytest

from hm_1.tasks.task_03_02 import parallel_load


@pytest.mark.parametrize("value", [25, 50, 75, 100, 200, 300, 400, 500])
def test_parallel_load_works_less_than_a_minute(value: int):
    start_time = time.time()
    actual_result = parallel_load(value)
    expected_result = 1025932
    assert (
        bool((time.time() - start_time) <= 60.0 and actual_result == expected_result)
        is True
    )


@pytest.mark.parametrize(
    "value",
    [10],
)
def test_parallel_load_works_more_than_a_minute(value: int):
    start_time = time.time()
    actual_result = parallel_load(value)
    expected_result = 1025932
    assert (
        bool((time.time() - start_time) <= 60.0 and actual_result == expected_result)
        is False
    )
