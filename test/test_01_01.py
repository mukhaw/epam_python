import pytest

from hm_1.tasks.task_01_01 import check_power_of_2


@pytest.mark.parametrize("value", [1, 2, 4, 8, 16, 32, 64, 128, 256, 512])
def test_power_of_two_returns_true(value: int):
    assert check_power_of_2(value) is True


@pytest.mark.parametrize(
    "value",
    [0, 3, 144, 56, 31, 511, 1023],
)
def test_power_of_two_returns_false(value: int):
    assert check_power_of_2(value) is False
