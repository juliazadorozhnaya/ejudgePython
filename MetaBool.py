"""
Написать метакласс empty так, чтобы объекты, порождаемые созданным с его помощью классом, считались пустыми, если хотя
бы одно из полей объекта пусто. Поля класса проверять не надо.
"""

def bool(self):
    for key, value in self.__dict__.items():
        if not value:
            return False

    return True

class empty(type):
    def __init__(cls, name, bases, per):
        cls.__bool__ = bool
        return super().__init__(name, bases, per)

    def __call__(cls, *args, **kwargs):
        return super().__call__(*args, **kwargs)

