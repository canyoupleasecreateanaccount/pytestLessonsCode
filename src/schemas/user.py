from pydantic import BaseModel, validator

from src.enums.user_enums import Genders, Statuses, UserErrors

"""
Пример описания pydantic model с использованием Enum и validator.

Example of describing pydantic model with using ENUM and validator features.
"""


class User(BaseModel):
    id: int
    name: int
    email: str
    password: str
    gender: Genders
    status: Statuses

    @validator('email')
    def check_that_dog_presented_in_email_address(cls, email):
        """
        Проверяем наше поле email, что в нём присутствует @ и в случае
        если она отсутствует, возвращаем ошибку.

        Checking fild email that in the filed contain @ and if it absent returns
        error, if not pass.
        """
        if '@' in email:
            return email
        else:
            raise ValueError(UserErrors.WRONG_EMAIL.value)
