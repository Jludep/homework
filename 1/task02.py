"""
Given a cell with "it's a fib sequence" from slideshow,
    please write function "check_fib", which accepts a Sequence of integers, and
    returns if the given sequence is a Fibonacci sequence

We guarantee, that the given sequence contain >= 0 integers inside.

"""
from collections import Sequence


def check_fibonacci(data: Sequence[int]) -> bool:
    if len(data) == 0:  # in case if sequence is empty
        return False

    elif len(data) == 1:  # in case if sequence consists only one element
        if data[0] == 0:
            return True
        else:
            return False

    elif len(data) == 2:  # in case if sequence consists of two elements
        if data[0] == 0 and data[1] == 1:
            return True
        else:
            return False

    else:  # in cases if length of sequence >=3



        for i in range(len(data)):

            if data[i] == data[-2]:
                return True

            if data[i] + data[i + 1] == data[i + 2]:
                continue
            else:
                return False
