import logging

from service import constants

LOGS_DIR = constants.BASE_DIR / "logs"

# Если папки logs не существует, программа свалится с ошибкой.
# Эта строчка проверяет наличие папки, если папки нет - создает
LOGS_DIR.mkdir(exist_ok=True)

logging.basicConfig(
    filename=LOGS_DIR / "log.log",
    level=logging.INFO
)
