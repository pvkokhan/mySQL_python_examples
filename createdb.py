import mysql.connector
from mysql.connector import Error

def create_connection(host_name, user_name, user_password):
    connection = None
    try:
        connection = mysql.connector.connect(
            host = host_name,
            user = user_name,
            passwd = user_password,
        )
        print("Connection to DB sucsessful")
    except Error as e:
        print(f"The error '{e}'occurred")

    return connection
connection = create_connection("localhost", "root", "Fedotdanet0t")

def create_database(connection, query):
    cursor = connection.cursor()
    try:
        cursor.execute(query)
        print("DB create sucsessfully")
    except Error as e:
        print(f"The error '{e}'occurred")

create_database_query = "CREATE DATABASE test_app"

#createdb.create_database(createdb.connection, createdb.create_database_query)