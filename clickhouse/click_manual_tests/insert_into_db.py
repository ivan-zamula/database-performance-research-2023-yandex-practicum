

from clickhouse_driver import Client

client = Client(host='localhost')

data = {'id': '12345',
        'user_id': '87654567',
        'movie_id': '62537462',
        'movie_timestamp': '1234567874',
        'time': '98765442'}

a = client.execute(
    """INSERT INTO movies.views (
        id, 
        user_id, 
        movie_id, 
        movie_timestamp, 
        time) VALUES""",
    [data]
    )

print(a)
