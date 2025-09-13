#!/usr/bin/python3
import sqlite3
import functools

#### decorator to lof SQL queries

 """ YOUR CODE GOES HERE"""
 def log_queries(func):
     @functools.wraps(func)
     def wrapper_log_queries(*args, **kwargs):
         log_args = args[0] if args else kwargs.get("query", None)
         if log_args:
             print(f"Executing SQL query: {log_query}")
         return func(*args, **kwargs)
     return wrapper_log_queries

@log_queries
def fetch_all_users(query):
    conn = sqlite3.connect('users.db')
    cursor = conn.cursor()
    cursor.execute(query)
    results = cursor.fetchall()
    conn.close()
    return results

#### fetch users while logging the query
users = fetch_all_users(query="SELECT * FROM users")
