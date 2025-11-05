from typing import Callable


def cache(func: Callable) -> Callable:
    cache_dict = dict()

    def wrapper(*args) -> int | list:
        nonlocal cache_dict
        if args not in cache_dict:
            cache_dict[args] = func(*args)
            print("Calculating new result")
            return cache_dict[args]
        else:
            print("Getting from cache")
            return cache_dict[args]
    return wrapper
