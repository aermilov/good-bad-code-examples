from contextlib import contextmanager
from time import sleep
from typing import List
import mysql.connector
from mysql.connector import Error
import pandas as pd


class MySQLConnection:
    def __init__(self, host_name, user_name, user_password, db_name):
        self.host_name = host_name
        self.user_name = user_name
        self.user_password = user_password
        self.db_name = db_name
        self.lock = False

    def connect(self):
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

    def disconnect(self):
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


class MySQLConnectionPoll:
    def __init__(self, host_name, user_name, user_password, db_name, num=1, heated=0):
        if num < heated:
            raise ValueError("Number of heated connections are more than total")

        self.host_name = host_name
        self.user_name = user_name
        self.user_password = user_password
        self.db_name = db_name
        self.num = num
        self.connections: List[MySQLConnection] = []
        for _ in range(heated):
            self._add_new_connection()

    def add_new_connection(self):
        # Check if the number of connections has exceeded the limit
        if len(self.connections) + 1 == self.num:
            raise ValueError("Number of connections exceeded")
            return
        return self._add_new_connection()

    def _add_new_connection(self):
        # Create a new MySQLConnection object and add it to the connections list
        conn = MySQLConnection(self.host_name, self.user_name, self.user_password, self.db_name)
        conn.connect()
        self.connections.append(conn)
        return conn

    def _get_unused_connection(self):
        # Loop through the connections list and return the first unused connection
        for conn in self.connections:
            if not conn.lock:
                return conn
        return None

    def _wait_until_unused(self):
        # Wait until an unused connection is available
        while True:
            conn = self._get_unused_connection()
            if conn is not None:
                return conn
            sleep(1)

    def get_connection(self):
        conn = self._get_unused_connection()
        if conn is not None:
            return conn

        if len(self.connections) < self.num:
            return self.add_new_connection()

        return self._wait_until_unused()

    @contextmanager
    def get_connection_context(self):
        conn = self.get_connection()
        conn.lock = True
        try:
            yield conn
        finally:
            conn.lock = False

    def close_all_connections(self):
        for conn in self.connections:
            conn.disconnect()
        self.connections = []
