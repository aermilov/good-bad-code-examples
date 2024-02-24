import mysql.connector
from mysql.connector import Error
import pandas as pd


class MySQLConnection:
    def __init__(self, host_name, user_name, user_password, db_name):
        self.host_name = host_name
        self.user_name = user_name
        self.user_password = user_password
        self.db_name = db_name

    def __enter__(self):
        try:
            self.connection = mysql.connector.connect(
                host=self.host_name,
                user=self.user_name,
                passwd=self.user_password,
                database=self.db_name
            )
            print("Подключение к MySQL успешно установлено")
        except Error as e:
            print(f"Ошибка '{e}' при подключении к MySQL")
        return self

    def __exit__(self, exc_type, exc_value, trace):
        self.connection.close()

    def add_saldo_to_db(self, account_id, balance, date, currency):
        query = "INSERT INTO saldo (account_id, balance, date, currency) VALUES (%s, %s, %s, %s)"
        args = (account_id, balance, date, currency)
        try:
            cursor = self.connection.cursor()
            cursor.execute(query, args)
            self.connection.commit()
            print("Запись успешно добавлена")
        except Error as e:
            print(f"Ошибка '{e}' при добавлении данных")

    def add_charges_to_db(self, account_id, amount, date, description, currency):
        query = "INSERT INTO charges (account_id, amount, date, description, currency) VALUES (%s, %s, %s, %s, %s)"
        args = (account_id, amount, date, description, currency)
        try:
            cursor = self.connection.cursor()
            cursor.execute(query, args)
            self.connection.commit()
            print("Запись успешно добавлена")
        except Error as e:
            print(f"Ошибка '{e}' при добавлении данных")

    def add_payments_to_db(self, account_id, amount, date, method, currency):
        query = "INSERT INTO payments (account_id, amount, date, method, currency) VALUES (%s, %s, %s, %s, %s)"
        args = (account_id, amount, date, method, currency)
        try:
            cursor = self.connection.cursor()
            cursor.execute(query, args)
            self.connection.commit()
            print("Запись успешно добавлена")
        except Error as e:
            print(f"Ошибка '{e}' при добавлении данных")

    def get_table_data(self, table_name):
        query = f"SELECT * FROM {table_name};"
        data = pd.read_sql(query, self.connection)
        return data
