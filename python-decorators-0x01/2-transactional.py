import sqlite3 
import functools
from 1-with_db_connection import with_db_connection

"""your code goes here"""
def transactional(func):
    @functools.wraps(func)
    def wrapper_transactional(*args, **kwargs):
        conn = kwargs.get('conn')
        time_stamp = datetime.now().strftime(%Y-%m-%d %H:%M:%S)
        if not conn:
            raise ValueError("Connection object required")
        try:
            result = func(conn, *args, **kwargs)
            conn.commit()
            return result
        except Exception as e:
            conn.rollback()
            print(f"[{time_stamp}] Transaction rollback due to Error: {e}")
            raise
    return wrapper_transactional

@with_db_connection 
@transactional 
def update_user_email(conn, user_id, new_email): 
cursor = conn.cursor() 
cursor.execute("UPDATE users SET email = ? WHERE id = ?", (new_email, user_id)) 
#### Update user's email with automatic transaction handling 

update_user_email(user_id=1, new_email='Crawford_Cartwright@hotmail.com')
