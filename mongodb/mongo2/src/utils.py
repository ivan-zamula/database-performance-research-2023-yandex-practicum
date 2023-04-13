import sys
import time
from random import randint

from pymongo import InsertOne

from config import settings


def benchmark(func):
    def wrapper(*args, **kwargs):
        t = time.perf_counter()
        func(*args, **kwargs)
        sys.stdout.write(f'{func.__name__} {time.perf_counter() - t}\n')

    return wrapper


def get_test_data(concern_data: bool = False):
    for i in range(1, settings.recs_num, settings.batch_size):
        test_data = []
        for j in range(settings.batch_size):
            data = {
                'id': f'{i + j}',
                'user_id': f'12345',
                'movie_id': f'{i + j}',
                'score': randint(1, 10),
            }
            if concern_data:
                test_data.append(InsertOne(data))
            else:
                test_data.append(data)
        yield test_data