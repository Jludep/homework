from pathlib import Path
from typing import Optional, Callable


def universal_file_counter(dir_path: Path, file_extension: str, tokenizer: Optional[Callable] = None) -> int:
    counter = 0
    for file in dir_path.glob(f'*.{file_extension}'):
        with file.open('r') as f:
            if tokenizer is None:
                counter += len(f.readlines())
            else:
                counter += len(tokenizer('\n'.join(f.readlines())))
    return counter
