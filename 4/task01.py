from os import path


def read_magic_number(location: str) -> bool:
    if path.exists(location):
        with open(location, 'r') as f:
            try:
                fst_line = float(f.readline())
                return 1. <= fst_line < 3.
            except Exception:
                raise ValueError