import pytest

from hm_1.tasks.task_01_01 import check_power_of_2


@pytest.mark.parametrize("value", [1, 4, 9, 16, 64, 144, 65536])
def test_power_of_two_returns_true(value: int):
    assert check_power_of_2(value) is True


@pytest.mark.parametrize(
    "value",
    [0, 2, 56, 678, 1000],
)
def test_power_of_two_returns_false(value: int):
    assert check_power_of_2(value) is False
