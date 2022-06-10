from pydantic import BaseModel, HttpUrl, UUID4

from pydantic.color import Color

"""
Пример описания pydantic model с нестандартными типами полей.
Позже эта модель будет использована как часть другой модели.

Example of describing pydantic mode with rare types.
Later that model we will use as a part of another model.
"""


class Physical(BaseModel):
    color: Color
    photo: HttpUrl
    uuid: UUID4
