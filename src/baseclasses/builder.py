

class BuilderBaseClass:
    """
    Базовый класс для билдера. Вы его можете дополнить ещё другими полезными
    методами, сейчас представлен только один.

    Base class for builder. You can add additional useful methods, but for now
    it has only one.
    """
    def __init__(self):
        self.result = {}

    def update_inner_value(self, keys, value):
        """
        Этот метод помогает обновить/добавить новое значение в объекте на
        указанном вами уровне.

        The method helps us update and add new values into object on specified
        level.
        """
        if not isinstance(keys, list):
            self.result[keys] = value
        else:
            temp = self.result
            for item in keys[:-1]:
                if item not in temp.keys():
                    temp[item] = {}
                temp = temp[item]
            temp[keys[-1]] = value
        return self

    def build(self):
        return self.result
