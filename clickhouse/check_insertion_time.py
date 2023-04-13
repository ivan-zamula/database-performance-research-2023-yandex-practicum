
from clickhouse_driver import Client
from tools.benchmark import benchmark
from tools.sql_commands import SQL


def check_insertion_time(doc_count: int):
    client = Client(host='localhost')
    sql = SQL(db='movies',
              table='views',
              cluster='company_cluster',
              columns={'id': 'String',
                       'user_id': 'String',
                       'movie_id': 'String',
                       'timestamp_movie': 'Int64',
                       'time': 'Int64'})
    data = [
        {'id': f'12345{i}',
         'user_id': f'87654567{i}',
         'movie_id': f'62537462{i}',
         'timestamp_movie': 1234567874 + i,
         'time': 98765442 + i}
        for i in range(doc_count)]

    @benchmark
    def insert():
        client.execute(sql.insert, data)

    pre_commands = [sql.create_db, sql.create_table, sql.truncate]
    for cmd in pre_commands:
        try:
            client.execute(cmd)
        except Exception:
            pass
    insert()


if __name__ == "__main__":
    check_insertion_time(1000000)
