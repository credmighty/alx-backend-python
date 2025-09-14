import sqlite3 
import functools
from datetime import datetime


def with_db_connection(func):
    """ your code goes here"""
    @functools.wraps(func)
    def wrapper_db_connection(*args, **kwargs):
        conn = sqlite3.connect('users.db')
        time_stamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        try:
            result = func(conn, *args, **kwargs)
            print(f"[{time_stamp} Function '{func.__name__}' executed successfully]")
            return result
        finally:
            if conn:
                conn.close()
                print(f"[{time_stamp}] Database connection closed.")
    return wrapper_db_connection

@with_db_connection 
def get_user_by_id(conn, user_id):
    cursor = conn.cursor() 
    cursor.execute("SELECT * FROM users WHERE id = ?", (user_id,)) 
    return cursor.fetchone() 


#### Fetch user by ID with automatic connection handling 

user = get_user_by_id(user_id=1)
print(user)
