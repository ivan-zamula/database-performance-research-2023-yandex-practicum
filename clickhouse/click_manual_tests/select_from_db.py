

from clickhouse_driver import Client
from benchmark import benchmark


client = Client(host='localhost')


@benchmark
def get_data(client):
    return client.execute('SELECT * FROM movies.views')


print(get_data(client))

