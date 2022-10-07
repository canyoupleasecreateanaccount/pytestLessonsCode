import pytest


class Letter:

    def __init__(self, letter, position):
        self.letter = letter
        self.position = position

    def __str__(self):
        """
        Магический метод который отвечает за строчное отображение инстансов
        нашего класса.

        Magic method that we described for params displaying in test name.
        """
        return f"Letter {self.letter}, Position {self.position}"


def get_cases():
    return [
        Letter('a', 1),
        Letter('b', 2)
    ]


@pytest.mark.parametrize("my_value", get_cases(), ids=str)
def test_my_magic_method(my_value):
    """
    Пример использования ids=str, для того, чтобы отображать конкретные данные,
    которые мы передали нашему тесту.

    Example of using ids=str, that needs to concreate displaying of data that we
    passed into autotest.
    """
    print(my_value)


@pytest.mark.parametrize("get_testing_scenarios", ['scenario_1'], indirect=True)
def test_data_indirect(get_testing_scenarios):
    """
    Пример использования фикстуры с indirect параметром. В этом кейсе мы
    вызываем фикстуру напрямую и передаём ей параметры, а она же, возвращает
    нам какие-то данные основываясь на них.

    Example of using fixture with indirect parameter. In the case we call
    fixture with params, so it returns some data according to the params
    """
    print(get_testing_scenarios)


def test_magic_method(get_magic_method):
    """
    Пример использования метода, который мы получили из фикстуры как объект.

    Example of using method that we received from fixture as object.
    """
    print(get_magic_method(1))


def test_option(getting_env):
    """
    В этом примере мы получаем значение кастомного параметра.

    In the test we get custom params from console during pytest run.
    """
    print(getting_env)
