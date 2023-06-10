from contextlib import contextmanager


@contextmanager
def suppressor(exception):
    try:
        yield
    except exception:
        pass


class Suppressor:
    def __init__(self, exception):
        self.exception = exception

    def __enter__(self):
        return self

    def __exit__(self, exc_type, exc_value, traceback):
        if exc_type == self.exception:
            return True

