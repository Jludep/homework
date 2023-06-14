import task05


def test_fizzbuzz(n: int = 25):
    value = task05.fizzbuzz(n)
    i = 1
    str = ""
    while i <= 25:
        str = next(value)
        i += 1
    assert str == "fizz buzz"