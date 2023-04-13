from research.clickhouse.tools.benchmark import benchmark


@benchmark
def insert(client, sql, data):
    client.executemany(sql.insert, data)


@benchmark
def insert_select(client, sql, data):
    client.executemany(sql.insert, data)
    client.execute(sql.select)


@benchmark
def buffer_insert(client, sql, data):
    client.execute(sql.buffer_insert, data)


@benchmark
def select(client, sql):
    client.execute(sql.select)
