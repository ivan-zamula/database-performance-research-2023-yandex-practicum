import os
import logging

from clickhouse_driver import Client
from tools.benchmark import benchmark
from tools.sql_commands import SQL

logging.basicConfig(level=logging.INFO)
logging.root.name = 'RESEARCH'


@benchmark
def insert(client, sql, data):
    client.execute(sql.insert, data)


@benchmark
def buffer_insert(client, sql, data):
    client.execute(sql.buffer_insert, data)


@benchmark
def select(client, sql):
    client.execute(sql.select)


def get_sql():
    return SQL(db='movies',
               table='views',
               cluster='company_cluster',
               columns={'id': 'String',
                        'user_id': 'String',
                        'movie_id': 'String',
                        'timestamp_movie': 'Int64',
                        'time': 'Int64'})


def get_test_data(doc_count):
    return [
        {'id': f'12345{i}',
         'user_id': f'87654567{i}',
         'movie_id': f'62537462{i}',
         'timestamp_movie': 1234567874 + i,
         'time': 98765442 + i}
        for i in range(doc_count)]


def check_insert_time_batches_in_full_db(
        doc_count: int,
        host: str = 'localhost',
        transaction: int = 1000):
    client = Client(host=host)
    data = get_test_data(doc_count)
    sql = get_sql()

    pre_commands = [sql.create_db, sql.create_table, sql.truncate]
    for cmd in pre_commands:
        try:
            client.execute(cmd)
        except Exception:
            pass
    client.execute(sql.insert, get_test_data(10000000))
    batches = prepare_batches(data, transaction)
    insert_batches(client, sql, batches)


def check_insert_time_batches(
        doc_count: int,
        host: str = 'localhost',
        transaction: int = 1000):
    client = Client(host=host)
    data = get_test_data(doc_count)
    sql = get_sql()

    pre_commands = [sql.create_db, sql.create_table, sql.truncate]
    for cmd in pre_commands:
        try:
            client.execute(cmd)
        except Exception:
            pass
    batches = prepare_batches(data, transaction)
    insert_batches(client, sql, batches)
    # select_batches(client, sql, transaction)


def prepare_batches(data, transaction=1000):
    buffer, result = [], []
    for i, msg in enumerate(data, start=1):
        buffer.append(msg)
        if i % transaction == 0:
            # client.execute(sql.insert, data)
            result.append(buffer.copy())
            buffer.clear()

    if buffer:
        # client.execute(sql.buffer_insert, data)
        result.append(buffer.copy())
        buffer.clear()
    return result


@benchmark
def insert_batches(client, sql, data):
    for i in data:
        client.execute(sql.insert, i)


@benchmark
def select_batches(client, sql, transaction=1000):

    buffer = []
    i = 0
    while True:
        # print(f'DEBUG: {sql._select(limit=transaction, offset=i * transaction)}')
        msg = client.execute(sql._select(limit=transaction,
                                         offset=i * transaction))
        buffer.append(msg)
        if len(msg) < transaction:
            break
        i += 1


def run():
    tests = [100000, 1000000, 10000000]
    transactions = [1000, 5000, 10000, 100000]
    host = os.environ.get('host', 'localhost')
    for t in transactions:
        for i in tests:
            logging.info(f'>>> TEST [BATCH] INSERT DEFAULT: documents count = {i}')
            logging.info(f'>>> TEST [BATCH] INSERT DEFAULT: transaction = {t}')
            check_insert_time_batches(i, host, t)
            logging.info('>>> \n')
    for t in transactions:
        for i in tests:
            logging.info(f'>>> TEST [BATCH] INSERT FULL DB: documents count = {i}')
            logging.info(f'>>> TEST [BATCH] INSERT FULL DB: transaction = {t}')
            check_insert_time_batches_in_full_db(i, host, t)
            logging.info('>>> \n')


if __name__ == "__main__":
    run()
