import pytest
import requests

from configuration import SERVICE_URL


@pytest.fixture
def get_users():
    """
    Пример фикстуры которая получает часто запрашиваемые данные с сервера.
    К примеру, вам нужно получать каких-то юзеров постоянно и брать одного
    рандомного, в таком случае этот вариант может стать отличным решением.
    """
    response = requests.get(SERVICE_URL)
    return response


