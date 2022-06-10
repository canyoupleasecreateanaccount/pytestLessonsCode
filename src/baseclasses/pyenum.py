from enum import Enum


class PyEnum(Enum):
    """
    Обычный ENUM класс с одним лишь отличием, мы расширили его одним методом
    который будет очень полезным для нас.

    Так как вы имеете список всех статусов и других параметров в виде ENUM,
    то почему бы не использовать это? Метод list будет возвращать все наши
    значения в виде списка, которые мы сможем использовать в нашем parametrize.

    Default ENUM class but with one difference. We have been added one
    additional method for us that returns all enum values as list, so as
    a result we can use them in parametrize construction in our autotests.
    """
    @classmethod
    def list(cls):
        return list(map(lambda c: c.value, cls))
