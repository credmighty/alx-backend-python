import sqlite3 
import functools


def with_db_connection(func):
    """ your code goes here""" 
    def wrapper_db_connection(*args, **kwargs):
        try:
            conn = sqlite3.connect('users.db')
            result = func(conn, *args, **kwargs)
            return result
        finally:
            if conn:
                conn.close()
    return wrapper_db_connection

@with_db_connection 
def get_user_by_id(conn, user_id):
    cursor = conn.cursor() 
    cursor.execute("SELECT * FROM users WHERE id = ?", (user_id,)) 
    return cursor.fetchone() 


#### Fetch user by ID with automatic connection handling 

user = get_user_by_id(user_id=1)
print(user)
