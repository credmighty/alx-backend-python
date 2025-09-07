#!/usr/bin/python3

from mysql.connector import Error
from seed import connect_to_prodev

# Function to fetch one page of users
def paginate_users(page_size, offset):
    connection = connect_to_prodev()
    try:
        cursor = connection.cursor(dictionary=True)
        query = "SELECT * FROM user_data LIMIT %s OFFSET %s"
        cursor.execute(query, (page_size, offset))
        rows = cursor.fetchall()
        cursor.close()
        return rows
    except Error as e:
        print(f"Error fetching page: {e}")
        return []

# Generator function to lazily paginate users 
def lazy_paginate(page_size):
    connection = connect_to_prodev()
    try:
        offset = 0
        while True:
            page = paginate_users(connection, page_size, offset)
            if not page:
                break
            for row in page:
                yield row
            offset += page_size
    except Error as e:
        print(f"Error in lazy pagination: {e}")
