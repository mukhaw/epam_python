from hm_1.tasks.task_02_03 import combinations


def test_combinations_with_2_lists_with_not_equal_sizes():
    expected_result = [[1, 3], [2, 3]]
    assert combinations([1, 2], [3]) == expected_result


def test_combinations_with_2_lists_with_not_equal_sizes_1():
    expected_result = [[1, 1], [2, 1]]
    assert combinations([1, 2], [1]) == expected_result


def test_combinations_with_2_lists_with_equal_sizes():
    expected_result = [[1, 3], [1, 4], [2, 3], [2, 4]]
    assert combinations([1, 2], [3, 4]) == expected_result


def test_combinations_with_4_lists_with_not_equal_sizes():
    expected_result = [[1, 3, 4, 5], [1, 3, 4, 6], [2, 3, 4, 5], [2, 3, 4, 6]]
    assert combinations([1, 2], [3], [4], [5, 6]) == expected_result


def test_combinations_with_list():
    expected_result = [[1], [2]]
    assert combinations([1, 2]) == expected_result


def test_combinations_with_3_list():
    expected_result = [[3, 1, 5], [4, 1, 5]]
    assert combinations([3, 4], [1], [5]) == expected_result
