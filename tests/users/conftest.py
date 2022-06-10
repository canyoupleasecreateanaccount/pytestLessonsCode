import pytest
import requests

from configuration import SERVICE_URL


@pytest.fixture
def get_users():
    """
    Пример фикстуры которая получает часто запрашиваемые данные с сервера.
    К примеру, вам нужно получать каких-то юзеров постоянно и брать одного
    рандомного, в таком случае этот вариант может стать отличным решением.

    Example of fixture that accept useful data from a server.
    For example, you need to get some users from the server regular and pick
    one random from them. So for that case fetching data using fixtures is a
    best solution.
    """
    response = requests.get(SERVICE_URL)
    return response


