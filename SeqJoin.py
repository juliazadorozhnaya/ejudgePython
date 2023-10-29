"""
Написать генератор-функцию joinseq(seq0, seq1, …), принимающую на вход произвольное количество (возможно, бесконечных) последовательностей.
Порождаемый ею генератор должен всякий раз возвращать наименьший из начальных элементов этих последовательностей. Если таких несколько,
используется самый первый. Если последовательность закончилась, она больше не учитывается.
Итератор завершается, когда все последовательности иссякли. Условие: использовать обработку исключений в этой задаче нельзя.
"""


def joinseq(*seq):
    iterators = [iter(s) for s in seq]
    first_elements = {ind: next(it, None) for ind, it in enumerate(iterators)}

    while any(first_elements.values()):
        min_index = min((ind for ind, element in first_elements.items() if element is not None),
                        key=lambda ind: first_elements[ind])
        yield first_elements[min_index]
        first_elements[min_index] = next(iterators[min_index], None)
