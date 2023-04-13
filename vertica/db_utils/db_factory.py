import vertica_python
from vertica_python.vertica import cursor

from settings import connection_info
from research.clickhouse.tools.benchmark import benchmark


def create_table() -> None:
    cursor.execute("""  
    CREATE TABLE views (
        id IDENTITY,
        user_id INTEGER NOT NULL,
        movie_id VARCHAR(256) NOT NULL,
        viewed_frame INTEGER NOT NULL,
        timestamp_movie INTEGER NOT NULL,
        time INTEGER NOT NULL
    );
    """)


def drop_table() -> None:
    cursor.execute("""  
    DROP TABLE views;
    """)


@benchmark
def insert_n_rows(n: int) -> None:
    values = [generate_data(i) for i in range(n)]
    try:
        cursor.executemany(
            'INSERT INTO views (user_id, movie_id, viewed_frame, timestamp_movie, time) VALUES (?,?,?,?,?)',
            values
        )
    except Exception as e:
        raise e


def generate_data(i) -> tuple:
    return (f'12345{i}',
            f'87654567{i}',
            f'62537462{i}',
            1234567874 + i,
            98765442 + i)


@benchmark
def select() -> None:
    cursor.execute("""
        SELECT * FROM views;
    """)
    # for row in cursor.iterate():
        # print(row)


@benchmark
def insert_butch_by_n_rows(n: int) -> None:
    for _ in range(9):
        insert_n_rows(10_000)


def insert_butches():
    with vertica_python.connect(**connection_info) as connection:
        cursor = connection.cursor()
        # drop_table()
        # create_table()
        for i in range(1, 11):
            print(f"Run {(i-1) * 100000} - {i * 100000}")
            insert_butch_by_n_rows(10_000)
            select()
            print("___")


