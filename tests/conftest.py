import pytest

from random import randrange


@pytest.fixture
def get_number():
    return randrange(1, 1000, 5)


def _calculate(a, b):
    return a + b


@pytest.fixture
def calculate():
    return _calculate


@pytest.fixture
def make_number():
    print("I'm getting number")
    number = randrange(1, 1000, 5)
    yield number
    print(f"Number at home {number}")
