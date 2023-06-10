class FileValueError(Exception):
    pass


class KeyValueStorage:
    """the class wraps a file and provide values as attributes"""

    def __setitem__(self, key, item):
        self.__dict__[key] = item

    def __getitem__(self, key):
        return self.__dict__[key]

    def __init__(self, path: str):
        with open(path, 'r') as file:
            for line in file:
                try:
                    int(line.split('=')[0])
                    raise FileValueError('Key can not be an integer.')
                except ValueError:
                    key = line.split('=')[0]
                    try:
                        value = int(line.split('=')[1])
                    except ValueError:
                        value = line.split('=')[1].strip()
                    if key not in dir(self):
                        setattr(self, key, value)
                        self[key] = value
