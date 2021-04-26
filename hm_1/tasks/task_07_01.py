"""
Given a dictionary (tree), that can contains multiple nested structures.
Write a function, that takes element and finds the number of occurrences
of this element in the tree.
Tree can only contains basic structures like:
    str, list, tuple, dict, set, int, bool
"""
from typing import Any, List


def iterate_all(iterable, returned="key"):
    if isinstance(iterable, dict):

        for key, value in iterable.items():

            if returned == "key":
                yield [key, value]
            elif returned == "value":
                if not (isinstance(value, dict) or isinstance(value, list)):
                    yield value
            else:
                raise ValueError("'returned' keyword only accepts 'key' or 'value'.")
            for ret in iterate_all(value, returned=returned):
                yield ret
    elif isinstance(iterable, list):
        for el in iterable:
            for ret in iterate_all(el, returned=returned):
                yield ret


def convert_to_list(tree: dict) -> List[Any]:
    b = []
    for i in list(iterate_all(tree)):
        for j in i:
            if not isinstance(j, dict):
                b.append(j)
            if isinstance(j, list):
                for k in j:
                    if not isinstance(k, dict):
                        b.append(k)
                b.remove(j)
    return b


def find_occurrences(tree: dict, element: Any) -> int:
    return convert_to_list(tree).count(element)
