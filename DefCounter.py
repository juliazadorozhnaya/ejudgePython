"""
Написать класс DefCounter, унаследованный от collections.Counter, в котором значения для несуществующих элементов были
бы не 0, а задавались в конструкторе именным параметром missing= (по умолчанию — -1). Дополнительно класс должен поддерживать
операцию abs(экземпляр), возвращающую сумму положительных элементов счётчика.
"""

from collections import Counter


class DefCounter(Counter):
    def __init__(self, iterable=None, **kwargs):
        self.missing = kwargs.get('missing', -1)
        super().__init__(iterable)

    def __getitem__(self, key):
        return super().__getitem__(key) if key in self else self.missing

    def __abs__(self):
        return sum(value for value in self.values() if value > 0)

