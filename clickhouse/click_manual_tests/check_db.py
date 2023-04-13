

from clickhouse_driver import Client

client = Client(host='localhost')

print('SHOW DATABASES: ', client.execute('SHOW DATABASES'))
print('default.views:  ', client.execute('SELECT * FROM default.views'))
print('movies.views:   ', client.execute('SELECT * FROM movies.views'))
