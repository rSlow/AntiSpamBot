import asyncio
from logger import logger
import re
import unicodedata

from aiogram import types

from service import constants


def get_message_text(message: types.Message) -> str:
    # Вынес извлечение текста из сообщения в отдельную функцию, т.к. может понадобиться много где, а суть одна и та же

    if message.text:
        return message.text
    if message.caption:
        return message.caption

    return ""


async def delete_message(message: types.Message, text):
    logger.info(text)

    reply_message = await message.reply(text=text)
    await asyncio.sleep(10)
    await message.delete()
    await reply_message.delete()


def check_has_url_in_message(message):
    """дефка проверит энтитис на содержание запрещённых"""

    # Сделал return сразу по обнаружении URL, ибо при нахождении урла дальнейшая проверка не имеет смысла.
    # Вообще, такая схема return в середине функции не приветствуется, но если дело касается такого типа проверок
    # - само то
    # И переименовал. Называть функцию с глагола - хорошая практика, т.к. функция по сути выполняет какое-то действие
    # (но это правило действует не всегда, конечно же :) )

    for item in message.entities:
        if item.type in constants.forbidden_entities:
            return True
    for item in message.caption_entities:
        if item.type in constants.forbidden_entities:
            return True

    return False


def printunicodes(string):
    """дефка чисто для отладки нужна была"""

    # не нашел, чтобы где-то использовалась, но пусть будет)

    for char in string:
        print(char, unicodedata.category(char), char.isalpha(), unicodedata.name(char))


def check_matches_in_file(file: str, string: str) -> int:
    """
    есть некий стоп-лист в файлике
    в нём части слов, по которым мы понимаем, что пост - спамный
    дефка считывает файл и считает, сколько совпадений стоп-слов в посте
    """

    # Объединил функции, чтобы можно было подкидывать в нее любой файл. Функционал, по сути, тут будет одинаковый для
    # любого файла, поэтому на каждый файл создавать отдельную функцию не нужно.

    matches = 0
    lower_string = string.lower()

    with open(file, encoding="utf-8") as file:
        stop_list_words = file.readlines()

    for stop_word in stop_list_words:
        string_matches = len(re.findall(stop_word, lower_string))
        matches += string_matches

    return matches
