
from enum import Enum


class PyEnum(Enum):

    @classmethod
    def list(cls):
        return list(map(lambda c: c.value, cls))
