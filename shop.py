# подключаем SQLite
import sqlite3 as sl

# создаем (открываем) файл с БД
con = sl.connect('shop.db')

with con:
    # получаем количество таблиц с нужным нам именем
    data = con.execute("SELECT COUNT(*) FROM sqlite_master WHERE TYPE='table' AND NAME='goods'")
    for row in data:
        # если таких таблиц нет
        if row[0] == 0:
            #создаем таблицу для товаров
            with con:
                con.execute("""
                    CREATE TABLE goods (
                        product VARCHAR(20) PRIMARY KEY,
                        amount INTEGER,
                        price INTEGER
                        );
                """)

    data = con.execute("SELECT COUNT(*) FROM sqlite_master WHERE TYPE='table' AND NAME='clients'")
    for row in data:
        # если таких таблиц нет
        if row[0] == 0:
            # создаем таблицу для товаров
            with con:
                con.execute("""
                        CREATE TABLE clients (
                            id INT PRIMARY KEY,
                            name VARCHAR(40),
                            phone VARCHAR(10)
                            );
                    """)

    data = con.execute("SELECT COUNT(*) FROM sqlite_master WHERE TYPE='table' AND NAME='orders'")
    for row in data:
        # если таких таблиц нет
        if row[0] == 0:
            # создаем таблицу для товаров
            with con:
                con.execute("""
                            CREATE TABLE orders (
                                order_id INT PRIMARY KEY,
                                product VARCHAR(20),
                                amount INT,
                                client_id INT,
                                FOREIGN KEY (product) REFERENCES goods(product),
                                FOREIGN KEY (client_id) REFERENCES clients(id)
                                );
                        """)

    #подготавливаем множественный запрос для таблицы goods
    sql = 'INSERT INTO goods(product, amount, price) VALUES(?, ?, ?)'
    #указываем данные для запроса
    data = [
        ('Стол2', 2, 3000),
        ('Стул2', 5, 1000),
        ('Табурет2', 1, 500)
    ]
    #добавляем с помощью множественного запроса все данные сразу
    with con:
        con.executemany(sql, data)
    #выводим содержимое таблицы на экран
    with con:
        data = con.execute('SELECT * FROM goods')
        for row in data:
            print(row)

        # подготавливаем множественный запрос для таблицы clients
        sql = 'INSERT INTO goods(product, amount, price) VALUES(?, ?, ?)'
        # указываем данные для запроса
        data = [
            ('Стол2', 2, 3000),
            ('Стул2', 5, 1000),
            ('Табурет2', 1, 500)
        ]
        # добавляем с помощью множественного запроса все данные сразу
        with con:
            con.executemany(sql, data)
        # выводим содержимое таблицы на экран
        with con:
            data = con.execute('SELECT * FROM goods')
            for row in data:
                print(row)

        # подготавливаем множественный запрос для таблицы orders
        sql = 'INSERT INTO goods(product, amount, price) VALUES(?, ?, ?)'
        # указываем данные для запроса
        data = [
            ('Стол2', 2, 3000),
            ('Стул2', 5, 1000),
            ('Табурет2', 1, 500)
        ]
        # добавляем с помощью множественного запроса все данные сразу
        with con:
            con.executemany(sql, data)
        # выводим содержимое таблицы на экран
        with con:
            data = con.execute('SELECT * FROM goods')
            for row in data:
                print(row)
