import logging
import vertica_python
from vertica_python import Connection
from vertica_python.vertica import cursor


from research.clickhouse.tools.benchmark import benchmark
from research.vertica.db_utils.settings import connection_info
from research.vertica.db_utils.vertica import Vertica
from research.vertica.run_tests.run_utils import insert_select

from random import randint

logging.basicConfig(level=logging.INFO)


def get_sql() -> Vertica:
    return Vertica(table='score',
                   columns={'id': 'Varchar(20)', 'user_id': 'Varchar(20)', 'movie_id': 'Varchar(20)',
                            'score': 'Integer', })


def get_test_data(doc_count):
    data = [(f'{i}', f'{i}', f'12345', randint(0, 10),) for i in range(doc_count)]
    return data


@benchmark
def insert_select_avg(client: cursor, sql: Vertica, data, transaction: int):
    client.executemany(sql.insert, data)
    client.execute(sql._select_avg(avg_by='score', field='movie_id', field_id='12345', limit=transaction))


@benchmark
def only_select_avg(client: cursor, sql: Vertica, transaction: int):
    client.execute(sql._select_avg(avg_by='score', field='movie_id', field_id='12345', limit=transaction))


def check_fast_insert_n_select_in_full_db(conn: Connection, sql: Vertica, doc_count: int, transaction: int = 1000,
                                          avg: bool = False):
    client = conn.cursor()
    data = get_test_data(doc_count)

    client.executemany(sql.insert, get_test_data(1000000))

    if not avg:
        insert_select(client, sql, data)
    else:
        insert_select_avg(client, sql, data, transaction)
        only_select_avg(client, sql, transaction)


def check_fast_insert_n_select(conn: Connection, sql: Vertica, doc_count: int, transaction: int = 1000,
                               avg: bool = False):
    client = conn.cursor()
    data = get_test_data(doc_count)

    if not avg:
        insert_select(client, sql, data)
    else:
        insert_select_avg(client, sql, data, transaction)
        only_select_avg(client, sql, transaction)


def run():
    logging.root.name = 'RESEARCH: SCORE'
    tests = [10000, 100000]
    transactions = [1000, 5000]
    sql = get_sql()

    with vertica_python.connect(**connection_info) as connection:
        pre_commands = [sql.create_table, sql.truncate]
        for cmd in pre_commands:
            try:
                connection.cursor().execute(cmd)
            except Exception:
                pass

        for t in transactions:
            for i in tests:
                logging.info(f'>>> TEST [SINGLE] INSERT + SELECT DEFAULT: documents count = {i}')
                logging.info(f'>>> TEST [SINGLE] INSERT + SELECT DEFAULT: transaction = {t}')
                check_fast_insert_n_select(connection, sql, i, t)
                logging.info('>>> \n')
                logging.info(f'>>> TEST [SINGLE] INSERT + SELECT AVERAGE: documents count = {i}')
                logging.info(f'>>> TEST [SINGLE] INSERT + SELECT AVERAGE: transaction = {t}')
                check_fast_insert_n_select(connection, sql, i, t, avg=True)
                logging.info('>>> \n')
        for t in transactions:
            for i in tests:
                logging.info(f'>>> TEST [SINGLE] INSERT + SELECT DEFAULT IN FULL DB: documents count = {i}')
                logging.info(f'>>> TEST [SINGLE] INSERT + SELECT DEFAULT IN FULL DB: transaction = {t}')
                check_fast_insert_n_select_in_full_db(connection, sql, i, t)
                logging.info('>>> \n')
                logging.info(f'>>> TEST [SINGLE] INSERT + SELECT AVERAGE IN FULL DB: documents count = {i}')
                logging.info(f'>>> TEST [SINGLE] INSERT + SELECT AVERAGE IN FULL DB: transaction = {t}')
                check_fast_insert_n_select_in_full_db(connection, sql, i, t, avg=True)
                logging.info('>>> \n')


if __name__ == "__main__":
    run()
