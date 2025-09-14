#!/usr/bin/python3
import sqlite3
from alx-airbnb-database.database-script-0x02.seed import connect_to_prodev

class DatabaseConnection(object):
    def __init__(self, file_name, method):
        self.file_obj = 
        self.conn = None
        self.cursor = None

    def __enter__(self):
        try:
            self.conn = connect_to_prodev
            self.cursor = self.conn.cursor()
            return self.cursor
        except Exception as e:
            print(f"failed to connect to database: {e}")

    def __exit__(self, type, value, traceback):
        try:
            if self.conn:
                if type is None:
                    self.conn.commit()
                else:
                    self.conn.rollback()
                self.cursor.close()
                self.conn.close()
        except Exception as e:
            print(f"Error closing database connection: {e}")

if __name__ == "__main__":
    with DatabaseConnection() as cursor:
        cursor.execute("SELECT * FROM users;")
        rows = cursor.fetchall()
        print(f"Query Results: {rows}")
