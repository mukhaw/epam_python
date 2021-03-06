import string

from hm_1.tasks.task_02_05 import custom_range


def test_custom_range_list_with_start_stop_step_returns_part_of_list_with_step():
    actual_result = custom_range(
        [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 34, 45], 1, 11, 2
    )
    expected_result = [1, 3, 5, 7, 9]
    assert actual_result == expected_result


def test_custom_range_list_with_start_stop_returns_part_of_list():
    actual_result = custom_range([1, 2, 3, 4, 5], 1, 4)
    expected_result = [1, 2, 3]
    assert actual_result == expected_result


def test_custom_range_list_with_start_returns_part_of_list_start_to_end():
    actual_result = custom_range([6, 2, 3, 4, 5], 5)
    expected_result = [6, 2, 3, 4]
    assert actual_result == expected_result


def test_custom_range_list_with_stop_returns_part_of_list_0_to_stop():
    actual_result = custom_range([6, 2, 3, 4, 5], 5)
    expected_result = [6, 2, 3, 4]
    assert actual_result == expected_result


def test_custom_range_empty_list():
    actual_result = custom_range([], 5)
    expected_result = "You're wrong"
    assert actual_result == expected_result


def test_custom_range_tuple_with_start_stop_step_returns_part_of_tuple_with_step():
    actual_result = custom_range(
        (1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 34, 45), 1, 11, 2
    )
    expected_result = (1, 3, 5, 7, 9)
    assert actual_result == expected_result


def test_custom_range_tuple_with_start_stop_returns_part_of_tuple():
    actual_result = custom_range((1, 2, 3, 4, 5), 1, 4)
    expected_result = (1, 2, 3)
    assert actual_result == expected_result


def test_custom_range_tuple_with_start_returns_part_of_tuple_start_to_end():
    actual_result = custom_range((6, 2, 3, 4, 5), 5)
    expected_result = (6, 2, 3, 4)
    assert actual_result == expected_result


def test_custom_range_tuple_with_stop_returns_part_of_tuple_0_to_stop():
    actual_result = custom_range((6, 2, 3, 4, 5), 5)
    expected_result = (6, 2, 3, 4)
    assert actual_result == expected_result


def test_custom_range_empty_tuple():
    actual_result = custom_range((), 5)
    expected_result = "You're wrong"
    assert actual_result == expected_result


def test_custom_range_string_with_start_stop_step_returns_part_of_string_with_step():
    actual_result = custom_range(string.ascii_lowercase, "p", "g", -2)
    expected_result = ["p", "n", "l", "j", "h"]
    assert actual_result == expected_result


def test_custom_range_string_with_start_stop_returns_part_of_string():
    actual_result = custom_range(string.ascii_lowercase, "g", "p")
    expected_result = ["g", "h", "i", "j", "k", "l", "m", "n", "o"]
    assert actual_result == expected_result


def test_custom_range_string_with_stop_returns_part_of_string_0_to_stop():
    actual_result = custom_range(string.ascii_lowercase, "g")
    expected_result = ["a", "b", "c", "d", "e", "f"]
    assert actual_result == expected_result


def test_custom_range_list_with_empty_string_stop_returns_part_of_string_0_to_stop():
    actual_result = custom_range([1, 2, 3, 4, "", 5, 6, 7], "")
    expected_result = [1, 2, 3, 4]
    assert actual_result == expected_result
