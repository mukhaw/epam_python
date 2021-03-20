import pytest

from hm_1.tasks.task_03_02 import parallel_load


@pytest.mark.parametrize("value", [25, 50, 75, 100, 200, 300, 400, 500])
def test_power_of_two_returns_true(value: int):
    assert parallel_load(value) is True


@pytest.mark.parametrize(
    "value",
    [10],
)
def test_power_of_two_returns_false(value: int):
    assert parallel_load(value) is False
