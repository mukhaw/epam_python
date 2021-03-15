import os
from typing import List

import pytest

from hm_1.tasks.task_02_01 import (
    count_non_ascii_chars,
    count_punctuation_chars,
    get_longest_diverse_words,
    get_most_common_non_ascii_char,
    get_rarest_char,
)


@pytest.mark.parametrize(
    ("file_name", "expected_result"),
    [
        (
            os.path.dirname(__file__) + "/example1.txt",
            [
                "vorgebahnte",
                "Betrachtung",
                "ausführen",
                "verbirgt",
                "vielmehr",
                "bedenkli",
                "Waldgang",
                "Ausflug",
                "hinter",
                "gefaßt",
            ],
        ),
        (
            os.path.dirname(__file__) + "/example2.txt",
            [
                "Gesellschaft",
                "Entwicklung",
                "Frauenfrage",
                "praktische",
                "wenngleich",
                "Welträtsel",
                "Optimismus",
                "überhaupt",
                "Forschung",
                "Probleme",
            ],
        ),
        (
            os.path.dirname(__file__) + "/example3.txt",
            [
                "Gesellschaft",
                "klassenlose",
                "Inzwischen",
                "entwickelt",
                "Außenpoli",
                "geworden",
                "Gebieten",
                "Planeten",
                "soziale",
                "gelöst",
            ],
        ),
        (
            os.path.dirname(__file__) + "/example4.txt",
            [
                "fragenstellende",
                "ununterbrochen",
                "objektiven",
                "Problemen",
                "beitragen",
                "Wißbegier",
                "geändert",
                "Wahrheit",
                "erfahren",
                "Beitrag",
            ],
        ),
        (
            os.path.dirname(__file__) + "/example5.txt",
            ["Mächte", "selbst", "Leser", "sichs", "wird", "sich", "Der", "an"],
        ),
    ],
)
def test_get_longest_diverse_words_works_right(
    file_name: str, expected_result: List[str]
):
    actual_result = get_longest_diverse_words(file_name)

    assert actual_result == expected_result


@pytest.mark.parametrize(
    ("file_name", "expected_result"),
    [
        (os.path.dirname(__file__) + "/example1.txt", "p"),
        (os.path.dirname(__file__) + "/example2.txt", "v"),
        (os.path.dirname(__file__) + "/example3.txt", ","),
        (os.path.dirname(__file__) + "/example4.txt", "-"),
        (os.path.dirname(__file__) + "/example5.txt", "\n"),
    ],
)
def test_get_rarest_char_works_right(file_name: str, expected_result: int):
    actual_result = get_rarest_char(file_name)

    assert actual_result == expected_result


@pytest.mark.parametrize(
    ("file_name", "expected_result"),
    [
        (os.path.dirname(__file__) + "/example1.txt", 6),
        (os.path.dirname(__file__) + "/example2.txt", 8),
        (os.path.dirname(__file__) + "/example3.txt", 3),
        (os.path.dirname(__file__) + "/example4.txt", 11),
        (os.path.dirname(__file__) + "/example5.txt", 1),
    ],
)
def test_count_non_ascii_chars_works_right(file_name: str, expected_result: int):
    actual_result = count_non_ascii_chars(file_name)

    assert actual_result == expected_result


@pytest.mark.parametrize(
    ("file_name", "expected_result"),
    [
        (os.path.dirname(__file__) + "/example1.txt", 7),
        (os.path.dirname(__file__) + "/example2.txt", 12),
        (os.path.dirname(__file__) + "/example3.txt", 5),
        (os.path.dirname(__file__) + "/example4.txt", 13),
        (os.path.dirname(__file__) + "/example5.txt", 0),
    ],
)
def test_count_punctuation_chars_works_right(file_name: str, expected_result: int):
    actual_result = count_punctuation_chars(file_name)

    assert actual_result == expected_result


@pytest.mark.parametrize(
    ("file_name", "expected_result"),
    [
        (os.path.dirname(__file__) + "/example1.txt", "ü"),
        (os.path.dirname(__file__) + "/example2.txt", "ß"),
        (os.path.dirname(__file__) + "/example3.txt", "ß"),
        (os.path.dirname(__file__) + "/example4.txt", "ß"),
        (os.path.dirname(__file__) + "/example5.txt", "ä"),
    ],
)
def test_get_most_common_non_ascii_char_works_right(
    file_name: str, expected_result: int
):
    actual_result = get_most_common_non_ascii_char(file_name)

    assert actual_result == expected_result
