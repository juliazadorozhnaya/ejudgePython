"""
(эту задачу надо сдавать в EJudge, но основные свойства решения там пока проверить нельзя)
Написать функцию bubble(sequence: Sortable) -> Sortable, которая сортирует эелменты изменяемой последовательности и
возвращает её в отсортированном виде, и type alias Sortable, задающий изменяемую последовательность, элементы которой п
оддерживают операцию сравнения. В результате приведённый пример должен проходить mypy --strict, компилироваться mypyc и
выполняться из полученной библиотеки, а любая закомментированная строка из примера — вызывать ошибку проверки/компиляции.
"""

from typing import TypeVar, List, MutableSequence, cast

T = TypeVar('T', bound="Comparable")


class Comparable:
    def __lt__(self, other: "Comparable") -> bool:
        ...


Sortable = MutableSequence[T]


def bubble(sequence: Sortable[T]) -> Sortable[T]:
    length = len(sequence)
    for i in range(length):
        for j in range(0, length - i - 1):
            if sequence[j] > sequence[j + 1]:
                sequence[j], sequence[j + 1] = sequence[j + 1], sequence[j]
    return sequence
