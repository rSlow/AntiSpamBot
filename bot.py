import logging

from aiogram import Bot, Dispatcher
from environs import Env

from service.constants import BASE_DIR

ENV = Env()
ENV.read_env(str(BASE_DIR / "env.env"))

bot = Bot(token=ENV.str("BOT_TOKEN"))
dispatcher = Dispatcher(bot=bot)

# Базовый логгер для aiogram
# (он не воспринимает loguru как стандартный логгер. Как скормить loguru аиограмму - я не знаю)
logging.basicConfig(level=logging.INFO)
