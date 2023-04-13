import os
import logging

from clickhouse_driver import Client
from tools.benchmark import benchmark
from tools.sql_commands import SQL


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


def check_insert_n_select_time(doc_count: int,
                               host: str = 'localhost'):
    client = Client(host=host)
    data = get_test_data(doc_count)
    sql = get_sql()

    pre_commands = [sql.create_db, sql.create_table, sql.truncate]
    for cmd in pre_commands:
        try:
            client.execute(cmd)
        except Exception:
            pass
    insert(client, sql, data)
    select(client, sql)


def check_insert_n_select_time_buffer(doc_count: int,
                                      host: str = 'localhost'):
    client = Client(host=host)
    data = get_test_data(doc_count)
    sql = get_sql()
    pre_commands = [sql.create_db, sql.create_table,
                    sql.buffer_table, sql.truncate]
    for cmd in pre_commands:
        try:
            client.execute(cmd)
        except Exception:
            pass
    buffer_insert(client, sql, data)
    select(client, sql)


def run():
    tests = [10000, 100000, 1000000, 10000000]
    host = os.environ.get('host', 'localhost')
    for i in tests:
        logging.info(f'>>> TEST [SINGLE] INSERT DEFAULT: documents count = {i}')
        check_insert_n_select_time(i, host)
        logging.info('>>> \n')
    for i in tests:
        logging.info(f'>>> TEST [SINGLE] INSERT BUFFERED: documents count = {i}')
        check_insert_n_select_time(i, host)
        logging.info('>>> \n')


if __name__ == "__main__":
    run()
