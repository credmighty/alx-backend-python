import time
import sqlite3 
import functools
from datetime import datetime
from 1-with_db_connection import with_db_connection

query_cache = {}

"""your code goes here"""
def cache_query(func):
    @functools.wraps(func)
    def wrapper(conn, *args, **kwargs):
        """Get query string: assume it is passed as a keyword
        or the first positional argument
        """
        query = kwargs.get('query') if 'query' in kwargs else (args[0] if args else None)
        time_stamp = datetime.now().strftime(%Y-%m-%d %H:%M:%S)

        if query in query_cache:
            print(f"[{time_stamp}] [CACHE HIT] Returning cache result for query: {query}")
            return query_cache[query]
        else:
            result = func(conn, *args, **kwargs)
            query_cache[query] = result
            print(f"[{time_stamp}] [CACHE MISS] Caching result for query: {query}")
            return result
    return wrapper


@with_db_connection
@cache_query
def fetch_users_with_cache(conn, query):
    cursor = conn.cursor()
    cursor.execute(query)
    return cursor.fetchall()

#### First call will cache the result
users = fetch_users_with_cache(query="SELECT * FROM users")

#### Second call will use the cached result
users_again = fetch_users_with_cache(query="SELECT * FROM users")
