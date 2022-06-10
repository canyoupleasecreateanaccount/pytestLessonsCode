from enum import Enum

from src.baseclasses.pyenum import PyEnum

"""
Один из тысяч файлов ENUM которые будут у вас в проекте. 
Нужны они для того, чтобы упростить поддержку вашего проекта и упростить
фикс самых простых изменений, которые могли бы занять у вас много времени.
К примеру, если изменится значение какого-то параметра, то вам не нужно будет 
бегать по всему проекту, достаточно будет изменить только здесь и всё.
"""


class Genders(Enum):
    """
    Класс для хранения пола пользователя.
    """
    female = "female"
    male = "male"


class Statuses(PyEnum):
    """
    Вариант хранения всех возможных статусов пользователя.
    """
    ACTIVE = "ACTIVE"
    BANNED = "BANNED"
    DELETED = "DELETED"
    INACTIVE = "INACTIVE"
    MERGED = "MERGED"


class UserErrors(Enum):
    """
    Класс с кастомными ошибками для какого-то конкретной сущности или
    тестируемого ендпоинта.
    """
    WRONG_EMAIL = "Email doesn't contain @"
