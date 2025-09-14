import sqlite3
from alx-airbnb-database.database-script-0x02.seed import connect_to_prodev

class ExecuteQuery:
    """custom context manager for query with parameter"""
    def __init__(self, query, params=None):
        self.query = query
        self.params = params
        self.conn = None
        self.cursor = None
        self.result = None

    def __enter__(self):
        self.conn = connect_to_prodev()
        self.cursor = self.conn.cursor()

        if self.params:
            self.cursor.execute(self.query, self.params)
        else:
            self.cursor.execute(self.query)

        self.result = self.cursor.fetchall()
        return self.result
    def __exit__(self, exc_type, exc_value, traceback):
        if self.cursor:
            self.cursor.close()
        if self.conn:
            if exc_type is not None:
                self.conn.rollback()
            else:
                self.conn.close()
        return False


if __name__ == "__main__":
    query = "SELECT * FROM user_data WHERE age > %s"
    param = (25,)
    with ExecuteQuery(query, param) as result:
        print(f"Users older than 25: {result}")
