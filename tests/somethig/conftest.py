import pytest


@pytest.fixture
def get_testing_scenarios(request):
    """
    Пример фикстуры, которая на основании полученных данных, возвращает
    разные значения.

    Example of fixture returns different data according to received params.
    """
    if request.param == 'scenario_1':
        return {"name": "John"}
    elif request.param == 'scenario_2':
        return {"name": "Ann"}
    else:
        return {"name": "Anton"}


@pytest.fixture
def get_magic_method(get_number):
    """
    Пример фикстуры которая возвращает метод как объект в автотест и при этом
    сохраняет контекст. Обратите внимание на параметры которые принимает
    фикстура, это совсем другая фикстура, результат который мы используем в
    методе который возвращаем.

    Example of fixture returns method as object in autotest and saves fixture
    context. Attention please for fixture params, it calls another one and uses
    results of it in returned method.
    """
    print(f"Polychili chislo bratik {get_number}")
    def _wrapped(additional_number):
        return additional_number + get_number
    return _wrapped
