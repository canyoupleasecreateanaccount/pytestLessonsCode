from faker import Faker

"""
Пример описания билдера для локализации.
"""


class PlayerLocalization:

    def __init__(self, lang):
        """
        В зависимости от того, какой язык будет передан в этот билдер, на таком
        языке и будет работать наш фейкер. Дальше, дело за малым, объект будет
        наполнен точно так же, как и другие подобные объекты, только каждый на
        своём языке.
        """
        self.fake = Faker(lang)
        self.result = {
            "nickname": self.fake.first_name()
        }

    def set_number(self, number=11):
        """
        Добавляет в результат ключ number, для которого будет использовано
        переданное значение, если же такое отсутствует, то используем значение
        11 по-умолчанию.
        """
        self.result['number'] = number
        return self

    def build(self):
        """
        Возвращает наш обьект в виде JSON.
        """
        return self.result
