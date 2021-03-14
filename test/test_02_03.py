import pytest

from hm_1.tasks.task_02_03 import combinations


@pytest.fixture()
def actual_result_with_2_lists_with_not_equal_sizes():
    return combinations([1, 2], [3])


@pytest.fixture()
def actual_result_with_2_lists_with_not_equal_sizes_1():
    return combinations([1, 2], [1])


@pytest.fixture()
def actual_result_with_2_lists_with_equal_sizes():
    return combinations([1, 2], [3, 4])


@pytest.fixture()
def actual_result_with_4_lists_with_not_equal_sizes():
    return combinations([1, 2], [3], [4], [5, 6])


@pytest.fixture()
def actual_result_with_list():
    return combinations([1, 2])


def test_combinations_with_2_lists_with_not_equal_sizes(
    actual_result_with_2_lists_with_not_equal_sizes,
):
    expected_result = [[1, 3], [2, 3]]
    assert actual_result_with_2_lists_with_not_equal_sizes == expected_result


def test_combinations_with_2_lists_with_not_equal_sizes_1(
    actual_result_with_2_lists_with_not_equal_sizes_1,
):
    expected_result = [[1, 1], [2, 1]]
    assert actual_result_with_2_lists_with_not_equal_sizes_1 == expected_result


def test_combinations_with_2_lists_with_equal_sizes(
    actual_result_with_2_lists_with_equal_sizes,
):
    expected_result = [[1, 3], [1, 4], [2, 3], [2, 4]]
    assert actual_result_with_2_lists_with_equal_sizes == expected_result


def test_combinations_with_4_lists_with_not_equal_sizes(
    actual_result_with_4_lists_with_not_equal_sizes,
):
    expected_result = [[1, 3, 4, 5], [1, 3, 4, 6], [2, 3, 4, 5], [2, 3, 4, 6]]
    assert actual_result_with_4_lists_with_not_equal_sizes == expected_result


def test_combinations_with_list(actual_result_with_list):
    expected_result = [[1], [2]]
    assert actual_result_with_list == expected_result
