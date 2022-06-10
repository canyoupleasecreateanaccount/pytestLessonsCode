import pytest

from src.baseclasses.response import Response
from src.schemas.user import User

from src.schemas.computer import Computer
from examples import computer


def test_getting_users_list(get_users, make_number):
    """
    Пример использования фикстуры которая отправляет запрос и возвращает
    респонс. Далее мы просто обрабатываем его с помощью нашего Response class
    применяя все доступные валидации.
    """
    Response(get_users).assert_status_code(200).validate(User)


@pytest.mark.development
@pytest.mark.production
@pytest.mark.skip('[ISSUE-23414] Issue with network connection')
def test_another():
    """
    Обычный тест, но не совсем. Обратите внимание на декораторы к нему.
    Мы скипаем его с определённым сообщением, а так же помечаем с каким скоупом
    его выполнять.
    """
    assert 1 == 2


@pytest.mark.development
@pytest.mark.parametrize('first_value, second_value, result', [
    (1, 2, 3),
    (-1, -2, -3),
    (-1, 2, 1),
    ('b', -2, None),
    ('b', 'b', None)
])
def test_calculator(first_value, second_value, result, calculate):
    """
    Вариант параметризации нашего теста, с несколькими параметрами за один
    раз.
    """
    assert calculate(first_value, second_value) == result


def test_pydantic_object():
    """
    Пример того, как после инициализации pydantic объекта, можно получить
    доступ к любому из его параметров.
    """
    comp = Computer.parse_obj(computer)
    print(comp.detailed_info.physical.color)
