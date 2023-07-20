import pathlib

from aiogram.types import MessageEntityType, ContentTypes

# Первый раунд проверки основан на посимвольной проверке сообщений
# Поэтому ниже два набора, связанные с этой проверкой
# Список эмодзи, которые мы считаем признаками спам-сообщения
aware_emoji_list = [
    '❗',
    '🔞',
    '‼',
]

# Категории символов, которые не попадают в проверку
skip_categories = [
    'Zs',  # пробел
    'Nd',  # цифра
    'Pd',  # тире
    'Ps',  # скобки открывающие
    'Pe',  # скобки закрывающие
    'Po',  # пунктуация остальная
]

# А это набор энтитисов в сообщениях, по которым мы тоже напрягаемся
forbidden_entities = [
    MessageEntityType.URL,
    MessageEntityType.MENTION,
    MessageEntityType.TEXT_LINK
]

# тут будет корневая директория
BASE_DIR = pathlib.Path(__file__).resolve().parent.parent

# общий список для проверяемых типов сообщения, чтобы не дублироваться
# Звездочка перед переменной - распаковка списка "прямо здесь".
# Почему-то, ContentTypes.TEXT равно ['text'] (именно список с одним элементом), а не строка 'text'
content_types = [
    *ContentTypes.TEXT,
    *ContentTypes.PHOTO
]

