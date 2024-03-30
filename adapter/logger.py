from abc import ABC, abstractmethod
from logging import Logger


class ThirdPartyLogger:
    def log_message(self, message: str, level: str):
        # Предположим, здесь происходит запись лога
        print(f"{level}: {message}")


class ABCLogger(ABC, Logger):
    @abstractmethod
    def info(self, message, *args, **kwargs):
        raise NotImplementedError()

    @abstractmethod
    def warning(self, message, *args, **kwargs):
        raise NotImplementedError()

    @abstractmethod
    def error(self, message, *args, **kwargs):
        raise NotImplementedError()


class LoggerAdapter(ABCLogger):
    def __init__(self, third_party_logger):
        self.logger = third_party_logger

    def info(self, message, *args, **kwargs):
        self.logger.log_message(message, "INFO")

    def warning(self, message, *args, **kwargs):
        self.logger.log_message(message, "WARNING")

    def error(self, message, *args, **kwargs):
        self.logger.log_message(message, "ERROR")