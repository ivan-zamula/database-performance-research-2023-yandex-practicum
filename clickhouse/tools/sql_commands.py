class SQL:

    def __init__(self, db: str, table: str, cluster: str, columns: dict,
                 limit: int = 0, offset: int = 0):
        self.db = db
        self.table = table
        self.cluster = cluster
        self.db_columns = ', '.join([f'{k} {v}' for k, v in columns.items()])
        self.columns = ', '.join(columns.keys())
        self.limit = limit
        self.offset = offset

        # init commands
        self.show = self._show()
        self.truncate = self._truncate()
        self.drop = self._drop()
        self.create_db = self._create_db()
        self.create_table = self._create_table()
        self.insert = self._insert()
        self.select = self._select()
        self.buffer_table = self._buffer_table()
        self.buffer_insert = self._buffer_insert()

    @staticmethod
    def _limit_offset(limit: int, offset: int) -> tuple:
        if limit == 0:
            limit = ''
        else:
            limit = f'ORDER BY id LIMIT {limit}'
        if offset == 0:
            offset = ''
        else:
            offset = f'OFFSET {offset}'
        return limit, offset

    @staticmethod
    def _show():
        return 'SHOW DATABASES'

    def _truncate(self):
        return f'TRUNCATE TABLE IF EXISTS ' \
               f'{self.db}.{self.table} ON CLUSTER {self.cluster}'

    def _drop(self):
        return f'DROP TABLE IF EXISTS ' \
               f'{self.db}.{self.table} ON CLUSTER {self.cluster}'

    def _create_db(self):
        return f'CREATE DATABASE IF NOT EXISTS ' \
               f'{self.db} ON CLUSTER {self.cluster}'

    def _create_table(self):
        return f"""CREATE TABLE {self.db}.{self.table} 
                   ON CLUSTER {self.cluster} (
                        {self.db_columns}
                        ) Engine=MergeTree() ORDER BY id
                 """

    def _buffer_table(self):
        return f"""CREATE TABLE {self.db}.{self.table}_buffer
        AS {self.db}.{self.table} 
        ENGINE = Buffer({self.db}, {self.table} 
        , 1, 10, 100, 10000, 1000000, 10000000, 100000000)"""

    def _insert(self):
        return f"""INSERT INTO {self.db}.{self.table} (
                        {self.columns}
                        ) VALUES"""

    def _buffer_insert(self):
        return f"""INSERT INTO {self.db}.{self.table}_buffer (
                        {self.columns}
                        ) VALUES"""

    def _select(self, limit=0, offset=0):
        pagination = ' '.join(self._limit_offset(limit, offset))
        pagination = '' if len(pagination) == 2 else pagination
        return f'SELECT * FROM {self.db}.{self.table} {pagination}'

    def _select_avg(self, avg_by='', field='', field_id='', limit=1000):
        return f"SELECT AVG({avg_by}) FROM {self.db}.{self.table} " \
               f"WHERE {field} = '{field_id}' LIMIT {limit}"

    def _select_count(self,
                      count_by='',
                      count_by_value='',
                      field='',
                      field_id='',
                      limit=1000):
        return f"SELECT COUNT(*) FROM {self.db}.{self.table} " \
               f"WHERE {field} = '{field_id}' " \
               f"AND {count_by} = {count_by_value}  LIMIT {limit}"

    def select_filtered_double(self,
                               count_by='',
                               count_by_value='',
                               field='',
                               field_id='',
                               limit=1000):
        return f"SELECT * FROM {self.db}.{self.table} " \
               f"WHERE {field} = '{field_id}' " \
               f"AND {count_by} = {count_by_value}  LIMIT {limit}"

    def select_filtered(self,
                        field='',
                        field_id='',
                        limit=1000):
        return f"SELECT * FROM {self.db}.{self.table} " \
               f"WHERE {field} = '{field_id}' " \
               f"LIMIT {limit}"


if __name__ == "__main__":
    sql = SQL(db='movies',
              table='views',
              cluster='company_cluster',
              columns={'id': 'String',
                       'user_id': 'String',
                       'movie_id': 'String',
                       'timestamp_movie': 'Int64',
                       'time': 'Int64'})
    print(sql.select)
