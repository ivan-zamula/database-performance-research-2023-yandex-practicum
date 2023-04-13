

from clickhouse_driver import Client

client = Client(host='localhost')


def create_cluster_table(client) -> None:
    return client.execute(
            """CREATE TABLE movies.views ON CLUSTER company_cluster (
                id String,
                user_id String,
                movie_id String,
                timestamp_movie Int64,
                time Int64
                ) Engine=MergeTree() ORDER BY id
         """)


print(create_cluster_table(client))
