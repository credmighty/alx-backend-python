def stream_users():
    try:
        cursor = cursor(dictionary=True) # return rows as dictionaries
        cursor.execute("SELECT * FROM user_data")
        for row in cursor:
            yield row
        cursor.close()
    except Error as e:
        print(f"Error streaming data: {e}")
    finally:
        if cursor:
            cursor.close()
