"""
Напишите параметрический декоратор Record(строка, **именные_параметры) произвольного класса, использующего __slots__ в качестве
объектной модели. Декоратор должен добавлять в возвращаемый класс слоты, имена которых перечислены через пробел в строке, и поля
только для чтения, имена и значения которых перечислены в именных_параметрах. Имена не могут начинаться на "_". Слоты возвращаемого
класса перечисляются в алфавитном порядке. Имена полей могут перекрывать имена слотов родительского класса. Дополнительно должна
поддерживаться итерация по объекту — она возвращает имена слотов и полей (имя которых не начинается на "_") в алфавитном порядке
Дополнительно должно поддерживаться преобразование в строку в таком формате (поля берутся также в алфавитном порядке):
для неопределённых слотов выводится только имя, для определённых — имя=значение, для переменных — имя:значение, разделитель — «|» (см. пример).
"""


def Record(slots_str: str, **readonly_attrs):
    def decorator(cls):
        new_slots = set(slots_str.split())
        all_slots = sorted(set(cls.__slots__) | new_slots)

        class EnhancedClass(cls):
            __slots__ = all_slots

            def __iter__(self):
                attrs = sorted(attr for attr in dir(self) if not attr.startswith("_"))
                return iter(attrs)

            def __str__(self):
                def format_attr(attr):
                    value = getattr(self, attr, None)
                    separator = "=" if attr in self.__slots__ else ":"
                    return f"{attr}{separator}{value}" if value is not None else attr

                return "|".join(format_attr(attr) for attr in self)

        for attr, value in readonly_attrs.items():
            setattr(EnhancedClass, attr, value)

        return EnhancedClass

    return decorator
