"""
Write a function that merges integer from sorted files and returns an iterator
file1.txt:
1
3
5
file2.txt:
2
4
6
list(merge_sorted_files(["file1.txt", "file2.txt"]))
[1, 2, 3, 4, 5, 6]
"""
from pathlib import Path
from typing import Iterator, List, Union


def read_data_from_file(file_name: str) -> List:
    with open(file_name) as f:
        return [int(i.rstrip("\n")) for i in f.readlines()]


def merge_sorted_files(file_list: List[Union[Path, str]]) -> Iterator:
    left = read_data_from_file(file_list[1])
    right = read_data_from_file(file_list[0])
    return sorted(left + right)
