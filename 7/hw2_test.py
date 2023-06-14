from hw2 import suppressor


def test_suppressor():
    with suppressor(IndexError):
        assert [][2] is None
