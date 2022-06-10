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
    """
    return Player()


@pytest.fixture
def get_item_type_generator():
    """
    Пример фикстуры для инициализации объекта генератора и передачу его в
    тест.
    """
    return ItemsTypeBuilder()


@pytest.fixture
def get_number():
    """
    Просто метод для генерации рандомного числа :)
    """
    return randrange(1, 1000, 5)


def _calculate(a, b):
    """
    Функция которая выполняет какую-то логику. При этом, ниже фикстура, которая
    отдаёт его в тест как объект, чтобы можно было применить там как
    именно как функцию.
    """
    if isinstance(a, int) and isinstance(b, int):
        return a + b
    else:
        return None


@pytest.fixture
def calculate():
    """
    Передача функции в тест используя фикстуру.
    """
    return _calculate


@pytest.fixture
def make_number():
    """
    Делаем какую-то логику, передаём управление тесту используя конструкцию
    yield и уже после того, как тест закончился, выполняем вторую часть кода.
    """
    print("I'm getting number")
    number = randrange(1, 1000, 5)
    yield number
    print(f"Number at home {number}")


@pytest.fixture
def get_db_session():
    """
    Создание сессии для работы с базой данных.
    """
    session = Session()
    try:
        yield session
    finally:
        session.close()


def delete_test_data(session, table, filter_data):
    """
    Функция для удаления данных из базы.
    """
    session.query(table).filter(filter_data).delete()
    session.commit()


def add_method(session, item):
    """
    Функция для добавления данных в базу.
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
    """
    return add_method


@pytest.fixture
def get_delete_method():
    """
    Пример фикстуры которая передаёт функцию для удаления данных в базу
    как объект в тест.
    """
    return delete_test_data
