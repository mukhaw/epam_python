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


def get_data(file_path: str) -> str:
    data = ""
    with open(file_path, encoding="unicode_escape") as f:
        for line in f:
            data += line
    return data


def get_longest_diverse_words(file_path: str) -> List[str]:
    data = {}
    result = []
    text_without_punctuation = get_data(file_path).translate(
        str.maketrans("", "", string.punctuation)
    )
    words = text_without_punctuation.split()
    for i in words:
        data[i] = len(set(i.lower()))
    k = len(data) if len(data) <= 10 else 10
    result = sorted(data.items(), key=lambda x: x[1], reverse=True)
    list_10_longest_words = []
    for i in sorted(result[0:k], key=lambda x: len(x[0]), reverse=True):
        list_10_longest_words.append(i[0])
    return list_10_longest_words


def get_rarest_char(file_path: str) -> str:
    data = {}
    text = get_data(file_path)
    symbols = set(text.lower())
    for i in symbols:
        data[i] = text.lower().count(i)
    sorted_data_by_rarest = sorted(data.items(), key=lambda k: k[0])
    return sorted(sorted_data_by_rarest, key=lambda k: k[1])[0][0]


def count_punctuation_chars(file_path: str) -> int:
    text = get_data(file_path)
    counts_punctuation_chars = []
    for i in string.punctuation:
        counts_punctuation_chars.append(text.count(i))
    return sum(counts_punctuation_chars)


def count_non_ascii_chars(file_path: str) -> int:
    text = get_data(file_path)
    count = 0
    for i in text.lower():
        if ord(i) > 128:
            count += 1
    return count


def get_most_common_non_ascii_char(file_path: str) -> str:
    text = get_data(file_path)
    non_ascii_symbols = []
    for i in text.lower():
        if ord(i) > 128:
            non_ascii_symbols.append(i)
    return Counter(non_ascii_symbols).most_common(1)[0][0]
