from hm_1.tasks.task_07_01 import find_occurrences

example_tree = {
    "first": ["RED", "BLUE"],
    "second": {
        "simple_key": ["simple", "list", "of", "RED", "valued"],
    },
    "third": {
        "abc": "BLUE",
        "jhl": "RED",
        "complex_key": {
            "key1": "value1",
            "key2": "RED",
            "key3": ["a", "lot", "of", "values", {"nested_key": "RED"}],
        },
    },
    "fourth": "RED",
}


def test_find_occurances_returns_number_of_occurances():
    assert find_occurrences(example_tree, "RED") == 6


def test_find_occurances_returns_0():
    assert find_occurrences(example_tree, "REG") == 0
    assert find_occurrences({"1": "2"}, 1) == 0
