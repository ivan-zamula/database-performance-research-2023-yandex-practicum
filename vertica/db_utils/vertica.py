class Vertica:
    def __init__(self, table: str, columns: dict, limit: int = 0):
        self.table = table
        self.db_columns = ', '.join([f'{k} {v}' for k, v in columns.items()])
        self.columns_count = len(columns.keys())
        self.columns = ', '.join(columns.keys())
        self.limit = limit

        # init commands
        self.create_table = self._create_table()
        self.truncate = self._truncate()
        self.drop_table = self._drop_table()
        self.insert = self._insert()
        self.select = self._select()

    def _create_table(self) -> str:
        return f"""CREATE TABLE {self.table} ({self.db_columns}) ORDER BY id;"""

    def _truncate(self) -> str:
        return f'TRUNCATE TABLE IF EXISTS {self.table};'

    def _drop_table(self) -> str:
        return f"""DROP TABLE {self.table};"""

    def _insert(self) -> str:
        values = '('
        for c in range(self.columns_count):
            values += '?'
            if c != self.columns_count - 1:
                values += ', '
        values += ')'
        query = f"""INSERT INTO {self.table} ({self.columns}) VALUES {values};"""
        # query = f"""INSERT INTO {self.table} VALUES {values};"""
        return query

    def _select(self) -> str:
        return f'SELECT * FROM {self.table};'

    def _select_avg(self, avg_by='', field='', field_id='', limit=1000) -> str:
        return f"SELECT AVG({avg_by}) FROM {self.table} " \
               f"WHERE {field} = '{field_id}' LIMIT {limit};"

    def _select_count(self, count_by='', count_by_value='', field='', field_id='', limit=1000) -> str:
        return f"SELECT COUNT(*) FROM {self.table} " \
               f"WHERE {field} = '{field_id}' " \
               f"AND {count_by} = {count_by_value}  LIMIT {limit};"

    def select_filtered_double(self, count_by='', count_by_value='', field='', field_id='', limit=1000) -> str:
        return f"SELECT * FROM {self.table} " \
               f"WHERE {field} = '{field_id}' " \
               f"AND {count_by} = {count_by_value}  LIMIT {limit};"

    def select_filtered(self, field='', field_id='', limit=1000) -> str:
        return f"SELECT * FROM {self.table} " \
               f"WHERE {field} = '{field_id}' " \
               f"LIMIT {limit};"
