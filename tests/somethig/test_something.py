import requests
import pytest

from src.generators.player_localization import PlayerLocalization
from src.enums.user_enums import Statuses
from src.baseclasses.response import Response
from src.schemas.computer import Inventory

import tables

"""
В этом файле рассмотрим примеры работы:
 1. С базой данных
 2. Параметризация ключей и поочерёдное их удаление
 3. Использование генератора в тестах 
 4. Кастомная генерацию локализаций
 
In the file we will learn:
 1. Working with database
 2. Key parametrize and delete it in object one by one
 3. Using generator in autotests
 4. Generator of custom localization
"""


@pytest.mark.parametrize("status", Statuses.list())
def test_generator_changing(status, get_player_generator):
    """
    Играемся с генератором, который был получен с помощью фикстуры.
    Вы можете попробовать изменить значение, написать новые методы и посмотреть
    как он будет реагировать.

    Playing with generator, that we received from fixture.
    Here you can change values, write some new useful methods and check how
    will it work.
    """
    print(get_player_generator.set_status(status).build())


@pytest.mark.parametrize("delete_key", [
    "account_status",
    "balance",
    "localize",
    "avatar"
])
def test_deleting_keys_in_object(delete_key, get_player_generator):
    """
    Пример того, как мы в определённом порядке удаляем каждое поле в объекте,
    который нам вернул генератор.

    Example of case when we delete one by one keys in received object.
    """
    object_to_send = get_player_generator.build()
    del object_to_send[delete_key]
    # print(object_to_send)


@pytest.mark.parametrize("localizations, loc", [
    ("fr", "fr_FR")
])
def test_updating_localization_in_generator(
        get_player_generator,
        localizations,
        loc
):
    """
    В этом примере мы получаем 2 генератора, один базовый и один, который ниже
    уровнем. Когда мы получили их, изменяем в генераторе локализацию, создаём
    экземпляр и обновляем им наш главный объект.

    In the test we receive two generators, first is main and second is included
    into first. We change localization in generator and update main using
    instance of second.
    """
    object_to_send = get_player_generator.update_inner_value(
        ['localize', localizations],
        PlayerLocalization(loc).set_number(15).build()
    ).build()
    print(object_to_send)


def test_human():
    """
    Пример отправки запроса, получения данных и использования Response class
    для работы с валидацией данных.

    Example of requesting data and push response into our Response class for
    future validation.
    """
    r = requests.get('https://petstore.swagger.io/v2/store/inventory')
    response = Response(r)
    response.validate(Inventory)


def test_get_data_films(get_db_session):
    """
    Получение сессии базы данных и использование её для того, чтобы достать
    нужную информацию.

    Getting database session. In the test, we get info from DB using the
    session.
    """
    data = get_db_session.query(tables.Films).first()
    print(data.film_id)


def test_try_to_delete_something(get_delete_method, get_db_session):
    """
    Пример того, как использовать удаление в тесте, когда мы не знаем ID.
    Просто получаем фикстуру которая умеет это делать и удаляем.
    Если тест упадёт раньше, то до этой строки кода мы не дойдём, так как
    удалять нет чего, если же мы дошли, то удалять есть что :).

    Example of case, when we know nothing about id that should be deleted from
    DB after test execution. So in that case we just paste our method at the end
    If our case fails we don't have to delete anything, if not
    our code will do what it has to do :)
    """
    #some code
    get_delete_method(get_db_session, tables.ItemType, (
            tables.ItemType.item_id == 3)
    )


def test_try_to_add_testdata(
        get_db_session, get_add_method, get_item_type_generator
):
    """
    Добавление в базу тестовых данных в самом тесте, плохой пример но может
    пригодится. Лучше используйте фикстуры.

    Adding test data into database in our test. It is very bad example.
    Please don't do like this.
    """
    item = tables.ItemType(**get_item_type_generator.build())
    get_add_method(get_db_session, item)
    print(item.item_id)


def test_try_to_add_testdata_and_delete_after_test(generate_item_type):
    """
    Пример идеального флоу, когда мы создаём и удаляем после себя данные в базе
    тем самым оставляя тест чистым.
    PS: Смотрите фикстуру

    Example of case, when we create and delete test data in our fixture.
    PS: Check fixtures.
    """
    print(generate_item_type.item_id)
