from hm_1.tasks.task_04_04 import fizzbuzz


def test_fizzbazz():
    """

    >>> fizzbuzz(5)
    ['1', '2', 'fizz', '4', 'buzz']
    >>> fizzbuzz(16)
    ['1', '2', 'fizz', '4', 'buzz', 'fizz', '7', '8', 'fizz', 'buzz', '11', 'fizz', '13', '14', 'FizzBuzz', '16']
    >>> fizzbuzz(-1)
    []
    """


if __name__ == "__main__":
    import doctest

    doctest.testmod()
