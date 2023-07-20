async def on_startup(_):
    try:
        # Регистрация обработчиков. При объявлении через декораторы - их нужно импортировать
        import handlers

        # Регистрация логгера
        import logger

    except ImportError:
        raise
