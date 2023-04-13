

from clickhouse_driver import Client

client = Client(host='localhost')

print('SHOW DATABASES: ', client.execute('SHOW DATABASES'))
print('DROP TABLE:  ', client.execute('DROP TABLE IF EXISTS movies.views ON CLUSTER company_cluster'))

