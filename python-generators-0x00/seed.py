#!/usr/bin/python3

import mysql.connector
import csv
import uuid
from mysql.connector import Error

def connect_db():
    try:
        sql_connection = mysql.connector.connect(
                host='localhost',
                user='root',
                password='password'
        )
        if sql_connection.is_connected():
            print("Connected to MySQL server!")
            return sql_connection
    except Error as e:
        print(f'Oops, something went wrong: {e}')
        return None

# Function to create the ALX_prodev database
def create_database(connection):
    try:
        cursor = connection.cursor()
        cursor.execute("CREATE DATABASE IF NOT EXISTS ALX_prodev")
        print("ALX-prodev active now")
    except Error as e:
        print(f"Error creating Database: {e}")
    finally:
        cursor.close()

# Function to connect to ALX_prodev database
def connect_to_prodev():
    try:
        alxdb_connection = mysql.connector.connect(
            host='localhost',
            user='root',
            password='password',
            database='ALX_prodev'
        )
        if alxdb_connection.is_connected():
            print("Connected to ALX_prodev Database")
            return alxdb_connection
    except Error as e:
        print(f"Oops, something went wrong: {e}")
        return None

# Function to create the user_data table
def create_table(connection):
    try:
        cursor = connection.cursor()
        create_table_query = """
        CREATE TABLE IF NOT EXISTS user_data (
            user_id VARCHAR Primary Key,
            name VARCHAR(255) NOT NULL,
            email VARCHAR(255) NOT NULL,
            age DECIMAL(5,2) NOT NULL,
            INDEX idx_user_id (user_id)
        )
        """
        cursor.execute(create_table_query)
        connection.commit()
        print("user_data table created or already exists!")
    except Error as e:
        print(f"Error creating table: {e}")
    finally:
        cursor.close()

# Function to insert data from CSV into user_data table
def insert_data(connection, data):
    try:
        cursor = connection.cursor()
        with open(data, mode='r', encoding='utf-8') as file:
            csv_reader = csv.DictReader(file)
            for row in csv_reader:
                #check if user_id already exists
                cursor.execute("SELECT user_id FROM user_data WHERE user_id=%s",(row['user_id'],))
                if cursor.fetchone():
                    print(f"Skipping duplicate user_id: {row['user_id']}")
                    continue
                insert_query = """
                INSERT INTO user_data(user_id, name, email, age)
                VALUES(%s, %s, %s, %s)
                """
                cursor.execute(insert_query, (
                    row['user_id'],
                    row['name'],
                    row['email'],
                    float(row['age'])
                ))
                connection.commit()
                print(f"Inserted data for {row['name']}")
    except Error as e:
        print(f"Error inserting data: {e}")
    except KeyError as e:
        print(f"Missing column in CSV: {e}")
    finally:
        cursor.close()
            cursor.close()
