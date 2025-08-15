import pymysql

try:
    connection = pymysql.connect(
        host="localhost",
        user="root",
        password="0703"
    )
    cursor = connection.cursor()
    cursor.execute("CREATE DATABASE IF NOT EXISTS alx_book_store")
    print("Database 'alx_book_store' created successfully!")
except Exception as e:
    print(f"Error while connecting to MySQL: {e}")
finally:
    if 'cursor' in locals():
        cursor.close()
    if 'connection' in locals():
        connection.close()
