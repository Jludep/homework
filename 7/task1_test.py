import os
from task1 import KeyValueStorage, FileValueError
import pytest


@pytest.fixture()
def file_wrapper():
    with open('4.txt', 'w+') as f:
        f.writelines(['name=kek\n', 'last_name=top\n', 'power=9001\n',
                      'song=shadilay\n', '__doc__=the class do something\n'])
    yield KeyValueStorage('4.txt')
    os.remove('4.txt')


def test_access_the_attributes(file_wrapper):
    assert file_wrapper['name'] == 'kek'
    assert file_wrapper['song'] == 'shadilay'


def test_type_of_num_in_file(file_wrapper):
    assert isinstance(file_wrapper['power'], int)


def test_priority(file_wrapper):
    assert file_wrapper.__doc__ == 'the class wraps a file and provide values as attributes'


def test_value_error():
    with open('4.txt', 'w+') as f:
        f.writelines(['name=kek\n', 'last_name=top\n', '1=something'])
    with pytest.raises(FileValueError):
        KeyValueStorage('4.txt')
    os.remove('4.txt')
