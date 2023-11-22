# подключаем SQLite
import mysql.connector
from mysql.connector import Error

def create_connection(host_name, user_name, user_password):
    connection = None
    try:
        connection = mysql.connector.connect(
            host=host_name,
            user=user_name,
            passwd=user_password
        )
        print("Подключение к SQLite БД выполнено успешно")
    except Error as e:
        print(f"Ошибка '{e}' обнаружена")
    return connection

def create_database(connection, query):
    cursor = connection.cursor()
    try:
        cursor.execute(query)
        print("БД успешно создана")
    except Error as e:
        print(f"Ошибка '{e}' обнаружена")

def execute_query(connection, query):
    cursor = connection.cursor()
    try:
        cursor.execute(query)
        print("Запрос успешно выполнен")
    except Error as e:
        print(f"Ошибка '{e}' обнаружена")


connection = create_connection("localhost", "root", "root")
create_user_table = "CREATE DATABASE social"
create_database(connection, create_database_query)