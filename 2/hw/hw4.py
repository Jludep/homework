"""
Write a function that accepts another function as an argument. Then it
should return such a function, so the every call to initial one
should be cached.


def func(a, b):
    return (a ** b) ** 2


cache_func = cache(func)

some = 100, 200

val_1 = cache_func(*some)
val_2 = cache_func(*some)

assert val_1 is val_2

"""
from collections import Callable

CACHE = {}

def cache(func: Callable) -> Callable:
    def wrapper(*args, **kwargs):
        result = func(*args, **kwargs)
        CACHE[f'{len(CACHE)} call of initial one'] = result
        return result
    return wrapper

@cache
def func(a, b):
    return (a**b)**2
""" Each time the func function is called, the wrapper wrapper first checks whether there is already a saved 
result in the CACHE dictionary. If the result has already been calculated and saved, the function returns this result. 
If the result has not yet been stored in the cache, the func function calculates the result, stores it in the cache and 
then returns it. The key of the CACHE dictionary is a string containing the function call number and a text description
 for debugging convenience.
 """