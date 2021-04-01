import time

import pytest

from hm_1.tasks.task_03_02 import parallel_load

exepected_result = 1024259


@pytest.mark.parametrize("value", [25, 50, 75, 100, 200, 300, 400, 500])
def test_power_of_two_returns_true(value: int):
    start_time = time.time()
    actual_result = parallel_load(value)
    assert (
        bool((time.time() - start_time) <= 60.0 and actual_result == exepected_result)
        is True
    )


@pytest.mark.parametrize(
    "value",
    [10],
)
def test_power_of_two_returns_false(value: int):
    start_time = time.time()
    actual_result = parallel_load(value)
    assert (
        bool((time.time() - start_time) <= 60.0 and actual_result == exepected_result)
        is False
    )
