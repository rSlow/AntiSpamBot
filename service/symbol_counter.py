import logging
import unicodedata

from logger import logger
from service import constants


class SymbolCounter:
    def __init__(self,
                 text_message: str):
        self.cyrillic: int = 0
        self.latin: int = 0
        self.unknown: int = 0
        self.forbidden_emoji: int = 0

        self._text_message = text_message

        self._count()

    def _count(self):
        for char in self._text_message:
            try:
                unicodedata.name(char)  # проверки на возможность декодирования символа в Unicode
            except UnicodeError:
                # Тут хорошей практикой является указывать конкретную ошибку. В данном случае при сваливании проверки
                # выше - будет ошибка UnicodeError. Другие возникающие ошибки пропускаться не будут, и вызовут
                # исключение.
                logger.warning(f"UnicodeError at decoding symbol {char}")
                continue

            if char.isalpha():
                # isalpha() проверяет, является ли символ текстовым (не цифра, знак препинания или что-то еще).

                if unicodedata.name(char).startswith('CYRILLIC'):
                    self.cyrillic += 1
                elif unicodedata.name(char).startswith('LATIN'):
                    self.latin += 1
                else:
                    self.unknown += 1

            else:
                if unicodedata.category(char) not in constants.skip_categories:
                    # если символ не альфа и не пунктуация (в скип листе), то в консоль пишем его расшифровки.
                    # чтобы сразу видеть новые, которые могут быть кандидатами в запрещённые.

                    # Можно для aware_emoji_list создать отдельный файлик, и дергать оттуда, чтобы в файл можно было
                    # дозаписать нужные символы, без перезапуска бота.
                    logging.warning(
                        f"Запрещенный символ - {unicodedata.name(char)} <{unicodedata.category(char)}>"
                    )

                    if unicodedata.name(char) in constants.aware_emoji_list:
                        self.forbidden_emoji += 1
