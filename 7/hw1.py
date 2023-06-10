from pathlib import Path
from typing import List, Union, Iterator


def merge_sorted_files(file_list: List[Union[Path, str]]) -> Iterator:
    result_list = []
    for file in file_list:
        with open(file, 'r') as f:
            for line in f.readlines():
                result_list.append(int(line))
    return iter(sorted(result_list))