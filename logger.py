import logging
from loguru import logger

from service import constants

LOGS_DIR = constants.BASE_DIR / "logs"

# Если папки logs не существует, программа свалится с ошибкой.
# Эта строчка проверяет наличие папки, если папки нет - создает
LOGS_DIR.mkdir(exist_ok=True)

# Настройка loguru
logger.add(
    encoding="u8",
    sink=LOGS_DIR / "loguru_log.log",
    format="{time:DD-MM-YYYY at HH:mm:ss} | {level} | {message}",
    backtrace=False,  # если кратко - чуть сокращает вывод исключения
    # rotation="1 week", # автоочистка файла лога спустя определенное время
)
