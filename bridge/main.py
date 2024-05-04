from abc import ABC, abstractmethod

# Абстрактный класс аутентификации
class Authentication(ABC):
    @abstractmethod
    def authenticate(self):
        pass

# Реализация аутентификации с использованием пароля
class PasswordAuthentication(Authentication):
    def authenticate(self):
        print("Authenticating using a password...")

# Реализация аутентификации с использованием биометрии
class BiometricAuthentication(Authentication):
    def authenticate(self):
        print("Authenticating using biometric data...")

# Абстрактный класс учетной записи
class Account(ABC):
    def __init__(self, authentication):
        self.authentication = authentication

    @abstractmethod
    def access_resources(self):
        pass

# Конкретная реализация учетной записи пользователя
class UserAccount(Account):
    def access_resources(self):
        print("User accessing resources...")
        self.authentication.authenticate()

# Конкретная реализация учетной записи администратора
class AdminAccount(Account):
    def access_resources(self):
        print("Admin accessing sensitive resources...")
        self.authentication.authenticate()

# Пример использования
if __name__ == "__main__":
    password_auth = PasswordAuthentication()
    biometric_auth = BiometricAuthentication()

    user_account = UserAccount(password_auth)
    admin_account = AdminAccount(biometric_auth)

    user_account.access_resources()
    admin_account.access_resources()
