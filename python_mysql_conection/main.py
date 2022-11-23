import pymysql
from config import *
import sys


create_table_query = "CREATE TABLE `users`(id int AUTO_INCREMENT," \
                                  " name varchar(32)," \
                                  " age integer(32));"
insert_query = "INSERT INTO `users` (name, age) VALUES ('Anna', '24');"
update_query = "UPDATE `users` SET name = 'Anna' WHERE age = '24';"
delete_query = "DELETE FROM `users` WHERE id = 1;"
search_query = "SELECT * FROM 'users' where id = (SELECT LAST_INSERT_ID());"


try:
    connection = pymysql.connect(
        host=host,
        port=3306,
        user=user,
        password=password,
        database=db_name,
        cursorclass=pymysql.cursors.DictCursor
    )
    print("successfully connected...")
    print("#" * 20)
    cursor = connection.cursor()

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
            cursor.execute("SELECT * FROM users")
            print("Результат", cursor.fetchall())

        elif arg_name in ("-d", "--delete"):
            cursor.execute(delete_query)
            connection.commit()
            count = cursor.rowcount
            print(count, "Запись успешно удалена")
            cursor.execute("SELECT * FROM users")
            print("Результат", cursor.fetchall())

        elif arg_name in ("-s", "--search"):
            cursor.execute(search_query)
            connection.commit()
            cursor.execute("SELECT * FROM users")
            print("Результат", cursor.fetchall())


    if __name__ == "__main__":
        myfunc(sys.argv)

except Exception as ex:
    print("Connection refused...")
    print(ex)

