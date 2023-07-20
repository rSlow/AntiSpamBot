async def on_startup(_):
    try:
        # Регистрация логгера
        import logger

        # Регистрация обработчиков. При объявлении через декораторы - их нужно импортировать
        import handlers

    except ImportError as ex:
        import logging
        logging.exception("ON STARTUP IMPORT ERROR", exc_info=ex)
