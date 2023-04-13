import logging
import time


def benchmark(func):
    def wrapper(*args, **kwargs):
        t = time.perf_counter()
        res = func(*args, **kwargs)
        logging.warning(f'{func.__name__}, {time.perf_counter() - t}')
        return res
    return wrapper
