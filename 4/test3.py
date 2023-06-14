from task03 import my_precious_logger
import pytest


@pytest.mark.parametrize('test_text', ('error: the file is not found',
                                       'ERROR! 404!',
                                       'error: 502, bad gateway'))
def test_logger_error(test_text, capsys):
    my_precious_logger(test_text)
    assert test_text in capsys.readouterr().err


@pytest.mark.parametrize('test_text', ('And we lived',
                                       'Beneath the waves',
                                       'In our yellow submarine'))
def test_logger_out(test_text, capsys):
    my_precious_logger(test_text)
    assert test_text in capsys.readouterr().out