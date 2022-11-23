import psycopg2
from psycopg2 import Error
from config import *
import sys


try:
    # Подключиться к существующей базе данных
    connection = psycopg2.connect(user=user,
                                  password=password,
                                  host=host,
                                  database=db_name)

    # Создайте курсор для выполнения операций с базой данных
    cursor = connection.cursor()
    create_table_query = '''CREATE TABLE IF NOT EXISTS users
                          (id INT PRIMARY KEY NOT NULL,
                          name VARCHAR(50) NOT NULL,
                          age INTEGER ); '''
    insert_query = """INSERT INTO users (id, name, age) VALUES (1,'Harry Pother', 23)"""
    update_query = """Update users set name = Dambuldor where id = 1"""
    delete_query = """Delete from users where id = 1"""
    search_query = """SELECT id FROM users WHERE name = 'Harry POther';"""


    def myfunc(argv):
        arg_help = "{0} -c <create table> -f <fill table> -u <update> -s <search> -d <delete>".format(argv[0])
        arg_name = argv[1]

        if arg_name in ("-h", "--help"):
            print(arg_help)  # print the help message
            sys.exit(2)
        elif arg_name in ("-c", "--create"):
            cursor.execute(create_table_query)
            connection.commit()
            print("Таблица успешно создана в PostgreSQL")

        elif arg_name in ("-f", "--fill table"):
            cursor.execute(insert_query)
            connection.commit()
            print("1 запись успешно вставлена")

        elif arg_name in ("-u", "--update"):
            cursor.execute(update_query)
            connection.commit()
            count = cursor.rowcount
            print(count, 'Запись успешно обнавлено')
            cursor.execute("SELECT * from users")
            print("Результат", cursor.fetchall())

        elif arg_name in ("-d", "--delete"):
            cursor.execute(delete_query)
            connection.commit()
            count = cursor.rowcount
            print(count, "Запись успешно удалена")
            cursor.execute("SELECT * from users")
            print("Результат", cursor.fetchall())

        elif arg_name in ("-s", "--search"):
            cursor.execute(search_query)
            connection.commit()
            cursor.execute("SELECT * from users")
            print("Результат", cursor.fetchall())


    if __name__ == "__main__":
        myfunc(sys.argv)

except (Exception, Error) as error:
    print("Ошибка при работе с PostgreSQL", error)
finally:
    if connection:
        cursor.close()
        connection.close()
        print("Соединение с PostgreSQL закрыто")















    # create_table_query = '''CREATE TABLE IF NOT EXISTS mobile
    #                       (ID INT PRIMARY KEY     NOT NULL,
    #                       MODEL           TEXT    NOT NULL,
    #                       PRICE         REAL); '''
    #
    # # Выполнение команды: это создает новую таблицу
    # cursor.execute(create_table_query)
    # connection.commit()
    # print("Таблица успешно создана в PostgreSQL")
    #
    # # Выполнение SQL-запроса для вставки данных в таблицу
    # insert_query = """ INSERT INTO mobile (ID, MODEL, PRICE) VALUES (1, 'Iphone12', 1100)"""
    # cursor.execute(insert_query)
    # connection.commit()
    # print("1 запись успешно вставлена")
    #
    # # Получить результат
    # cursor.execute("SELECT * from mobile")
    # record = cursor.fetchall()
    # print("Результат", record)
    #
    # # Выполнение SQL-запроса для обновления таблицы
    # update_query = """Update mobile set price = 1500 where id = 1"""
    # cursor.execute(update_query)
    # connection.commit()
    # count = cursor.rowcount
    # print(count, "Запись успешно обнавлена")
    #
    # # Получить результат
    # cursor.execute("SELECT * from mobile")
    # print("Результат", cursor.fetchall())
    #
    # # Выполнение SQL-запроса для удаления таблицы
    # delete_query = """Delete from mobile where id = 1"""
    # cursor.execute(delete_query)
    # connection.commit()
    # count = cursor.rowcount
    # print(count, "Запись успешно удалена")
    #
    # # Получить результат
    # cursor.execute("SELECT * from mobile")
    # print("Результат", cursor.fetchall())