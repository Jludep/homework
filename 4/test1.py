import os
from task01 import read_magic_number
import pytest

path = 'my_test_file.txt'


def fill_the_file(text, file_address):
    with open(file_address, 'w') as f:
        f.write(text)


@pytest.mark.parametrize('file_string', ['1\nhello\nthat"s a test',
                                         '1.5\nblalalal',
                                         '2.999999\nOH MY GOD!'])
def test_read_magic_number_positive(file_string):
    fill_the_file(file_string, path)
    assert read_magic_number(path) is True


@pytest.mark.parametrize('file_string', ['0\nhello\nDinoLand',
                                         '5\nabobba',
                                         '3\nburning man'])
def test_read_magic_number_negative(file_string):
    fill_the_file(file_string, path)
    assert read_magic_number(path) is False


def test_read_magic_number_error():
    fill_the_file('number one\nTAYLER DERTON"', path)
    with pytest.raises(ValueError):
        read_magic_number(path)


def test_self_cleaning():
    os.remove(path)
    assert not os.path.exists(path)