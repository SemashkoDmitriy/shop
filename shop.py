# подключаем SQLite
import sqlite3
from sqlite3 import Error

def create_connection(path):
    connection = None
    try:
        connection = sqlite3.connect(path)
        print("Подключение к SQLite БД выполнено успешно")
    except Error as e:
        print(f"Ошибка '{e}' обнаружена")
    return connection

connection = create_connection("C:\\Temp\\social.sqlite")