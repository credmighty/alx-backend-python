#!/usr/bin/python3

from seed import connect_to_prodev
from mysql.connector import Error

# Generator function to stream rows in batches
def stream_users_in_batches(batch_size):
    connection = connect_to_prodev()
    try:
        cursor = connection.cursor(dictionary=True)  # Return rows as dictionaries
        cursor.execute("SELECT * FROM user_data")
        while True:
            batch = cursor.fetchmany(batch_size)  # Fetch the next batch of rows
            if not batch:  # If no more rows, stop
                break
            yield batch  # Yield the batch (list of rows)
        cursor.close()
    except Error as e:
        print(f"Error streaming data: {e}")
    finally:
        if cursor:
            cursor.close()

# Generator function to process batches and filter users over 25
def batch_processing(batch_size):
    try:
        for batch in stream_users_in_batches(batch_size):
            # Filter users over 25 years old
            filtered_batch = (user for user in batch if user['age'] > 25)
            if filtered_batch:  # Only yield if the filtered batch is not empty
                yield filtered_batch
    except Error as e:
        print(f"Error processing batches: {e}")
