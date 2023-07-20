import logging

from aiogram import types

import logger
from bot import dispatcher
from service import service, constants, symbol_counter


@dispatcher.message_handler(content_types=constants.content_types)
async def handle_spam(message: types.Message):
    input_text = service.get_message_text(message)
    counter = symbol_counter.SymbolCounter(input_text)

    logging.info(f"Символы: {counter.cyrillic, counter.latin, counter.unknown, counter.forbidden_emoji}")

    if counter.unknown >= 2 or counter.forbidden_emoji >= 3:
        # Если хотя бы два символа странных юникодов или хотя бы три запретных эмодзи, то пидор найден. Удаляем
        await service.delete_message(message, 'Вижу спам. Удалю через 10 секунд')


@dispatcher.message_handler(content_types=constants.content_types)
async def handle_stop_list(message: types.Message):
    input_text = service.get_message_text(message)
    has_url = service.check_has_url_in_message(message)

    stop_words = service.check_matches_in_file(
        file=constants.BASE_DIR / "stop_list",
        string=input_text
    )
    logging.info(f"стоп слов: {stop_words}")
    # если стоп-слов хотя бы два и ссылка в энтитис, то это - пидор
    if has_url and stop_words >= 2:
        await service.delete_message(message, 'Похоже на политоту. Удалю через 10 секунд')


@dispatcher.message_handler(content_types=constants.content_types)
async def handle_hujnya_list(message: types.Message):
    input_text = service.get_message_text(message)
    has_url = service.check_has_url_in_message(message)

    hujnya_words = service.check_matches_in_file(
        file=constants.BASE_DIR / "hujnya_list",
        string=input_text
    )
    logging.info(f"слов из рекламной хуйни: {hujnya_words}")
    if has_url and hujnya_words >= 3:
        await service.delete_message(message, 'Похоже на хуйню кликбейтную. Удалю через 10 секунд')


@dispatcher.message_handler(content_types=constants.content_types)
async def handle_url_and_photo(message: types.Message):
    has_url = service.check_has_url_in_message(message)

    # Всякие вайлберисы присылают картинку без текста, но со ссылкой
    # Поэтому четвёртый этап проверки как раз об этом
    # Потому что первые три он пройдёт спокойно, текста же нет.
    # Тут ещё важно участь, что может запоститься реклама, которую Артём размещает
    # И оно обязательно попадёт в этот фильтр.
    # Поэтому добавляем в условие не реагировать, если пост от GroupAnonymousBot
    # Не уверен, что это правильный метод. Надо перепроверять

    if has_url and message.photo and (message.from_user.username != 'GroupAnonymousBot'):
        await service.delete_message(message, 'Картиночка со ссылочкой? Похоже на рекламу. Удалю через 10 секунд')
