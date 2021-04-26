"""
Given two strings. Return if they are equal when both are typed into
empty text editors. # means a backspace character.
Note that after backspacing an empty text, the text will continue empty.
Examples:
    Input: s = "ab#c", t = "ad#c"
    Output: True
    # Both s and t become "ac".
    Input: s = "a##c", t = "#a#c"
    Output: True
    Explanation: Both s and t become "c".
    Input: a = "a#c", t = "b"
    Output: False
    Explanation: s becomes "c" while t becomes "b".
"""


def delete_backspace(s: str):
    for i in s:
        s = s.replace(i + "#", "")
    return s.replace("#", "")


def backspace_compare(first: str, second: str):
    """

    >>> backspace_compare("ab#c", "ad#c")
    True
    >>> backspace_compare("a##c", "#a#c")
    True
    >>> backspace_compare("a#c", "c")
    True
    >>> backspace_compare("ab#c", "ad#ghc")
    False
    >>> backspace_compare("a#c", "b")
    False
    """
    return delete_backspace(first) == delete_backspace(second)


if __name__ == "__main__":
    import doctest

    doctest.testmod()
