"""
Написать генератор-функцию LookSay() цифр последовательности Конвея «Look and Say».
Сама последовательность должна быть целочисленной. Описание в Википедии
"""

import itertools


def LookSay():
    number = [1]
    while True:
        for i in number:
            yield i
        new_number = []
        for k, g in itertools.groupby(number):
            new_number.append(len(list(g)))
            new_number.append(k)
        number = new_number

