

class BuilderBaseClass:
    """
    Базовый класс для билдера. Вы его можете дополнить ещё другими полезными
    методами, сейчас представлен только один.
    """
    def __init__(self):
        self.result = {}

    def update_inner_value(self, keys, value):
        """
        Этот метод помогает обновить/добавить новое значение в объекте на
        указанном вами уровне.
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
