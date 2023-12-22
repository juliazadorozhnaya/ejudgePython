"""
Написать метакласс posistioned, который добавляет в создаваемый с его помощью класс три свойства:
Строковое представление экземпляра этого класса должно выглядеть как "поле1=значение1 поле2=значение2 …" для всех аннотированных
полей этого класса (в порядке их появления в аннотации). При создании экземпляра класса ему можно передавать произвольное
количество параметров (включая ноль). Первый параметр инициализирует первое аннотированное поле в этом экземпляре,
второй — второе и т. д.; если параметров больше, чем аннотированных полей, они отбрасываются
При сопоставлении шаблону допускается позиционное сопоставление с аннотированными полями (в порядке появления в аннотации)
"""

class positioned(type):
    def __new__(cls, name, bases, namespace):
        annotations = namespace.get('__annotations__', {})
        namespace['_fields'] = list(annotations.keys())
        namespace['__match_args__'] = tuple(namespace['_fields'])

        def __init__(self, *args, **kwargs):
            defaults = {field: getattr(self, field, None) for field in self._fields}
            values = dict(zip(self._fields, args), **kwargs)
            for field in self._fields:
                setattr(self, field, values.get(field, defaults[field]))

        namespace['__init__'] = __init__

        def __str__(self):
            return ' '.join(f"{field}={getattr(self, field, None)}" for field in self._fields)

        namespace['__str__'] = __str__

        return super().__new__(cls, name, bases, namespace)

