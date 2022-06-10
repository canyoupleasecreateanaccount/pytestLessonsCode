from enum import Enum


class GlobalErrors(Enum):
    """
    Обычный класс с ошибками которые стоит использовать в ваших Assert и в
    Response класс. Нужно это для того, чтобы:
    1. Унифицировать всё это дело
    2. Облегчить использование и обновление ошибок

    Default ENUM class with error that should be used in your asserts and in
    Response class. It needs for:
    1. Unification
    2. Helps in code support
    """
    WRONG_STATUS_CODE = 'Status code is different than expected'
