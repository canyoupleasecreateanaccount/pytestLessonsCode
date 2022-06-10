from faker import Faker

"""
Пример описания билдера для локализации.

Example of declaration for localization builder.
"""


class PlayerLocalization:

    def __init__(self, lang):
        """
        В зависимости от того, какой язык будет передан в этот билдер, на таком
        языке и будет работать наш фейкер. Дальше, дело за малым, объект будет
        наполнен точно так же, как и другие подобные объекты, только каждый на
        своём языке.

        Example of customizing low level builder. According to received lang,
        values in builder will be populated on the set language without any
        changes in logic of populating.
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

        Method adds into result key "number" with value that has been received
        from user, if not, we will set default that equal to 11.
        """
        self.result['number'] = number
        return self

    def build(self):
        """
        Возвращает наш обьект в виде JSON.

        Returns object as JSON.
        """
        return self.result
