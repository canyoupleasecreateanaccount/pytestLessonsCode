import pytest

from random import randrange

import tables
from src.generators.player import Player
from src.generators.item_type_generator import ItemsTypeBuilder

from db import Session


@pytest.fixture
def get_player_generator():
    """
    Пример фикстуры для инициализации объекта генератора и передачу его в
    тест.

    Fixture that initialize generator object and returns it into autotest.
    """
    return Player()


@pytest.fixture
def get_item_type_generator():
    """
    Пример фикстуры для инициализации объекта генератора и передачу его в
    тест.

    Fixture that initialize generator object and returns it into autotest.
    """
    return ItemsTypeBuilder()


@pytest.fixture
def get_number():
    """
    Просто метод для генерации рандомного числа :)

    Method that generates random number :)
    """
    return randrange(1, 1000, 5)


def _calculate(a, b):
    """
    Функция которая выполняет какую-то логику. При этом, ниже фикстура, которая
    отдаёт его в тест как объект, чтобы можно было применить там как
    именно как функцию.

    It is function that does some logic. Please check fixture below, that
    returns that function as object into autotest where you can call it as
    a common function and pass some param into it.
    """
    if isinstance(a, int) and isinstance(b, int):
        return a + b
    else:
        return None


@pytest.fixture
def calculate():
    """
    Передача функции в тест используя фикстуру.

    Return function as an object into autotest.
    """
    return _calculate


@pytest.fixture
def make_number():
    """
    Делаем какую-то логику, передаём управление тесту используя конструкцию
    yield и уже после того, как тест закончился, выполняем вторую часть кода.

    In that case we do some logic, than return number to autotest, wait till
    test has been passed and after it again do some logic.
    """
    print("I'm getting number")
    number = randrange(1, 1000, 5)
    yield number
    print(f"Number at home {number}")


@pytest.fixture
def get_db_session():
    """
    Создание сессии для работы с базой данных.
    Пожалуйста, обратите внимание, что мы в любом случае закрываем нашу сессию.

    Creating of database session and return it into our autotest.
    Please check, that in any case, we close our db session.
    """
    session = Session()
    try:
        yield session
    finally:
        session.close()


def delete_test_data(session, table, filter_data):
    """
    Функция для удаления данных из базы.

    Example of function for delete test data from database.
    """
    session.query(table).filter(filter_data).delete()
    session.commit()


def add_method(session, item):
    """
    Функция для добавления данных в базу.

    Example of function for add test data from database.
    """
    session.add(item)
    session.commit()


@pytest.fixture
def generate_item_type(
        get_db_session,
        get_item_type_generator,
        get_add_method,
        get_delete_method
):
    """
    Пример фикстуры которая использует другие фикстуры. С помощью этого примера
    мы можем подготовить себе тестовые данные в базе, передать их в тест, а
    уже после выполнения удалить.

    Example of fixture that uses another fixtures inside itself.
    Using that example we can create test data, return it into autotest and
    after test execution delete all from database.
    """
    item = tables.ItemType(**get_item_type_generator.build())
    get_add_method(get_db_session, item)
    yield item
    get_delete_method(
        get_db_session,
        tables.ItemType,
        (tables.ItemType.item_id == item.item_id)
    )


@pytest.fixture
def get_add_method():
    """
    Пример фикстуры которая передаёт функцию для добавления данных в базу
    как объект в тест.

    Example of fixture, that returns add method as object into our tests.
    """
    return add_method


@pytest.fixture
def get_delete_method():
    """
    Пример фикстуры которая передаёт функцию для удаления данных в базу
    как объект в тест.

    Example of fixture, that returns delete method as object into our tests.
    """
    return delete_test_data
