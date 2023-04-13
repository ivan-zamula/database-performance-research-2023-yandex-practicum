
from clickhouse_driver import Client
from benchmark import benchmark


client = Client(host='localhost')

data = [
    {'id': f'12345{i}',
     'user_id': f'87654567{i}',
     'movie_id': f'62537462{i}',
     'movie_timestamp': f'98765442{i}',
     'time': f'98765442{i}'}
    for i in range(10)]


@benchmark
def insert_data(data):
    return client.execute(
        """INSERT INTO movies.views (
            id, 
            user_id, 
            movie_id, 
            movie_timestamp, 
            time) VALUES""",
        data)


# for 10 000 = 0.03454999998211861
# for 10 000 000 = 29.771902300068177
print(insert_data(data))

