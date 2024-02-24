import psycopg2

class Database:
    def __init__(self):
        self.connection = None

    def get_connection(self):
        if self._connection is None:
            self._connection = self.connect_to_database()
        return self._connection

    def connect_to_database(self):
        print("Подключение к базе данных")
        try:
            connection = psycopg2.connect(
                host="localhost",  # Или другой адрес сервера БД
                database="your_database_name",  # Имя вашей базы данных
                user="your_username",  # Ваше имя пользователя
                password="your_password")  # Ваш пароль
            print("Успешное подключение к базе данных")
            return connection
        except (Exception, psycopg2.DatabaseError) as error:
            print(error)
            return None

class HeavyResource:
    def __init__(self):
        self._data = None

    def get_data(self):
        if self._data is None:
            print("Загрузка тяжелого ресурса")
            self._data = "some_large_data"
        return self._data

class User:
    def __init__(self):
        self.profile_picture = None

    def get_profile_picture(self):
        if self._profile_picture is None:
            print("Загрузка изображения профиля пользователя")
            # Здесь происходит загрузка изображения
            self._profile_picture = "profile_picture_data"
        return self._profile_picture

class Application:
    def __init__(self):
        self.database = None
        self.heavy_resource = None
        self.users = [User() for _ in range(5)]

    def get_database(self):
        if self._database is None:
            self._database = Database()
        return self._database

    def get_heavy_resource(self):
        if self._heavy_resource is None:
            self._heavy_resource = HeavyResource()
        return self._heavy_resource

    def run(self):
        print("Запуск приложения")

app = Application()
app.run()