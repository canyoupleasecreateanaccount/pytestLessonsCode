from pydantic import BaseModel, EmailStr, validator
from pydantic.types import PastDate, FutureDate, List, PaymentCardNumber
from pydantic.networks import IPv4Address, IPv6Address
from src.schemas.physical import Physical

"""
Именно в этом файле можно поиграться с уже готовой моделью и примером
тестового объекта для неё.
"""

from src.enums.user_enums import Statuses


class Owners(BaseModel):
    name: str
    card_number: PaymentCardNumber
    email: EmailStr


class DetailedInfo(BaseModel):
    physical: Physical
    owners: List[Owners]


class Computer(BaseModel):
    id: int
    status: Statuses
    activated_at: PastDate
    expiration_at: FutureDate
    host_v4: IPv4Address
    host_v6: IPv6Address
    detailed_info: DetailedInfo


class Human(BaseModel):
    name: str
    last_name: str
    surname: str = None
    is_hide: bool

    @validator('is_hide')
    def validate_surname_showing(cls, hide_value, values):
        """
        Пример валидатора, который используется для проверки значения в поле
        is_hide.
        :param hide_value:
        :param values:
        :return:
        """
        if hide_value is False and values.get('surname') is None:
            raise ValueError('Surname should be presented')
        return hide_value


human = Human.parse_obj({
    "name": "Andrii",
    "last_name": "Shevchenko",
    "is_hide": True
})


class Inventory(BaseModel):
    sold: int
    string: int
    unavailable: int
    pending: int
    available: int
    not_available: int
    status01: int
    status: int
