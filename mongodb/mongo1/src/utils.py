import sys
import time

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
            data = {'id': f'12345{i + j}',
                    'user_id': f'87654567{i + j}',
                    'movie_id': f'62537462{i + j}',
                    'timestamp_movie': 1234567874 + i + j,
                    'time': 98765442 + i + j}
            if concern_data:
                test_data.append(InsertOne(data))
            else:
                test_data.append(data)
        yield test_data
