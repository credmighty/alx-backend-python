#!/usr/bin/python3

from seed import connect_to_prodev
from mysql.connector import Error

# Generator function to stream user ages
def stream_user_ages():
    connection = connect_to_prodev()
    try:
        cursor = connection.cursor(dictionary=True)
        cursor.execute("SELECT age FROM user_data")
        for row in cursor:  # Loop 1: Yield each age
            yield row['age']
        cursor.close()
    except Error as e:
        print(f"Error streaming ages: {e}")
    finally:
        if cursor:
            cursor.close()

# Function to calculate average age using the generator
def calculate_average_age():
    connection = connect_to_prodev()
    try:
        total_age = 0
        count = 0
        for age in stream_user_ages(connection):  # Loop 2: Process ages
            total_age += age
            count += 1
        if count == 0:
            return 0  # Avoid division by zero
        return total_age / count
    except Error as e:
        print(f"Error calculating average: {e}")
        return 0
