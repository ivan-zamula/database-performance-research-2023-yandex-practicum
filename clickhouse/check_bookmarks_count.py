import os
import logging

from clickhouse_driver import Client
from tools.benchmark import benchmark
from tools.sql_commands import SQL
from random import randint

logging.basicConfig(level=logging.INFO)


@benchmark
def insert(client, sql, data):
    client.execute(sql.insert, data)


@benchmark
def insert_select(client, sql, data):
    client.execute(sql.insert, data)
    client.execute(sql.select)


@benchmark
def insert_select_count(client, sql, data, transaction):
    client.execute(sql.insert, data)
    client.execute(sql.select_filtered(field='user_id',
                                       field_id='12345',
                                       limit=transaction))


@benchmark
def only_select_count(client, sql, transaction):
    client.execute(sql.select_filtered(field='user_id',
                                       field_id='12345',
                                       limit=transaction))


@benchmark
def buffer_insert(client, sql, data):
    client.execute(sql.buffer_insert, data)


@benchmark
def select(client, sql):
    client.execute(sql.select)


def get_sql():
    return SQL(db='movies',
               table='score',
               cluster='company_cluster',
               columns={'id': 'String',
                        'user_id': 'String',
                        'movie_id': 'String',
                        })


def get_test_data(doc_count):
    return [
        {'id': f'{i}',
         'user_id': f'12345',
         'movie_id': f'{i}',
         }
        for i in range(doc_count)]


def check_fast_insert_n_select_in_full_db(
        doc_count: int,
        host: str = 'localhost',
        transaction: int = 1000,
        avg: bool = False):
    client = Client(host=host)
    data = get_test_data(doc_count)
    sql = get_sql()

    pre_commands = [sql.create_db, sql.create_table, sql.truncate]
    for cmd in pre_commands:
        try:
            client.execute(cmd)
        except Exception:
            pass
    client.execute(sql.insert, get_test_data(1000000))
    if not avg:
        insert_select(client, sql, data)
    else:
        insert_select_count(client, sql, data, transaction)
        only_select_count(client, sql, transaction)


def check_fast_insert_n_select(
        doc_count: int,
        host: str = 'localhost',
        transaction: int = 1000,
        avg: bool = False):
    client = Client(host=host)
    data = get_test_data(doc_count)
    sql = get_sql()

    pre_commands = [sql.create_db, sql.create_table, sql.truncate]
    for cmd in pre_commands:
        try:
            client.execute(cmd)
        except Exception:
            pass
    if not avg:
        insert_select(client, sql, data)
    else:
        insert_select_count(client, sql, data, transaction)
        only_select_count(client, sql, transaction)


def run():
    logging.root.name = 'RESEARCH: BOOKMARKS'
    tests = [10000, 100000]
    transactions = [1000, 5000]
    host = os.environ.get('host', 'localhost')
    for t in transactions:
        for i in tests:
            logging.info(f'>>> TEST [SINGLE] INSERT + SELECT DEFAULT: documents count = {i}')
            logging.info(f'>>> TEST [SINGLE] INSERT + SELECT DEFAULT: transaction = {t}')
            check_fast_insert_n_select(i, host, t)
            logging.info('>>> \n')
            logging.info(f'>>> TEST [SINGLE] INSERT + SELECT COUNT: documents count = {i}')
            logging.info(f'>>> TEST [SINGLE] INSERT + SELECT COUNT: transaction = {t}')
            check_fast_insert_n_select(i, host, t, avg=True)
            logging.info('>>> \n')
    for t in transactions:
        for i in tests:
            logging.info(f'>>> TEST [SINGLE] INSERT + SELECT DEFAULT IN FULL DB: documents count = {i}')
            logging.info(f'>>> TEST [SINGLE] INSERT + SELECT DEFAULT IN FULL DB: transaction = {t}')
            check_fast_insert_n_select_in_full_db(i, host, t)
            logging.info('>>> \n')
            logging.info(f'>>> TEST [SINGLE] INSERT + SELECT COUNT IN FULL DB: documents count = {i}')
            logging.info(f'>>> TEST [SINGLE] INSERT + SELECT COUNT IN FULL DB: transaction = {t}')
            check_fast_insert_n_select_in_full_db(i, host, t, avg=True)
            logging.info('>>> \n')


if __name__ == "__main__":
    run()
