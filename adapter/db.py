from time import sleep

from adapter.logger import ABCLogger


def insert(logger: ABCLogger):
    logger.info("Начинается вставка")
    sleep(0.5)
    logger.warning("оо, кажется что-то не так")
    sleep(0.5)
    logger.error("ну всё, пи***")