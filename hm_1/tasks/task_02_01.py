"""
Given a file containing text. Complete using only default collections:
    1) Find 10 longest words consisting from largest amount of unique symbols
    2) Find rarest symbol for document
    3) Count every punctuation char
    4) Count every non ascii char
    5) Find most common non ascii char for document
"""
import string
from collections import Counter
from typing import List


def get_text(file_path: str) -> str:
    data = ""
    with open(file_path, encoding="unicode_escape") as f:
        for line in f:
            data += line
    return data


def get_longest_diverse_words(file_path: str) -> List[str]:
    data = {}
    text_without_punctuation = get_text(file_path).translate(
        str.maketrans("", "", string.punctuation)
    )
    words = text_without_punctuation.split()
    for i in words:
        data[i] = len(set(i.lower()))
    result = sorted(data.items(), key=lambda x: x[1], reverse=True)
    list_10_longest_words = []
    for i in sorted(result[0:10], key=lambda x: len(x[0]), reverse=True):
        list_10_longest_words.append(i[0])
    return list_10_longest_words


def get_rarest_char(file_path: str) -> str:
    data = Counter(get_text(file_path).lower())
    key, _ = min(data.items(), key=lambda x: x[1])
    return key


def count_punctuation_chars(file_path: str) -> int:
    text = get_text(file_path)
    text_without_punctuation = text.translate(str.maketrans("", "", string.punctuation))
    return len(text) - len(text_without_punctuation)


def count_non_ascii_chars(file_path: str) -> int:
    text = get_text(file_path)
    text_without_non_ascii_chars = text.encode("ascii", "ignore").decode()
    return len(text) - len(text_without_non_ascii_chars)


def get_most_common_non_ascii_char(file_path: str) -> str:
    text = get_text(file_path)
    text_without_non_ascii_chars = text.encode("ascii", "ignore").decode()
    non_ascii_chars = ""
    for i in text:
        if i not in text_without_non_ascii_chars:
            non_ascii_chars += i
    data = Counter(non_ascii_chars)
    key, _ = max(data.items(), key=lambda x: x[1])
    return key
