

from clickhouse_driver import Client

client = Client(host='localhost')

print(client.execute('CREATE DATABASE IF NOT EXISTS movies ON CLUSTER company_cluster'))
