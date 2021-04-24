"""
Given a dictionary (tree), that can contains multiple nested structures.
Write a function, that takes element and finds the number of occurrences
of this element in the tree.
Tree can only contains basic structures like:
    str, list, tuple, dict, set, int, bool
"""
import string
from typing import Any


def find_occurrences(tree: dict, element: Any) -> int:
    text_without_punctuation = str(tree).translate(
        str.maketrans("", "", string.punctuation)
    )
    list_of_dict_elements = text_without_punctuation.split()
    return list_of_dict_elements.count(element)
