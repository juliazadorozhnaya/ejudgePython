"""
Напишите параметрический декоратор Record(строка, **именные_параметры) произвольного класса, использующего __slots__ в
качестве объектной модели. Декоратор должен добавлять в возвращаемый класс слоты, имена которых перечислены через пробел
в строке, и поля только для чтения, имена и значения которых перечислены в именных_параметрах. Имена не могут начинаться
на "_". Слоты возвращаемого класса перечисляются в алфавитном порядке. Имена полей могут перекрывать имена слотов родительского
класса. Дополнительно должна поддерживаться итерация по объекту — она возвращает имена слотов и полей
(имя которых не начинается на "_") в алфавитном порядке Дополнительно должно поддерживаться преобразование в строку в
таком формате (поля берутся также в алфавитном порядке): для неопределённых слотов выводится только имя, для определённых
— имя=значение, для переменных — имя:значение, разделитель — «|» (см. пример).
"""

def Record(slots_str, **fields):
    def decorator(cls):
        class Wrapped(cls):
            added_slots = slots_str.split()
            __slots__ = sorted(set(cls.__slots__ + added_slots))

            def __iter__(self):
                return iter(sorted(set(self.__slots__) | set(fields.keys())))

            def __str__(self):
                parts = []
                for attr in self:
                    if hasattr(self, attr):
                        parts.append(f"{attr}={getattr(self, attr)}")
                    elif attr in fields:
                        parts.append(f"{attr}:{fields[attr]}")
                    else:
                        parts.append(attr)
                return "|".join(parts)

        for field, value in fields.items():
            if field not in cls.__slots__:
                setattr(Wrapped, field, property(lambda self, value=value: value))

        return Wrapped

    return decorator


@Record("b c", d=11, e=12)
class C:
    __slots__ = ["a", "b"]
    c = 8
    d = 9


c = C()
c.a, c.c = 42, 100500
print(c, "//", "".join(c.__slots__))
for i, attr in enumerate(c):
    try:
        setattr(c, attr, i)
    except AttributeError:
        pass
    print(c, "//", *(getattr(c, attr, "<NOPE>") for attr in c))