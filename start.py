from bot import dispatcher
from aiogram import executor

from service import startup

if __name__ == '__main__':
    executor.start_polling(
        dispatcher=dispatcher,
        skip_updates=True,
        on_startup=startup.on_startup
    )
