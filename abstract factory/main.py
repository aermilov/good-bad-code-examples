from abc import ABC, abstractmethod

class EnvEnum:
    mobile = 'mobile'
    web = 'web'


env = 'mobile'


# Абстрактные продукты
class Notification(ABC):
    @abstractmethod
    def show(self):
        pass

# Абстрактная фабрика
class NotificationFactory(ABC):
    @abstractmethod
    def create_message(self) -> Notification:
        pass

    @abstractmethod
    def create_warning(self) -> Notification:
        pass

    @abstractmethod
    def create_error(self) -> Notification:
        pass

# Конкретные продукты для веб-уведомлений
class WebMessage(Notification):
    def show(self):
        print("Showing web message notification")

class WebWarning(Notification):
    def show(self):
        print("Showing web warning notification")

class WebError(Notification):
    def show(self):
        print("Showing web error notification")

# Конкретная фабрика для веб-уведомлений
class WebNotificationFactory(NotificationFactory):
    def create_message(self) -> Notification:
        return WebMessage()

    def create_warning(self) -> Notification:
        return WebWarning()

    def create_error(self) -> Notification:
        return WebError()

# Конкретные продукты для мобильных уведомлений
class MobileMessage(Notification):
    def show(self):
        print("Showing mobile message notification")

class MobileWarning(Notification):
    def show(self):
        print("Showing mobile warning notification")

class MobileError(Notification):
    def show(self):
        print("Showing mobile error notification")

# Конкретная фабрика для мобильных уведомлений
class MobileNotificationFactory(NotificationFactory):
    def create_message(self) -> Notification:
        return MobileMessage()

    def create_warning(self) -> Notification:
        return MobileWarning()

    def create_error(self) -> Notification:
        return MobileError()


def factory_method() -> NotificationFactory:
    match env:
        case EnvEnum.mobile:
            return MobileNotificationFactory()
        case EnvEnum.web:
            return WebNotificationFactory()
    raise EnvironmentError()

# Демонстрация использования
def show_notifications(factory: NotificationFactory):
    message = factory.create_message()
    warning = factory.create_warning()
    error = factory.create_error()

    message.show()
    warning.show()
    error.show()

if __name__ == "__main__":
    # Использование веб-фабрики для отображения уведомлений

    factory: NotificationFactory = factory_method()
    show_notifications(factory)
