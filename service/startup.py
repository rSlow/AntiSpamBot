import logging


async def on_startup(_):
    try:
        # Регистрация обработчиков. При объявлении через декораторы - их нужно импортировать
        import handlers

        # Регистрация логгера
        import logger
        import logger1

    except ImportError as ex:
        from logger import logger
        logger.exception("ON STARTUP IMPORT ERROR", ex)
