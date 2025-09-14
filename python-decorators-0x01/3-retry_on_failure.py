import time
import sqlite3 
import functools
from 1-with_db_connection import with_db_connection
from datetime import datetime

#### paste your with_db_decorator here

""" your code goes here"""
def retry_on_failure(retries=3, delay=2):
    def decorator(func):
        @functools.wraps(func)
        def wrapper(*args, **kwargs):
            last_exception = None
            for retry in range(1, retries + 1):
                try:
                    return func(*args, **kwargs)
                except Exception as e:
                    last_exception = e
                    time_stamp = datetime.now().strftime(%Y-%m-%d %H:%M:%S)
                    print(f"[{time_stamp}] Attempt {retry} failed {e}")
                    if retry < retries:
                        print(f"[{time_stamp}] Retryin in {delay} seconds...")
                        time.sleep(delay)
            print(f"[{time_stamp}] all retry attempts failed.")
            raise last_exception
        return wrapper
    return decorator


@with_db_connection
@retry_on_failure(retries=3, delay=1)

def fetch_users_with_retry(conn):
cursor = conn.cursor()
cursor.execute("SELECT * FROM users")
return cursor.fetchall()

#### attempt to fetch users with automatic retry on failure

users = fetch_users_with_retry()
print(users)
