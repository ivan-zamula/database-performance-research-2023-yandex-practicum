
from clickhouse_driver import Client
from tools.benchmark import benchmark
from tools.sql_commands import SQL


def check_selection_time():
    client = Client(host='localhost')
    sql = SQL(db='movies',
              table='views',
              cluster='company_cluster',
              columns={'id': 'String',
                       'user_id': 'String',
                       'movie_id': 'String',
                       'timestamp_movie': 'Int64',
                       'time': 'Int64'})

    @benchmark
    def select():
        client.execute(sql.select)

    select()


if __name__ == "__main__":
    check_selection_time()
