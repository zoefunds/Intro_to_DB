import mysql.connector
from mysql.connector import Error
from datetime import datetime

def create_database():
    """
    Creates the alx_book_store database in MySQL server.
    Handles connection errors and ensures proper resource management.
    
    Current Date and Time (UTC): 2025-11-16 22:11:49
    Current User's Login: AirdropGucci
    """
    connection = None
    try:
        # Connect to MySQL server
        connection = mysql.connector.connect(
            host='localhost',
            user='root',
            password='',  # Update with your MySQL password if needed
            port=3306
        )
        
        if connection.is_connected():
            db_info = connection.get_server_info()
            print(f"Successfully connected to MySQL Server version {db_info}")
            
            # Create cursor to execute queries
            cursor = connection.cursor()
            
            try:
                # Create database if it does not exist
                cursor.execute("CREATE DATABASE IF NOT EXISTS alx_book_store")
                
                # Print success message
                print("Database 'alx_book_store' created successfully!")
                
            except Error as e:
                print(f"Error executing CREATE DATABASE query: {e}")
            
            finally:
                # Close cursor
                cursor.close()
    
    except Error as e:
        print(f"Error while connecting to MySQL: {e}")
    
    except Exception as e:
        print(f"An unexpected error occurred: {e}")
    
    finally:
        # Close the database connection
        if connection is not None and connection.is_connected():
            connection.close()
            print("MySQL connection is closed")

if __name__ == "__main__":
    create_database()