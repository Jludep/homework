from hw3 import universal_file_counter
import pytest
import os
from pathlib import Path


@pytest.fixture()
def file_list():
    for i in range(1, 4):
        with open(f'5_{i}.txt', 'w+') as f:
            f.writelines([f'{1*i}\n', f'{100*i}\n', f'{10*i}\n'])
    yield ['5_1.txt', '5_2.txt', '5_3.txt']
    for j in range(1, 4):
        os.remove(f"5_{j}.txt")


def test_universal_file_counter_without_tokenizer(file_list):
    assert universal_file_counter(Path('.'), 'txt') == 9


def test_universal_file_counter_with_tokenizer(file_list):
    assert universal_file_counter(Path('.'), 'txt', str.split) == 9
