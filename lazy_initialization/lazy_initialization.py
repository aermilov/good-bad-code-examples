import psycopg2

class Database:
    def __init__(self):
        self.connection = self.connect_to_database()

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
        print("Загрузка тяжелого ресурса")
        # Предположим, здесь происходит загрузка большого объема данных или сложная инициализация
        self.data = "some_large_data"

class User:
    def __init__(self):
        self.profile_picture = self.load_profile_picture()

    def load_profile_picture(self):
        print("Загрузка изображения профиля пользователя")
        # Загрузка изображения
        return "profile_picture_data"

class Application:
    def __init__(self):
        self.database = Database()
        self.heavy_resource = HeavyResource()
        self.users = [User() for _ in range(5)]

    def run(self):
        # Здесь код, который может и не использовать все предварительно загруженные ресурсы
        print("Запуск приложения")

app = Application()
app.run()