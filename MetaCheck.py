"""
Написать метакласс checker, с помощью которого при создании класса будет происходить два дополнительных действия: Все
аннотированные поля класса, имеющие заданные значения, будут проверяться на то, что значение соответствует аннотации-типу,
и в случае несоответствия — инициироваться исключение TypeError Для каждого неаннотированного поля, имеющего заданное
значения числового типа, будет создаваться соответствующая аннотация
"""

from fractions import Fraction as frac
import inspect
from decimal import Decimal
class checker(type):
    def __new__(cls, name, bases, attrs):
        new_attrs = attrs.copy()
        annotations = attrs.get('__annotations__', {})
        base_annotations = {}
        for base in bases:
            if hasattr(base, '__annotations__'):
                base_annotations.update(base.__annotations__)

        # Проверяем соответствие между новыми аннотациями и значениями базовых классов
        for attr_name, attr_type in annotations.items():
            if attr_name in base_annotations and not isinstance(base_annotations[attr_name], attr_type):
                raise TypeError("NOPE")


        combined_annotations = {**base_annotations, **annotations}


        for attr_name, attr_value in attrs.items():
            attr_type = combined_annotations.get(attr_name)
            if attr_type and not isinstance(attr_value, attr_type):
                raise TypeError(f"Value of {attr_name} does not match its annotation type: {attr_type}")
            if attr_name not in combined_annotations and isinstance(attr_value, (int, float, frac, Decimal)):
                combined_annotations[attr_name] = type(attr_value)

        new_attrs['__annotations__'] = combined_annotations
        return super().__new__(cls, name, bases, new_attrs)

