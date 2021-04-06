from typing import List


def fizz_bass_element(number: int):
    if number % 15 == 0:
        return "FizzBuzz"
    elif number % 3 == 0:
        return "fizz"
    elif number % 5 == 0:
        return "buzz"
    else:
        return str(number)


def fizzbuzz(n: int) -> List[str]:
    return [fizz_bass_element(i) for i in range(1, n + 1)]
